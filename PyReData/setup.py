import os

from setuptools import find_packages
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = read("requirements.txt").split()

setup(
    name="PyReData",
    version="0.1",
    author="Hrishikesh Kamath",
    author_email="kamathhrishi@gmail.com",
    description=(
        "Allows to share analysis and visualizations done using Python as HTML web pages. "
    ),
    license="Apache-2.0",
    keywords="Data visualizations Data analysis",
    packages=find_packages(exclude=["examples"]),
    include_package_data=True,
    url="https://github.com/OpenMined/PySyft",
    install_requires=requirements,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-flake8"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
