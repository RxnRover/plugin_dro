@ECHO off

:: Activate the virtual environment
call ..\venv\Scripts\activate.bat

:: Run the Python optimizer using the default "python" command *must be in PATH*
python "..\dro2\realreaction.py" "..\config\2xflow_percent_temp_yield_2021_04_19.json"

:: Deactivate the virtual environment when finished
call ..\venv\Scripts\deactivate.bat

:: Pause after the script is finished for debugging
IF "%1" == "DEBUG" (
    pause
)
