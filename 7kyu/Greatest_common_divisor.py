"""
Find the greatest common divisor of two positive integers.
The integers can be large, so you need to find a clever solution.

The inputs x and y are always greater or equal to 1, so the greatest common
divisor will always be an integer that is also greater or equal to 1.
"""


def mygcd(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


assert mygcd(30,12) == 6
assert mygcd(8,9) == 1
assert mygcd(1,1) == 1
