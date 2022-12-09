"""
Given a string, you have to return a string in which each character
(case-sensitive) is repeated once.
"""
"""
def double_char(s):
    return ''.join(c * 2 for c in s)
"""


def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result
