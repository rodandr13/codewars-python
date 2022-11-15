"""
Create a function that returns the CSV representation of a two-dimensional
numeric array.
"""


def to_csv_text(array):
    result = []
    for i in range(len(array)):
        result.append(','.join(map(str, array[i])))
    result = '\n'.join(result)
    return result
