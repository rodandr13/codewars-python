"""
#Adding values of arrays in a shifted way

You have to write a method, that gets two parameter:

1. An array of arrays with int-numbers
2. The shifting value
#The method should add the values of the arrays to one new array.

The arrays in the array will all have the same size and this size will always
be greater than 0.
The shifting value is always a value from 0 up to the size of the arrays.
There are always arrays in the array, so you do not need to check for null or
empty.

#1. Example:

[[1,2,3,4,5,6], [7,7,7,7,7,-7]], 0

1,2,3,4,5,6
7,7,7,7,7,-7

--> [8,9,10,11,12,-1]
"""
"""
def sum_arrays(arrays, shift):
    shifted = [ [0]*i*shift + a + [0]*(len(arrays)-i-1)*shift  for i, a in enumerate(arrays)]
    return list(map(sum, zip(*shifted)))
"""


def sum_arrays(arrays, shift):
    result = [0] * ((len(arrays) - 1) * shift + len(arrays[0]))
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            result[i * shift + j] += arrays[i][j]
    return result
