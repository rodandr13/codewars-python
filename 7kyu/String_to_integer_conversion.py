"""
It can be used like this:

parseInt("10") returns 10
parseInt("10 apples") also returns 10
We would like it to return "NaN" (as a string) for the second case because
the input string is not a valid number.
"""
"""
def my_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return 'NaN'
"""


def my_parse_int(string):
    string = string.strip()
    if string.isnumeric():
        return int(string)
    return "NaN"
