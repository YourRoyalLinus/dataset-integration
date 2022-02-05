import csv
from _collections_abc import Sequence
from itertools import count
from numpy import genfromtxt, ndarray
from DataFile import datafile

def examine_file(file: 'datafile.DataFile') -> tuple:
    first_n_bytes = 1024
    sniffer = csv.Sniffer()

    with open(file.path, 'r') as f:
        sample = f.read(first_n_bytes)


    return (sniffer.sniff(sample).delimiter, sniffer.has_header(sample))


def load_file(file: 'datafile.DataFile', columns : Sequence,
            fill_missing=None) -> ndarray:

        skip_h = 1 if file.has_headers else 0
        iter_count = count(0, 1)
        
        def valid_x_value(x):
            if not str(x).isnumeric():
                return iter_count.__next__()
            else:
                return 0 if x is None else x

        converter = {0: valid_x_value}
        return genfromtxt(file.path, delimiter=file.delimeter,
                        usecols=columns, skip_header=skip_h,
                        converters=converter, unpack=True,
                        filling_values=fill_missing)

