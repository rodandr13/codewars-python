"""
Define a function that removes duplicates from an array of numbers
and returns it as a result.

The order of the sequence has to stay the same.
"""


def distinct(seq):
    result = []
    for char in seq:
        if char not in result:
            result.append(char)
    return result
