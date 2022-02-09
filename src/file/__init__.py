"""Package for objects to represent data files in Python

Classes:
    datafile.DataFile
        - class to represent a file
Modules:
    load
        - contains functions to load the datafile into new data structures
"""

from . import datafile
from . import load

__all__ = ["datafile", "load"]