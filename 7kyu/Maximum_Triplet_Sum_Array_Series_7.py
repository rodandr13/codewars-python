"""
Given an array/list [] of n integers , find maximum triplet sum in the array
Without duplications.

1- maxTriSum ({3,2,6,8,2,3}) ==> return (17)
"""
"""
def max_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])
"""


def max_tri_sum(numbers):
    numbers.sort()
    result = sorted(set(numbers))[-3:]
    return sum(result)
