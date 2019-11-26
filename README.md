# PyReData
<p style="text-align:justify">Allows to share analysis and visualizations done using Python as HTML web pages. Still a work in progress. You can run the PIMA example under examples folder to get a feel of the library. The example will be updated with further progress being made during development. </p>

<h1>Installation</h1>

PyReData supports Pandas , Matplotlib and Seaborn.

Run the following command in the root directory.

Clone the repository

```git clone https://github.com/kamathhrishi/PyReData.git```

Change directory

```cd PyReData```

Run Installation script

``` python setup.py install```

Bonus: Run testcases

``` sh test.sh ```

<h3>To Do:</h3>

Aim to reduce effort from turning data science to reports or visuals with little effort as possible.

Complete PIMA Diabetes Example showing an

* Tabsets
* Modal
* Templating
* Instant plots

Priority

High
* Handle Stylesheets
* Name all components
* Style is written to stylesheets
* Write Unit tests

Medium
* Improved API for tables (various bootstrap classes)
* Easy API to go from Dataframes to tables
* Templating
* Generalized Seaborn Matplotlib and pandas plot support
* Automatically name every Node
* Visualize complete tree for debugging
* Make Node iterable
* Handle type errors
* Jupyter Notebook PIMA
* Render output dynamically

Low
* Type Annotations
* Documentation
* Profiling
