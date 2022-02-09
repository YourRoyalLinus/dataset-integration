from _collections_abc import Sequence
from itertools import count
from numpy import genfromtxt, ndarray
from file import datafile

def load_file(file: 'datafile.DataFile', columns : Sequence,
            fill_missing=None) -> ndarray:
        """Return a 2D numpy.ndarray of the interval and data columns from the
        DataFile

        Positional Arguments:
            file: DataFile object
            columns: Tuple of ints to determine which two columns to extract 
                    from the file (interval, data). Invalid interval columns 
                    will be converted to incremented integers. Invalid data 
                    values are the responsibility of the user.
        Keyword Arguemnts:
            fill_missing -- value to substitute for missing values in the 
            dataset (default = None) 
        """
        skip_h = 1 if file.has_headers else 0
        iter_count = count(0, 1)
        
        def valid_x_value(x):
            value = x
            try:
               value = float(x)
            except (ValueError, TypeError):
                value = iter_count.__next__()
                
            return 0 if value is None else value

        converter = {columns[0]: valid_x_value}
        return genfromtxt(file.path, delimiter=file.delimeter,
                        usecols=columns, skip_header=skip_h,
                        converters=converter, unpack=True,
                        filling_values=fill_missing)

