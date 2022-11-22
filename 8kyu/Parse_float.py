"""
Write function parse_float which takes a string/list and returns a number
or 'none' if conversion is not possible.
"""
"""
def parse_float(string):
    try:
        return float(string)
    except:
        return None
"""


def parse_float(string):
    if isinstance(string, list):
        return None
    return float(string) if string[0].isdigit() else None
