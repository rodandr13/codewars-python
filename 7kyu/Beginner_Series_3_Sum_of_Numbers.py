"""
Given two integers a and b, which can be positive or negative, find the sum of
all the integers between and including them and return it. If the two numbers
are equal return a or b.
"""


def get_sum(a,b):
    return sum(range(a, b + 1)) if a < b else sum(range(b, a + 1))
