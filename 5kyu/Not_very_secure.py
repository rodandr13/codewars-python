"""
In this example you have to validate if a user input string is alphanumeric.
The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
"""
"""
def alphanumeric(string):
    return string.isalnum()
"""
"""
import re

pattern = re.compile('^[0-9a-zA-Z]+$')

def alphanumeric(string):
  return pattern.match(string) is not None
"""
"""
def alphanumeric(string):
    return bool(re.search(r'^[0-9a-zA-Z]+$', string))
"""

def alphanumeric(password):
    if not password:
        return False
    for char in password:
        if not char.isalpha() and not char.isdigit():
            print(not char.isalpha(), not char.isdigit())
            return False
    return True
