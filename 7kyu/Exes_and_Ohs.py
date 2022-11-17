"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.
"""


def xo(s):
    return s.lower().count('x') == s.lower().count('o')
