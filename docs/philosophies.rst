*Disclaimer: Large portions of this were lifted from the writeup for* `DrivenData's CookieCutter implementation <https://drivendata.github.io/cookiecutter-data-science/>`_.

Design Philosophies
===================

There are some opinions implicit in the project structure that have grown out of our experience with what works and what doesn't when collaborating on data science projects. Some of the opinions are about workflows, and some of the opinions are about tools that make life easier. Here are some of the beliefs which this project is built on.


.. _immutable-data:

Data is immutable
-----------------
Don't ever edit your raw data, especially not manually, and especially not in Excel. Don't overwrite your raw data. Don't save multiple versions of the raw data. Treat the data (and its format) as immutable. The code you write should move the raw data through a pipeline to your final analysis. You shouldn't have to run all of the steps every time you want to make a new figure (see :ref:`analysis-dag`), but anyone should be able to reproduce the final products with only the code in ``src`` and the data in ``data/raw``.

Also, if data is immutable, it doesn't need source control in the same way that code does. Therefore, **by default, the data folder is included in the ``.gitignore`` file**. If you have a small amount of data that rarely changes, you may want to include the data in the repository. Github currently warns if files are over 50MB and rejects files over 100MB. Often, though you'll want to version any data retrieval queries used to populate ``data/raw`` in the ``src/data/queries`` folder. 

.. _notebook-rules:

Notebooks are for exploration and communication
-----------------------------------------------
Notebook packages like the Jupyter notebook, Zeppelin, and other literate programming tools are very effective for exploratory data analysis. However, these tools can be less effective for reproducing an analysis. When we use notebooks in our work, we often subdivide the ``notebooks`` folder. For example, ``notebooks/exploratory`` contains initial explorations, whereas ``notebooks/reports`` is more polished work that can be exported to the ``reports`` directory.

Since notebooks are challenging objects for source control (e.g., diffs of the ``json`` are often not human-readable and merging is near impossible), **we recommended not collaborating directly with others on Jupyter notebooks.** There are two steps we recommend for using notebooks effectively:

 1. Follow a naming convention that shows the owner and the order the analysis was done in. We use the format ``<step>-<ghuser>-<description>.ipynb`` (e.g., ``0.3-bull-visualize-distributions.ipynb``).

 2. Refactor the good parts. Don't write code to do the same task in multiple notebooks. If it's a data preprocessing task, put it in the pipeline at ``src/data`` and load data from ``data/interim``. If it's useful utility code, refactor it to ``src``.


.. _analysis-dag:

Analysis is a DAG
-----------------
Often in an analysis you have long-running steps that preprocess data or train models. If these steps have been run already (and you have stored the output somewhere like the ``data/interim`` directory), you don't want to wait to rerun them every time. We prefer ``make`` for managing steps that depend on each other, especially the long-running ones. Make is a common tool on Unix-based platforms (but is `available for Windows <https://gist.github.com/evanwill/0207876c3243bbb6863e65ec5dc3f058#make>`_). Following the ``make`` documentation will go a long way to ensure that your Makefiles work platform-to-platform.

We'll cover using these files effectively in :ref:`make-organization`.


Build from the environment up
-----------------------------

The first step in reproducing an analysis is always reproducing the computational environment it was run in. You need the same tools, the same libraries, and the same versions to make everything play nicely together.

One effective approach to this is use ``virtualenv``. By listing all of your requirements in the repository (we include a `requirements.txt` file) you can easily track the packages needed to recreate the analysis. 

You'll find a good workflow at :ref:`make-venv`.
