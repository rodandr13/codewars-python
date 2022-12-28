from functools import reduce


def grow(arr):
    return reduce(lambda a, b: a * b, arr)
