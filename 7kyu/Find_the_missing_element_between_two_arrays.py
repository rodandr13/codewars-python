"""
Given two integer arrays where the second array is a shuffled duplicate
of the first array with one element missing, find the missing element.

Please note, there may be duplicates in the arrays, so checking if a numerical
value exists in one and not the other is not a valid solution.
"""


def find_missing(arr1, arr2):
    """
    if not arr2:
        return arr1[0]
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1) - 1):
        if arr1[i] != arr2[i]:
            return arr1[i]
    return arr1[-1]
    """
    for char in arr1:
        if arr1.count(char) != arr2.count(char):
            return char


assert find_missing([1, 2, 3], [1, 3]) == 2
assert find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]) == 8
assert find_missing([7], []) == 7
