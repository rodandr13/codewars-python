"""
Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool
and Crash Override are some notable examples from the film Hackers.

Your task is to create a function that, given a proper first and last name,
will return the correct alias.
"""


import re


FIRST_NAME = {
    "C": "Cache",
    "R": "RAD",
    "J": "Java",
    "B": "Beta",
    "H": "Half-life",
    "L": "Logic",
    "O": "OS",
    "Y": "Y",
    "Q": "Quantum",
    "T": "Trojan",
    "S": "Strike",
    "M": "Malware",
    "E": "Energy",
    "F": "Function",
    "A": "Alpha",
    "K": "Keystroke",
    "I": "Ice",
    "W": "WiFi",
    "N": "Nagware",
    "Z": "Zero",
    "D": "Data",
    "G": "Glitch",
    "V": "Vanilla",
    "X": "Xerox",
    "P": "Phishing",
    "U": "Ultraviolet",
}

SURNAME = {
    "E": "Electron",
    "Q": "Quark",
    "Z": "Zombie",
    "C": "Catalyst",
    "S": "Spy",
    "O": "Overclock",
    "X": "X",
    "D": "Discharge",
    "M": "Mike",
    "P": "Payload",
    "G": "Gig",
    "K": "Killer",
    "R": "Roy",
    "B": "Bomb",
    "H": "Hacker",
    "Y": "Yob",
    "I": "IP",
    "F": "Faraday",
    "A": "Analogue",
    "W": "Worm",
    "U": "Unit",
    "L": "Lazer",
    "T": "T-Rex",
    "V": "Virus",
    "N": "n00b",
    "J": "Jabber",
}

def alias_gen(f_name, l_name):
    regex = r'^[a-zA-Z]+'
    if re.match(regex, f_name) and re.match(regex, l_name):
        return '{} {}'.format(FIRST_NAME[f_name[0].upper()], SURNAME[l_name[0].upper()])
    else:
        return 'Your name must start with a letter from A - Z.'