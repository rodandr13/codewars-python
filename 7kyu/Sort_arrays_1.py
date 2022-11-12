"""
Just a simple sorting usage. Create a function that returns the elements of
the input-array / list sorted in lexicographical order.
"""


def sortme(names):
    return sorted(names)


assert sortme(["one", "two", "three"]) == ["one", "three", "two"]
