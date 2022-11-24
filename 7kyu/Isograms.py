"""
An isogram is a word that has no repeating letters, consecutive or
non-consecutive. Implement a function that determines whether a string
that contains only letters is an isogram. Assume the empty string is an
isogram. Ignore letter case.
"""
"""
def is_isogram(string):
    return len(string) == len(set(string.lower()))
"""


def is_isogram(string):
    return len(set(list(string.lower()))) == len(string)


assert is_isogram("Dermatoglyphics") == True
assert is_isogram("isogram") == True
assert is_isogram("aba") == False
