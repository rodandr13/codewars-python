"""
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings.
Each match is represented by a string in the format "x:y", where x is our
team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]
"""


def points(games):
    total = 0
    for s in games:
        command1, command2 = s.split(':')
        total += 3 if int(command1) > int(command2) else 0
        total += 1 if int(command1) == int(command2) else 0

    return total
