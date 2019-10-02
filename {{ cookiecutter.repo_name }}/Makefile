.PHONY: clean data lint requirements

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DATA_DIR = $(PROJECT_DIR)/data/
PROJECT_NAME = project_name
TODAY = $(shell date +%Y%m%d)

## Check if user is running on Windows
UNAME = $(shell uname)

WIN=0
check_for_win =
ifneq (,$(findstring MING,$(UNAME)))
    WIN=1
endif
ifneq (,$(findstring MSYS,$(UNAME)))
    WIN=1
endif
ifneq (,$(findstring CYGWIN,$(UNAME)))
    WIN=1
endif

ifdef check_for_win
endif


# Different Python Calls 
ifeq ($(WIN), 1)
    PYTHON_INTERPRETER = winpty python.exe
else
    PYTHON_INTERPRETER = python
endif


#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up virtual environment
instantiate:
	pip install -U virtualenv
	virtualenv env

newvenv: instantiate
	mv -t env pip.ini .pipconf

## Test python environment is setup correctly
testenv:
	python test_environment.py

## Install Python Dependencies
requirements: test_environment
	pip install -U pip setuptools wheel
	pip install -r requirements.txt


## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Blow away all processed data
cleandata:
	find data/interim -type f -name "*.csv" -delete
	find data/processed -type f -name "*.csv" -delete

purgedata: cleandata
	find data/raw -type f -name "*.csv" -delete

## Lint using flake8
lint:
	flake8 src



#################################################################################
# PROJECT FLOW  - Make sure you've activated your virtual environment
#################################################################################

## Make Dataset(s)
raw:
	$(PYTHON_INTERPRETER) src/data/00_pull_data.py

interim: 
	$(PYTHON_INTERPRETER) src/data/01_table_name.py raw/input_file.csv interim/output_file.csv

processed: interim

data: processed
	@# Executes each of the above data prep steps above

## Build datestamped, read-only report using the following syntax
#
#      make report NBNAME=your_file.ipynb
#
report:
	$(eval OUTNAME := $(basename $(NBNAME)))
	$(eval SAVENAME := $(OUTNAME)_$(TODAY).ipynb)
	jupyter nbconvert --execute --to notebook --inplace notebooks/reports/$(NBNAME)
	cd notebooks && cp reports/$(NBNAME) ../reports/$(SAVENAME)
	chmod =r reports/$(SAVENAME)
