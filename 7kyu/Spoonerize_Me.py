"""
A spoonerism is a spoken phrase in which the first letters of two of the
words are swapped around, often with amusing results.

In its most basic form a spoonerism is a two word phrase in which only the
first letters of each word are swapped:

"not picking" --> "pot nicking"
"""

"""
def spoonerize(words):
    words = words.split()
    return words[1][:1] + words[0][1:] + " " + words[0][:1] + words[1][1:]
"""


def spoonerize(words):
    a, b = words.split()
    return f"{b[0]}{a[1:]} {a[0]}{b[1:]}"


assert spoonerize("nit picking") == "pit nicking"
assert spoonerize("wedding bells") == "bedding wells"
assert spoonerize("jelly beans") == "belly jeans"
