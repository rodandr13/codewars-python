"""
Create a function called shortcut to remove the lowercase vowels
(a, e, i, o, u ) in a given string.
"""


def shortcut( s ):
    chars = 'aeiou'
    result = [x for x in s if x not in chars]
    return ''.join(result)
