"""
You will be given a sphere with radius(r). Imagine that sphere gets cut with
flat surface, in this case the figure that is made with this cut is circle.
You will also be given distance(h) between centres of sphere and circle.Your
task is to return the area of the original sphere,area of circle and perimeter
of circle, all of them rounded to 3 decimal places and order must be same as
in the description.
"""


from math import pi, sqrt


def stereometry(r,h):
    R = sqrt(r ** 2 - h ** 2)
    return (
        round(4 * pi * r ** 2, 3),
        round(pi * R ** 2, 3),
        round(2 * pi * R, 3)
    )


assert stereometry(2,1) == (50.265, 9.425, 10.883)
assert stereometry(3,2) == (113.097, 15.708, 14.05)
assert stereometry(4,3) == (201.062, 21.991, 16.624)

