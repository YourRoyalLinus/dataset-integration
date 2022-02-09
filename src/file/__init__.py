"""Package for objects to represent data files in Python

Classes:
    datafile.DataFile
        - class to represent a file
Subpackages:
    manage
"""

from . import manage
from . import datafile

__all__ = ["datafile", "manage"]