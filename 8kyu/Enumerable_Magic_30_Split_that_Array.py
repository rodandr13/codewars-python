"""
Create a method partition that accepts a list and a method/block.
It should return two arrays: the first, with all the elements for
which the given block returned true, and the second for the remaining elements.
"""


def partition(arr, classifier_method):
    return ([x for x in arr if classifier_method(x)],
           [x for x in arr if not classifier_method(x)])
