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

<h1>To Do:</h1>

Aim to reduce effort from turning data science to reports or visuals with little effort as possible.

Complete PIMA Diabetes Example showing an

* Tabsets
* Modal
* Templating
* Instant plots

Priority

Current

* More generalized naming standard
* Allow single/multiple naming of classes/id easily
* Add test for widgets with stylesheet support

High

* Name all components
* Write Unit tests


Kinda cool

A bash program to automatically run tests , black formatter , code coverage, documentation coverage and push to Github
Maybe even automatically generate unit tests based on examples?

Medium

* Cache pages and results for faster rendering
* Improved API for tables (various bootstrap classes)
* Easy API to go from Dataframes to tables
* Templating
* Generalized Seaborn Matplotlib and pandas plot support
* Visualize complete tree for debugging
* Make Node iterable
* Handle type errors
* Jupyter Notebook PIMA

Low
* Type Annotations
* Documentation
* Profiling
