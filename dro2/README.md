# dro2

This is a modified version of Deep Reaction Optimizer (DRO) which has been 
reorganized and modified to use an objective function which will communicate 
with the 
[Deep Reaction Optimizer plugin](https://github.com/RxnRover/plugin_dro) for 
[Rxn Rover](https://github.com/RxnRover/RxnRover). 

This modified version of DRO has been modified so that:

- an initial guess can be provided, 
- the number of parameters, parameter names, and parameter ranges can be changed, 
- the objective function used to communicate with the Rxn Rover plugin can be turned
on and off, and 
- the IP address and port used to communicate with the plugin
can be changed in the configuration file.

# Original Project

We thank the original authors of DRO for their hard work and publication of DRO
as a free tool for others to use an expand upon. Their original license is 
retained at the bottom of the LICENSE file, as per the terms of the MIT license.
Please view their associated publication and GitHub repository below, and be 
sure to cite them when using the DRO plugin in your experiments!

Paper: Zhou, Z.;  Li, X.; Zare, R. N., Optimizing Chemical Reactions with Deep Reinforcement Learning. ACS Central Science 2017, 3 (12), 1337-1344.; DOI: 10.1021/acscentsci.7b00492

Original DRO available at: https://github.com/lightingghost/chemopt.