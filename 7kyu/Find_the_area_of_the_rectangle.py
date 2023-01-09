"""
Find the area of a rectangle when provided with one diagonal and one side of
the rectangle. If the input diagonal is less than or equal to the length of
the side, return "Not a rectangle". If the resultant area has decimals round
it to two places.
"""


from math import sqrt


def area(d, l):
    if d <= l: return "Not a rectangle"
    return round(l * sqrt(d ** 2 - l ** 2), 2)
