"""
Finish the uefaEuro2016() function so it return string just like in the examples below:
"""


def uefa_euro_2016(teams, scores):
    if scores[0] == scores[1]:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."
    return f"At match {teams[0]} - {teams[1]}, {teams[0] if scores[0] > scores[1] else teams[1] } won!"
