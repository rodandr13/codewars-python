"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one
digit, continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.
"""


def digital_root(n):
    result = sum([int(num) for num in str(n)])
    if len(str(result)) >= 2:
        result = digital_root(result)
    return result


assert digital_root(16) == 7
assert digital_root(942) == 6
assert digital_root(132189) == 6
