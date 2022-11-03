"""
Find the volume of a cone whose radius and height are provided as parameters to the function volume.
Use the value of PI provided by your language (for example: Math.PI in JS, math.pi in Python
or Math::PI in Ruby) and round down the volume to an Interger.
"""


from math import pi


def volume(r,h):
    return int(0.3333333 * pi * (r ** 2) * h)


assert volume(7,3) == 153
assert volume(56, 30) == 98520
assert volume(0,10) == 0
