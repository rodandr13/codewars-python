"""
You are given two arrays arr1 and arr2, where arr2 always contains integers.
For arr1 = ['a', 'a', 'a', 'a', 'a'], arr2 = [2, 4]
find_array returns ['a', 'a']
For arr1 = [0, 1, 5, 2, 1, 8, 9, 1, 5], arr2 = [1, 4, 7]
find_array returns [1, 1, 1]
"""


def find_array(arr1, arr2):
    return [arr1[i] for i in arr2 if i < len(arr1)]


assert find_array(['a', 'a', 'a', 'a', 'a'], [2, 4]) == ['a', 'a']
assert find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7]) == [1, 1, 1]
