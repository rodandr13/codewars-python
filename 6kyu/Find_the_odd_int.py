"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
"""
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""


def find_it(seq):
    keys = []
    values = []
    for num in seq:
        if num in keys:
            values[keys.index(num)] += 1
        else:
            keys.append(num)
            values.append(1)
    for i in range(len(keys)):
        if values[i] % 2 != 0:
            return keys[i]
    return None


assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
assert find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) == -1
