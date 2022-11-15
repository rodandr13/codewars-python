"""
Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.
"""


def invert(lst):
    return [x * -1 for x in lst]
