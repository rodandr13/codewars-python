"""
Write a function which removes from string all non-digit characters
and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

Function:

getNumberFromString(s)
"""


def get_number_from_string(string):
    return int("".join([x for x in string if x.isdigit()]))
