"""
The Western Suburbs Croquet Club has two categories of membership, Senior and
Open. They would like your help with an application form that will tell
prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap
greater than 7. In this croquet club, handicaps range from -2 to +26; the
better the player the lower the handicap.
"""


def open_or_senior(data):
    result = []
    for age, handicaps in data:
        if age >= 55 and handicaps > 7:
            result.append("Senior")
        else:
            result.append("Open")

    return result


call =[(45, 12), (55, 21), (19, -2), (104, 20)]
result = ['Open', 'Senior', 'Open', 'Senior']
assert open_or_senior(call) == result


call = [(16, 23), (73, 1), (56, 20), (1, -1)]
result = ['Open', 'Open', 'Senior', 'Open']
assert open_or_senior(call) == result
