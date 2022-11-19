"""
Your job is to return the volume of a cup when given the diameter of the top,
the diameter of the bottom and the height.

You know that there is a steady gradient from the top to the bottom.

You want to return the volume rounded to 2 decimal places.
"""


from math import pi


def cup_volume(d1, d2, height):
    return round((pi * height) / 12 * (d1 ** 2 + d1 * d2 + d2 ** 2), 2)
