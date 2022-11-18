"""
Given an array of ones and zeroes, convert the equivalent binary value to an
integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
"""


def binary_array_to_number(arr):
    arr = [str(i) for i in arr]
    string = ''.join(arr)
    return int(string, 2)

