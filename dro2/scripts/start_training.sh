#!/bin/bash

################################################################################
#
# Multiple Model Training Script
#
# Author: Zachery Crandall
#
# Description:
# Use this script to train one or more models, one after another. Be sure to
# update values labelled with a comment starting with UPDATE (a search works
# well to find them).
#
################################################################################

# UPDATE this virtual environment variable to the correct path to your venv
# activate function
VENV="../venv/bin/activate"

# Activate the venv
source $VENV


################################################################################
#
# UPDATE this section by:
#
# 1) Changing the ``cp'' commands to copy your custom config file to config.json
#
# 2) Update the OUTPUT files of the ``python'' commands to uniquely represent
#    the model
#
# 3) Ensure that the ``save_path'' directory specified in each config file is
#    unique for each model and already exists
#
################################################################################

# Train the model using the specified config, outputting to a unique output file
python ../dro2/lets_start.py ../config/default-config.json > ../output/OUTPUT_default

# Repeat for however many more models you have...

# python ../dro2/lets_start.py ../config/example_config.json > ../output/OUTPUT_example


# Deactivate the venv
deactivate
