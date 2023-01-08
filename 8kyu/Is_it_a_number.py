"""
Given a string s, write a method (function) that will return true if its a
valid single integer or floating number or false if its not.
"""


def isDigit(string):
    string = string.replace(".", "")
    return string.isdigit() or string.startswith("-")
