import json
from collections import namedtuple

class Config(object):
    """Provides additional parsing of config.json elements.

    Attributes:
        config: Parsed config.json file 
    """

    def __init__(self, config_file):
        """Sets json file to be parsed. (Must be open)

        Args:
            config_file: Open config.json file to parse
        """

        self.file_name = config_file.name
        self.config = json.load(config_file,
                       object_hook=lambda d:namedtuple('x', d.keys())(*d.values()))

    def batch_norm(self):
        """
        Wrapper for batch_norm of config.json.
        
        Returns:
            Boolean value of batch_norm
        """
        
        return bool(self.config.batch_norm)

    def batch_size(self):
        """
        Wrapper for batch_size of config.json.
        
        Returns:
            Integer value of batch_size
        """
        
        return int(self.config.batch_size)

    def constraints(self):
        """
        Wrapper for constraints of config.json.
        
        Returns:
            Boolean value of constraints
        """
        
        return bool(self.config.constraints)

    def discount_factor(self):
        """
        Wrapper for discount_factor of config.json.
        
        Returns:
            Floating point value of discount_factor
        """
        
        return float(self.config.discount_factor)

    def evaluation_epochs(self):
        """
        Wrapper for evaluation_epochs of config.json.
        
        Returns:
            Integer value of evaluation_epochs
        """
        
        return int(self.config.evaluation_epochs)

    def evaluation_period(self):
        """
        Wrapper for evaluation_period of config.json.
        
        Returns:
            Integer value of evaluation_period
        """
        
        return int(self.config.evaluation_period)

    def hidden_size(self):
        """
        Wrapper for hidden_size of config.json.
        
        Returns:
            Integer value of hidden_size
        """
        
        return int(self.config.hidden_size)

    # DEBUG: figure out type of instrument_error
    def instrument_error(self):
        """
        Wrapper for instrument_error of config.json.
        
        Returns:
            ____ value of instrument_error
        """
        
        return self.config.instrument_error

    def ip_address(self):
        """
        Wrapper for ip_address of config file.

        Returns:
            String value of IP address (without the port)
        """

        return self.config.ip_address
    
    def learning_rate(self):
        """
        Wrapper for learning_rate of config.json.
        
        Returns:
            Floating point value of learning_rate
        """
        
        return float(self.config.learning_rate)
        
    def log_path(self):
        """
        Wrapper for log_path of config.json.
        
        Returns:
            String value of log_path
        """
        
        return self.config.log_path

    def log_period(self):
        """
        Wrapper for log_period of config.json.
        
        Returns:
            Integer value of log_period
        """
        
        return int(self.config.log_period)

    def loss_type(self):
        """
        Wrapper for loss_type of config.json.
        
        Returns:
            String value of loss_type
        """
        
        return self.config.loss_type

    def lr_decay(self):
        """
        Wrapper for lr_decay of config.json.
        
        Returns:
            Floating point value of lr_decay
        """
        
        return float(self.config.lr_decay)
    
    def norm_cov(self):
        """
        Wrapper for norm_cov of config.json.
        
        Returns:
            Floating point value of norm_cov
        """
        
        return float(self.config.norm_cov)

    def num_epochs(self):
        """
        Wrapper for num_epochs of config.json.
        
        Returns:
            Integer value of num_epochs
        """
        
        return int(self.config.num_epochs)

    def num_layers(self):
        """
        Wrapper for num_layers of config.json.
        
        Returns:
            Integer value of num_layers
        """
        
        return int(self.config.num_layers)

    def num_params(self):
        """
        Wrapper for num_params of config.json.
        
        Returns:
            Integer value of num_params
        """
        
        return int(self.config.num_params)

    def num_steps(self):
        """
        Wrapper for num_steps of config.json.
        
        Returns:
            Integer value of num_steps
        """
        
        return int(self.config.num_steps)

    def opt_direction(self):
        """
        Wrapper for opt_direction of config.json.
        
        Returns:
            String value of opt_direction
        """
        
        return self.config.opt_direction

    def optimizer(self):
        """
        Wrapper for optimizer of config.json.
        
        Returns:
            String value of optimizer
        """
        
        return self.config.optimizer
        
    def param_names(self):
        """
        Parse parameter names from the param_names in config.json.
        
        Returns:
            list of strings containing parameter names
        """
        
        return list(self.config.param_names)
    
    def param_ranges(self):
        """Parse parameter ranges from the param_range in config.json. 
        
        Returns:
            ranges: list of floating point tuples representing the ranges
            None: Mismatch in number of param names and ranges
        """

        param_ranges = self.config.param_ranges
        ranges = []  # List of tuples for ranges

        # Check for a mismatch between the number of parameter names
        # and the number of ranges given. This also ensures that
        # the number of range minima equal the number of range
        # maxima.
        
        if(self.num_params() != len(param_ranges.min) or
           self.num_params() != len(param_ranges.max)):
            return None

        for i in range(self.num_params()):
            tmp = (param_ranges.min[i], param_ranges.max[i])  # Create tuples
            ranges.append(tmp)  # Append tuples

        return ranges

    def param_init(self):
        """
        Parse initial parameter values, which can be an empty list

        Returns:
            list of numbers representing initial parameter values
        """

        x0 = self.config.param_init

        # Return None if the parameter list is not empty or has an
        # incorrect number of parameters
        if (len(x0) != 0 and len(x0) != self.num_params()):
            return None
        
        return list(self.config.param_init)
    
    def policy(self):
        """
        Wrapper for policy of config.json.
        
        Returns:
            String value of policy
        """
        
        return self.config.policy

    def port(self):
        """
        Wrapper for port of config.json.
        
        Returns:
            Integer value of port number
        """
        
        return int(self.config.port)
    
    def reaction_type(self):
        """
        Wrapper for reaction_type of config.json.
        
        Returns:
            String value of reaction_type
        """
        
        return self.config.reaction_type

    def reuse(self):
        """
        Wrapper for reuse of config.json.
        
        Returns:
            Boolean value of reuse
        """
        
        return bool(self.config.reuse)

    def save_path(self):
        """
        Wrapper for save_path of config.json.
        
        Returns:
            String value of save_path
        """
        
        return self.config.save_path

    def trainable_init(self):
        """
        Wrapper for trainable_init of config.json.
        
        Returns:
            String value of trainable_init
        """
        
        return bool(self.config.trainable_init)

    
    def unroll_length(self):
        """
        Wrapper for unroll_length of config.json.
        
        Returns:
            Integer value of unroll_length
        """
        
        return int(self.config.unroll_length)

    def zmq(self):
        """
        Wrapper for zmq flag of config.json.

        Returns:
            Boolean value of whether to use ZMQ or not.
        """

        return bool(self.config.zmq)
    
# For testing purposes only

if __name__ == "__main__":
    config_file = open("../config/default-config.json")
    p = Config(config_file)

    print("file_name: " + str(p.file_name))
    print("num_params: " + str(p.num_params()))
    print("param_names: " + str(p.param_names()))
    print("param_ranges: " + str(p.param_ranges()))
    print("param_init: " + str(p.param_init()))
    print("log_path: " + str(p.log_path()))
    print("save_path: " + str(p.save_path()))
    print("batch_size: " + str(p.batch_size()))
    print("hidden_size: " + str(p.hidden_size()))
    print("num_layers: " + str(p.num_layers()))
    print("batch_norm: " + str(p.batch_norm()))
    print("reuse: " + str(p.reuse()))
    print("num_epochs: " + str(p.num_epochs()))
    print("log_period: " + str(p.log_period()))
    print("evaluation_period: " + str(p.evaluation_period()))
    print("evaluation_epochs: " + str(p.evaluation_epochs()))
    print("reaction_type: " + str(p.reaction_type()))
    print("norm_cov: " + str(p.norm_cov()))
    print("constraints: " + str(p.constraints()))
    print("instrument_error: " + str(p.instrument_error()))
    print("num_steps: " + str(p.num_steps()))
    print("unroll_length: " + str(p.unroll_length()))
    print("learning_rate: " + str(p.learning_rate()))
    print("lr_decay: " + str(p.lr_decay()))
    print("optimizer: " + str(p.optimizer()))
    print("loss_type: " + str(p.loss_type()))
    print("discount_factor: " + str(p.discount_factor()))
    print("opt_direction: " + str(p.opt_direction()))
    print("policy: " + str(p.policy()))
    print("trainable_init: " + str(p.trainable_init()))
    print("zmq: " + str(p.zmq()))
    print("ip_address: " + str(p.ip_address()))
    print("port: " + str(p.port()))
