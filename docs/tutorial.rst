Tutorial
========

Assuming you've already completed the :doc:`introduction`, this tutorial should
take you the rest of the way.

.. _make-organization:

Makefiles and this Project Template
-----------------------------------
We're going to leverage Makefiles heavily throughout this project flow, so if
you haven't already, `get set up with the make command
<https://gist.github.com/evanwill/0207876c3243bbb6863e65ec5dc3f058#make>`_.

.. _make-venv:

Make and Virtual Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Virtual Environments are a key component to any project aiming to be
reproducible across platforms. We've added some helpful ``make`` commands to
facilitate easy use.

 1. Run ``make newvenv`` when creating a new project
 2. Activate your environment with ``source ./env/Scripts/activate``
 3. ``pip install`` the packages that your analysis needs
 4. Run ``pip freeze > requirements.txt`` to pin the exact package versions used to recreate the analysis
 5. If you find you need to install another package, run ``pip freeze > requirements.txt`` again and commit the changes to version control.
 6. Exit the virtual environment with ``deactivate``

Make and Data Generation
~~~~~~~~~~~~~~~~~~~~~~~~
Per our :ref:`immutable-data` philosophy, our goal is to be able to summon all
of the data that we need via simple commands, with **ZERO** manual tinkering in Excel
or Python. Therefore, all data saved in the ``interim`` and ``processed``
folders are ignore by git by default.

To that end, if you were to open up the Makefile to the "Project Flow" section,
you'll see the following.

.. code:: none

    ## Make Dataset(s)
    raw:
        $(PYTHON_INTERPRETER) src/data/00_pull_data.py

    interim: 
        $(PYTHON_INTERPRETER) src/data/01_table_name.py raw/input_file.csv interim/output_file.csv

    processed: interim

    data: processed
        @# Executes each of the above data prep steps above

Some explanation of what's going on here-- the first level of indentation
creates commands, and everything the next level of tab-indentation in gets
executed as a result. For instance, ``make raw`` will invoke the python
interpreter to run the file located at ``src/data/00_pull_data.py``.

Next, you may notice that some commands have other commands directly to the
right of them after the ``:``. This creates a command-chaining behavior.
Therefore invoking ``make data`` first invokes ``make process`` which invokes
``make interim`` before actually executing. This allows for some tidy
separation of section to section. 

More on this in :ref:`pipelining-data`.

.. note::

   We separate out ``raw``, ``interim``, and ``processed`` for convenience.
   Leaving any command blank will simply execute nothing, silently.

   Thus, you may consider adding a ``make alldata`` call that chains all of the
   processes together when you've got a good data flow going.

Finally, you can use ``make cleandata`` to remove all files from ``data/interim``
and ``data/processed``, and ``make purgedata`` to get ``data/raw``, as well.

Exploratory Data Analysis
---------------------------

Gather Raw Data
~~~~~~~~~~~~~~~
Our first goal is to generate a dataset saved in ``data/raw`` to start
exploring. This can take the form of a ``.csv`` downloaded from a site or the
result of some query.

.. important::

   All data is ignored by default, so any scripts/queries used to generate the
   data should be saved and descriptively-named in the appropriate location of ``src/data``

Make A Dummy Notebook at Root
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Notebooks located at the top level of your project are ignored by default, so
this makes for a very cheap and effective way to start working through some of
your data processing steps.

As you figure out steps that process your data effectively, you'll want to
graduate on to

.. _pipelining-data:

Pipelining Your Data
~~~~~~~~~~~~~~~~~~~~

After you've poked around in the base dataset awhile, you may have identified
transformations that get it closer to the polished dataset you intend to
actually work with. This probably includes

- Filtering
- Column Renaming
- Type Cleaning
- Missing Data Handling

Now you want to pull all of that preprocessing code *out of your notebook* and
into ``.py`` files located in ``src/data`` that can be effectively maintained.

A lot of work has gone into ensuring simple use of files located in ``src/data``.
The functions located in ``src/data/helpers.py`` figure out a lot of the file
IO for you.

Thus, the workflow of adding another data processing step should
be:

1. Save a new copy of ``src/data/template.py`` at the same location with a
   filename of the form ``<# execution step>_<data_step_it_represents>.py``
2. Add a new line to the relevant ``Project Flow`` section of your makefile
   that looks like the following

.. code:: none

   $(PYTHON_INTERPRETER) ##_filename.py in_data_layer/file out_data_layer/file

3. Run ``make data`` to transfer from your ``raw`` layer to ``interim`` and
``processed``


Making More Formal Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you've finished poking around in your dummy notebook at the top of the
project and want to start sharing the work you've done head into the
``notebooks`` folder.

.. important::
   
   Make sure that you're executing ``jupyter notebook`` from the main directory
   of your project. Failure to do so will mean you can't import code saved
   under ``src/``

Here, you'll find a few things:

- An ``exploratory`` subfolder where you can profile the data
- A ``reporting`` subfolder used for writing up more formal analysis (more on
  this in :ref:`reports`
- ``Template.ipynb`` notebooks in each of these subfolders with boilerplate
  imports and code
    
    - Save a new copy, **not delete**, these files when making a new notebook

- A ``nbutils.py`` file containing functions allowing easier refactoring and
  cleaner-looking code

.. _reports:

Generate Reports
----------------
Where you'll find that this structure really shines is in its ability to
generate prestine reporting.

Because we've refactored all of the heavy-lifting code out of our Notebooks and
into ``src`` (per :ref:`notebook-rules`!) we can now lean on Jupyter notebooks
as an impressive presentation layer. We can generate report of any notebook
located in ``notebooks/reports`` with the following:

.. code:: none

   make report NBNAME=<your_notebook>.ipynb

.. warning::

   This section of the makefile is regrettably finicky, the ``NBNAME=``
   argument is very important


Doing this will yield you a few interesting benefits. The command:

- Executes the notebook from top to bottom, helping you ensure that your
  analysis follows a logical progression
- Saves the file with a ``YYYYMMDD`` of the day the report was generated to the
  ``reports`` directory located at the root of your project
- Makes the file read-only, ergo more tamper-proof
- Watermarks your report at the very bottom with the commit hash ID of the
  project at the time of generation 
