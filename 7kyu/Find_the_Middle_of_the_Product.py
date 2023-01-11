"""
Given a string of characters, I want the function findMiddle()/find_middle()
to return the middle number in the product of each digit in the string.

Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as
an integer.

Not all strings will contain digits. In this case and the case for any
non-strings, return -1.

If the product has an even number of digits, return the middle two digits

Example: 1563 -> 56

NOTE: Remove leading zeros if product is even and the first digit of the two
is a zero. Example 2016 -> 1
"""


import functools


def find_middle(string):
    if not isinstance(string, str) or not string:
        return -1
    numbers = [int(x) for x in string if x.isdigit()]
    if not numbers:
        return -1
    total = str(functools.reduce(lambda a, b : a * b, numbers))
    print(total)
    if len(total) % 2 != 0:
        return int(list(total)[len(total) // 2])
    return int(total[len(total) // 2 - 1: len(total) // 2 + 1])
