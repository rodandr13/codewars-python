"""
Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool
and Crash Override are some notable examples from the film Hackers.

Your task is to create a function that, given a proper first and last name,
will return the correct alias.
"""


def alias_gen(f_name, l_name):
    first = FIRST_NAME.get(f_name[0].upper())
    last = SURNAME.get(l_name[0].upper())
    return '{} {}'.format(first, last) if first and last else \
        'Your name must start with a letter from A - Z.'