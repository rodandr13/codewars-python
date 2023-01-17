"""
Fix the Bugs (Syntax) - My First Kata
Overview
Hello, this is my first Kata so forgive me if it is of poor quality.

In this Kata you should fix/create a program that returns the following values:

false/False if either a or b (or both) are not numbers
a % b plus b % a if both arguments are numbers
You may assume the following:

If a and b are both numbers, neither of a or b will be 0.
"""


def my_first_kata(a, b):
    if (not isinstance(a, int)
            or not isinstance(b, int)
            and not isinstance(a, bool)):
        return False
    else:
        return a % b + b % a
