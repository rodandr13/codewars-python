"""
Write a function to convert a name into initials.
This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""
"""
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
"""


def abbrev_name(name):
    name1, name2 = name.title().split()
    return f"{name1[0]}.{name2[0]}"


assert abbrev_name("Sam Harris") == "S.H"
assert abbrev_name("patrick feenan") == "P.F"
assert abbrev_name("Evan C") == "E.C"
