"""
Given an array of 3 non-negative integers a, b and c,
determine if they form a pythagorean triple.

A pythagorean triple is formed when:

c2 = a2 + b2
where c is the largest value of a, b, c.

For example: a = 3, b = 4, c = 5 forms a pythagorean triple,
because 52 = 32 + 42
"""
"""
def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a * a + b * b == c * c
"""


def pythagorean_triple(integers):
    integers.sort()
    return integers[-1] ** 2 == integers[0] ** 2 + integers[1] ** 2


assert pythagorean_triple([3, 4, 5]) == True
assert pythagorean_triple([3, 5, 9]) == False
