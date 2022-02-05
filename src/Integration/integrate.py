from _collections_abc import Sequence
from numpy import ndarray
from scipy.integrate import cumulative_trapezoid

def _strictly_increasing(l: Sequence):
    return all(x < y for x, y in zip(l, l[1:]))

def _strictly_decreasing(l: Sequence):
    return all(x > y for x, y in zip(l, l[1:]))

def is_monotonic(values :Sequence) -> bool:
    if not (_strictly_increasing(values) or _strictly_decreasing(values)):
        return False
    else:
        return True

def integral(x : Sequence, y: Sequence) -> ndarray:
    return cumulative_trapezoid(y,x, initial=0)
