#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py
"""Install script for this package."""

import os
from setuptools import setup, find_packages
from aversio import Version, get_git_version, maintain_version

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
#def read(fname):
#    return open(os.path.join(os.path.dirname(__file__), fname)).read()

VERSION = maintain_version(str(Version(get_git_version()[1:])), "VERSION")

# Also store the version to be seen from the code
with open("./aversio/version.py", "w") as file:
    file.write("__version__ = '%s'" % VERSION)


setup(
    name = "aversio",
    version = VERSION,
    author = "Jaroslav Klapálek",
    author_email = "klapajar@fel.cvut.cz",
    description = ("Automatic versioning tool for Python."),
    license = "GPLv3",
    keywords = "version Python git automatic",
    #url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    #long_description=read('README'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
    ],
)
