"""
Note: anagrams are case insensitive
Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
"""


def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


assert is_anagram("foefet", "toffee") == True
assert is_anagram("Buckethead", "DeathCubeK") == True
assert is_anagram("apple", "pale") == False
