from functools import reduce
"""
def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product
"""


def grow(arr):
    return reduce(lambda a, b: a * b, arr)
