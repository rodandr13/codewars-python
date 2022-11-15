"""
Return a new array consisting of elements which are multiple of their own
index in input array (length > 1).
"""


def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
