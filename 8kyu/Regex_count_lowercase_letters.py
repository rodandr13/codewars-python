"""
Your task is simply to count the total number of lowercase letters in a string.
"""

"""
def lowercase_count(strng):
    count = 0
    for char in strng:
        if char.islower():
            count += 1
    return count
"""


def lowercase_count(strng):
    return sum(a.islower() for a in strng)


assert lowercase_count("abc") == 3
assert  lowercase_count("abcABC123") == 3
assert lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 3