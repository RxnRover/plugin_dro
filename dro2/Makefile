# Author: Zachery Crandall
# Email:  zachcran@iastate.edu
#
# Makefile to make Deep Reaction Optimizer a bit easier to work with on Linux and Mac OS.

PROJECT = "dro2"

DOCS = documentation

CONFIG = config
SRCDIR = dro2
SCRIPTDIR = scripts
OUTPUT = output

# Python
PYTHON = python3
PIP = pip3
REQFILE = requirements.txt
VENVDIR = ./venv

# Set bash shell so the `source` command is available
SHELL := /bin/bash

.DEFAULT_GOAL := help
.PHONY: clean veryclean run train install all help

# Targets include all, clean, debug, tar

install : venv
	@source $(VENVDIR)/bin/activate; \
	echo "----- INSIDE VENV -----"; \
	$(PIP) install -r $(REQFILE); \
	$(PIP) freeze; \
	deactivate

venv :
	@echo "CREATING VENV AT $(VENVDIR)"
	$(PYTHON) -m venv $(VENVDIR)

run : output
	cd ./$(SCRIPTDIR); \
	source ./start_inference.sh

output :
	mkdir -p ./$(OUTPUT)

train : output
	cd ./$(SCRIPTDIR); \
	./start_training.sh

clean :
	rm -rf ./*.tgz ./*.zip ./$(SRCDIR)/__pycache__

veryclean : clean
	rm -rf ./$(VENVDIR) ./$(OUTPUT)

tar: clean
	tar zcvf ./$(PROJECT).tgz README.* LICENSE requirements.txt $(DOCS) $(SRCDIR) \
		 $(CONFIG) $(OUTPUT)/ckpt Makefile $(SCRIPTDIR)

zip : clean
	zip -r ./$(PROJECT).zip README.* LICENSE requirements.txt $(DOCS) $(SRCDIR) \
	       $(CONFIG) $(OUTPUT)/ckpt Makefile $(SCRIPTDIR) 

help:
	@echo " Makefile usage:"
	@echo "	make clean   - remove compressed files and __pycache__"
	@echo "	make install - installs all dependencies in a venv, creating the venv if necessary"
	@echo "	make run     - starts model inference using start_inference.sh"
	@echo "	make train   - trains the model according to the start_training.sh"
	@echo "	make venv    - creates a venv. This is called when make install is used."
	@echo "	make veryclean - \`make clean\` and remove output and venv directories."
	@echo ""
	@echo " Help with this Makefile:"
	@echo "	make         - same as make help"
	@echo "	make help    - this message"
	@echo ""
	@echo " Compression and Distribution:"
	@echo "	make tar     - make a tarball of project files"
	@echo "	make zip     - make a zip of project files"
