"""
I created this function to add five to any number that was passed in to it and return the new value.
It doesn't throw any errors, but it returns the wrong number.
"""


def add_five(num):
    return num + 5


assert add_five(5) == 10
assert add_five(0) == 5
assert add_five(-5) == 0