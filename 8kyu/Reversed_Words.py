"""
Complete the solution so that it reverses all of the words within
the string passed in.
"""


def reverse_words(s):
    return " ".join(s.split()[::-1])
