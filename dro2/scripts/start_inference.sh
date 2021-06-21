#!/bin/bash

# Activate the virtual environment
source ../venv/bin/activate

# Run the Python optimizer using the default "python" command *must be in PATH*
python "../dro2/realreaction.py" "../config/default-config.json"

# Deactivate the virtual environment when finished
deactivate

# Pause after the script is finished for debugging
if [ "$1" = "DEBUG" ]; then
    read -n1 -r -p "Press 'y' key to continue..." key
fi
