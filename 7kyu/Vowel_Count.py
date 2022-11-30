"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
"""
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
"""
"""
def getCount(s):
    return sum(c in 'aeiou' for c in s)
"""


def get_count(sentence):
    chars = "aeiou"
    counter = 0
    for char in sentence:
        if char in chars:
            counter += 1
    return counter
