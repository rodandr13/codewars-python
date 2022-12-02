"""
An element in an array is dominant if it is greater than all elements to its
right. You will be given an array and your task will be to return a list of
all dominant elements. For example
"""


def solve(arr):
    result = []
    for i in range(len(arr) - 1):
        if arr[i] > max(arr[i+1:]):
            result.append(arr[i])
    result.append(arr[-1])
    return result
