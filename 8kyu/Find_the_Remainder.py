"""
Write a function that accepts two integers and returns the remainder
of dividing the larger value by the smaller value.

Division by zero should return an empty value.
"""


def remainder(a, b):
    return max(a, b) % min(a, b) if min(a, b) != 0 else None
