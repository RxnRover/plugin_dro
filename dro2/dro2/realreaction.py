#!/usr/bin/env python3

import argparse
import tensorflow as tf
import numpy as np
import logging
import matplotlib.pyplot as plt
import json
import zmq # For message queues

import rnn
from reactions import QuadraticEval, ConstraintQuadraticEval, RealReaction, RealReactionZMQ
from logger import get_handlers
from collections import namedtuple
from Config import Config

class StepOptimizer:
    def __init__(self, cell, func, ndim, nsteps, ckpt_path, logger, constraints, x0=[]):
        self.logger = logger
        self.cell = cell
        self.func = func
        self.ndim = ndim
        self.nsteps = nsteps
        self.ckpt_path = ckpt_path
        self.constraints = constraints
        self.init_state = self.cell.get_initial_state(1, tf.float32)
        self.results = self.build_graph()

        self.saver = tf.train.Saver(tf.global_variables())
        self.x0 = x0

    def get_state_shapes(self):
        return [(s[0].get_shape().as_list(), s[1].get_shape().as_list())
                for s in self.init_state]

    def step(self, sess, x, y, state):
        feed_dict = {'input_x:0':x, 'input_y:0':y}
        for i in range(len(self.init_state)):
            feed_dict['state_l{0}_c:0'.format(i)] = state[i][0]
            feed_dict['state_l{0}_h:0'.format(i)] = state[i][1]
        new_x, new_state = sess.run(self.results, feed_dict=feed_dict)
        return new_x, new_state

    def build_graph(self):
        x = tf.placeholder(tf.float32, shape=[1, self.ndim], name='input_x')
        y = tf.placeholder(tf.float32, shape=[1, 1], name='input_y')
        state = []
        for i in range(len(self.init_state)):
            state.append((tf.placeholder(
                              tf.float32, shape=self.init_state[i][0].get_shape(),
                              name='state_l{0}_c'.format(i)),
                          tf.placeholder(
                              tf.float32, shape=self.init_state[i][1].get_shape(),
                              name='state_l{0}_h'.format(i))))

        with tf.name_scope('opt_cell'):
            new_x, new_state = self.cell(x, y, state)
            if self.constraints:
                new_x = tf.clip_by_value(new_x, 0.01, 0.99)
        return new_x, new_state

    def load(self, sess, ckpt_path):
        ckpt = tf.train.get_checkpoint_state(ckpt_path)
        if ckpt and ckpt.model_checkpoint_path:
            self.logger.info('Reading model parameters from {}.'.format(
                ckpt.model_checkpoint_path))
            self.saver.restore(sess, ckpt.model_checkpoint_path)
        else:
            raise FileNotFoundError('No checkpoint available')

    def get_init(self):
        if (len(self.x0) == 0):
            x = np.random.normal(loc=0.5, scale=0.2, size=(1, self.ndim))
            x = np.maximum(np.minimum(x, 0.9), 0.1)
        else:
            x = np.array(self.x0).reshape((1, self.ndim))
        y = np.array(self.func(x)).reshape(1, 1)
        init_state = [(np.zeros(s[0]), np.zeros(s[1]))
                      for s in self.get_state_shapes()]
        return x, y, init_state

    def run(self):
        with tf.Session() as sess:
            self.load(sess, self.ckpt_path)
            x, y, state = self.get_init()
            x_array = np.zeros((self.nsteps + 1, self.ndim))
            y_array = np.zeros((self.nsteps + 1, 1))
            
            # If a stop command was received, stop optimizing
            if (y == -1):
                print("Exit Received, breaking out of optimization loop in StepOptimizer.run()") # DEBUG
                return x_array, y_array
            
            x_array[0, :] = x
            y_array[0] = y
            for i in range(self.nsteps):
                x, state = self.step(sess, x, y, state)
                y = self.func(x)
                
                # If a stop command was received, stop optimizing
                if (y == -1):
                    print("Exit Received, breaking out of optimization loop in StepOptimizer.run()") # DEBUG
                    break
                
                y = np.array(y).reshape(1, 1)
                x_array[i+1, :] = x
                y_array[i+1] = y

        return x_array, y_array

# This is setting up a Reply-Request model client
# so it will start by sending a request and waiting
# for a reply
def init_socket(binding):
    print("Binding socket at {} ...".format(binding))

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(binding)
    
    print("Binding complete!")

    return socket

def parse_args():
    """Parse command line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("config_file")

    args = parser.parse_args()

    return args

def main():
    
    # Parse command line arguments
    args = parse_args()

    logging.basicConfig(level=logging.ERROR, handlers=get_handlers())
    #logging.basicConfig(level=logging.INFO, handlers=get_handlers())
    logger = logging.getLogger()

    
    # Open and parse the config file
    config_file = open(args.config_file)
    config = Config(config_file)
    config_file.close()
    logger.info(str(config.config))
    
    param_names = config.param_names()
    param_range = config.param_ranges()
    logger.info(str(param_range))
    
    # Scale initialized parameter values
    x0 = config.param_init()
    if (len(x0) != 0):
        for i in range(config.num_params()):
            a, b = config.param_ranges()[i]
            x0[i] = (x0[i] - a) / (b - a)

    # Use the ZMQ method if indicated in the config file
    if (config.zmq()):
        # Bind to local socket
        binding = config.ip_address() + ":" + str(config.port())
        socket = init_socket(binding)

        func = RealReactionZMQ(num_dim=config.num_params(),
                               param_range=param_range,
                               param_names=param_names,
                               direction=config.opt_direction(),
                               logger=None,
                               socket=socket)
    else:
        func = RealReaction(num_dim=config.num_params(),
                               param_range=param_range,
                               param_names=param_names,
                               direction=config.opt_direction(),
                               logger=None)


    cell = rnn.StochasticRNNCell(cell=rnn.LSTM,
                                 kwargs={'hidden_size':config.hidden_size()},
                                 nlayers=config.num_layers(),
                                 reuse=config.reuse())
    
    optimizer = StepOptimizer(cell=cell, func=func, ndim=config.num_params(),
                              nsteps=config.num_steps(),
                              ckpt_path=config.save_path(), logger=logger,
                              constraints=config.constraints(),
                              x0=x0)
    
    x_array, y_array = optimizer.run()
    
    # plt.figure(1)
    # plt.plot(y_array)
    # plt.show()
    
if __name__ == '__main__':
    main()
