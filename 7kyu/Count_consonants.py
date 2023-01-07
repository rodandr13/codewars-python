"""
Write a function consonantCount, consonant_count or ConsonantCount
that takes a string of English-language text and returns the number
of consonants in the string.

Consonants are all letters used to write English excluding
the vowels a, e, i, o, u.
"""


def consonant_count(s):
    count = 0
    consonants = "bcdfghjklmnpqrstvwxyz"
    for x in s:
        if x.lower() in consonants:
            count +=1
    return count
