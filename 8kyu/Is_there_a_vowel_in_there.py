"""
Given an array of numbers, check if any of the numbers are the character
codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array.
"""


def is_vow(inp):
    result = []
    vowels = "aeiou"
    for x in inp:
        result.append(chr(x) if chr(x) in vowels else x)
    return result
