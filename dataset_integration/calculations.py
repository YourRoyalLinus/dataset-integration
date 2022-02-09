from _collections_abc import Sequence
from numpy import ndarray
from scipy.integrate import cumulative_trapezoid


def strictly_increasing(s: Sequence):
    """Returns true if sequence s is monotonically increasing"""
    return all(x < y for x, y in zip(s, s[1:]))

def strictly_decreasing(s: Sequence):
    """Returns true if sequence s is monotonically decreasing"""
    return all(x > y for x, y in zip(s, s[1:]))

def is_monotonic(values :Sequence) -> bool:
    """Returns true if the values sequence is monotonically increasing or 
        monotonically decreasing
    """
    if not (strictly_increasing(values) or strictly_decreasing(values)):
        return False
    else:
        return True

def integrate(x : Sequence, y: Sequence) -> ndarray:
    """Return an ndarray as the result of cumulative integration of y along the 
    axis using the composite trapezoidal rule. 

    Positional Arguments:
        x : Sequence
            - values to represent the interval over which you're
                integrating

        y : Sequence
            - values to integrate
    """
    return cumulative_trapezoid(y,x, initial=0)
