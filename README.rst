DS Project Template
===================

Streamlining best practices in data science and analysis, with emphasis on reproducibility, quality, and ease of use.

Getting Started
---------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
~~~~~~~~~~~~~

First things first, you should ensure that your environment is ready to leverage all of the parts of this project (on Windows, anyhow)

- Ensure that you have Git Bash and Anaconda installed
- Second, `follow these steps <https://gist.github.com/evanwill/0207876c3243bbb6863e65ec5dc3f058#make>`_ to get set up with the ``make`` command.

Finally, install the ``CookieCutter`` Python library via

.. code:: none

   pip install cookiecutter


Quick Start
~~~~~~~~~~~

To start a new project with this template, simply use

.. code:: none
   
   cookiecutter https://github.com/NapsterInBlue/analysis-template

And follow along with the prompt, either accepting the defaults, [in braces] or replacing them with your own

.. code:: none
    
   project_name [project_name]: My Project
   repo_name [my_project]:
   author_name [Your name (or your organization/company/team)]: Idk, Dan Smith?
   description [A short description of the project.]: Technical Wizardry

Doing all of this will yield a project with the following structure with your responses filled in where appropriate

.. code:: none

   ├── Makefile           <- Makefile with commands like `make data` or `make report`
   ├── README.md          <- The top-level README for developers using this project.
   ├── data
   │   ├── interim        <- Intermediate data that has been transformed.
   │   ├── processed      <- The final, canonical data sets for modeling.
   │   └── raw            <- The original, immutable data dump.
   │
   ├── models             <- Trained and serialized models, model predictions, or model summaries
   │
   ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
   │                         and a short `_` delimited description, e.g.
   │                         `initial_data_exploration`.
   │
   ├── .pipconf           <- Configuration file do set default pip behavior (*NIX)
   ├── pip.ini            <- (Windows equivalent)
   │
   ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
   │
   ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
   │   └── figures        <- Generated graphics and figures to be used in reporting
   │
   ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
   │                         generated with `pip freeze > requirements.txt`
   │
   ├── src                <- Source code for use in this project.
   │   ├── __init__.py    <- Makes src a Python module
   │   │
   │   ├── data           <- Scripts to download or generate data. Naming convention is a
   │   │                     number (for ordering), and the name of the table they
   │   │        	     represent (from 01 onward) e.g.`03_population.py`
   │   │
   │   ├── features       <- Scripts to turn raw data into features for modeling
   │   │   └── build_features.py
   │   │
   │   ├── models         <- Scripts to train models and then use trained models to make
   │   │   │                 predictions
   │   │   ├── predict_model.py
   │   │   └── train_model.py
   │   │
   │   ├── utils          <- Handy user-defined functions imported into Notebooks so they can
   │   │                     REMAIN A PRESENTATION LAYER
   │   │
   │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
   │       └── visualize.py
   │
   │
   └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
  

Documentation
-------------
See the documentation at https://NapsterInBlue.github.io/analysis-template 

Contributing
------------

This is very much a work in progress. best ways to pitch in are:

1. Trying this out for size and letting us demo it as a success story
2. Opening up an issue to tell us why it didn't go so hot
3. Submitting a Pull Request **that tackles an existing issue**.
    - Make sure you add yourself to ``AUTHORS.rst``!
