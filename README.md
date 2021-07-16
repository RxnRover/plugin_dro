# Deep Reaction Optimizer Plugin

This plugin allows Rxn Rover to connect with an instance of the Deep Reaction 
Optimizer (DRO). [1] A Python program is provided with the plugin to launch an 
instance of DRO for use with this plugin. This program uses a modified 
objective function with built-in communication capabilities. The DRO algorithm, 
along with other aspects of the program, can be configured by specifying a 
configuration file (example files are provided).

Please be sure to cite the DRO authors using the paper below when using this 
plugin!

[1] Zhou, Z.;  Li, X.; Zare, R. N., Optimizing Chemical Reactions with Deep Reinforcement Learning. ACS Central Science 2017, 3 (12), 1337-1344.; DOI: 10.1021/acscentsci.7b00492; Code available at: https://github.com/lightingghost/chemopt.

## Installation

### Prerequisites

This plugin requires Python >= 3.4 and <= 3.7. Download it from https://www.python.org/.

### Getting the Plugin

Download this plugin by clicking the "Code" button in the top right of its 
GitHub repository and selecting "Download ZIP". Extract the ZIP file into your 
`<documents>/Plugins/Optimizers` directory. 

### Setting up DRO

Inside `<documents>/Plugins/Optimizers/Deep Reaction Optimizer` there are two folders, 
`plugin`, where the Rxn Rover plugin resides, and `dro2`, where the necessary 
code to launch an instance of SQSnobFit that can communicate with the plugin. 
If you are using Linux or Mac, simply type `make install` in the `dro2`
directory to download and install dependencies into a virtual environment.

If using Windows, open a terminal in the `dro2` directory and type the 
following commands:

```batch
python -m venv venv             # Creates a virtual environment (venv)
.\venv\Scripts\activate         # Activates the venv
pip install -r requirements.txt # Installs dependencies in venv
deactivate                      # Deactivates the venv
```

## Configurations

The DRO optimization can be configured by editing or creating a new 
config file in the `dro2/config` directory. An example
configuration file with default values is provided as `default-config.json`.

## Plugin Scripts

Scripts used by the plugin are located in the 
`dro2/scripts` subdirectory. When creating a new script,
ensure that it activates the `venv`, runs `src/main.py` with the correct 
config file as a command line argument, and deactivates the `venv` when 
complete.
