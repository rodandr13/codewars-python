"""
The method is supposed to remove even numbers from the list and return
a list that contains the odd numbers.

However, there is a bug in the method that needs to be resolved.
"""


def kata_13_december(lst):
    return [lst[x] for x in range(len(lst)) if lst[x] % 2 != 0]
