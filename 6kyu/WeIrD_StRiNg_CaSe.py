"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
and returns the same string with all even indexed characters in each word
upper cased, and all odd indexed characters in each word lower cased.
The indexing just explained is zero based, so the zero-ith index is even,
therefore that character should be upper cased and you need to start over
for each word.

The passed in string will only consist of alphabetical characters and
spaces(' '). Spaces will only be present if there are multiple words.
Words will be separated by a single space(' ').
"""
"""
def to_weird_case(words):
    result = ""
    words_list = words.split()
    for i in range(len(words_list)):
        chars = list(words_list[i])
        for j in range(len(chars)):
            if j % 2 == 0:
                result += chars[j].upper()
            else:
                result += chars[j].lower()
        result += " "
    return result.strip()
"""


def to_weird_case(words):
    result = ""
    words_list = words.split()
    for i in range(len(words_list)):
        chars = list(words_list[i])
        for j in range(len(chars)):
            if j % 2 == 0:
                result += chars[j].upper()
            else:
                result += chars[j].lower()
    return result
