"""
In this kata you will be given a sequence of the dimensions of rectangles
(sequence with width and length ) and circles ( radius - just a number ).
Your task is to return a new sequence of dimensions, sorted ascending by area.
"""
"""
def sort_by_area(seq): 
    def func(x):
        if isinstance(x, tuple):
            return x[0] * x[1]
        else:
            return 3.14 * x * x
    return sorted(seq, key=func)
"""

from math import pi


def square1(value):
    if isinstance(value, tuple):
        return value[0] * value[1]
    else:
        return pi * (value ** 2)


def sort_by_area(seq):
    if not seq:
        return []
    result = sorted(seq, key=square1)
    return result
