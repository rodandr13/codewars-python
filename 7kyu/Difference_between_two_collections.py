"""
Find the difference between two collections. The difference means that
either the character is present in one collection or it is present in other,
but not in both. Return a sorted list with the difference.
The collections can contain any character and can contain duplicates.
"""

"""
def diff(a, b):
    if not a:
        return b
    elif not b:
        return a
    a = set(a)
    b = set(b)
    return sorted(list(a ^ b))
"""


def diff(a, b):
    return sorted(set(a).symmetric_difference(b))

