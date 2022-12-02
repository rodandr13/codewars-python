"""
Find out "B"(Bug) in a lot of "A"(Apple).

There will always be one bug in apple, not need to consider the situation
that without bug or more than one bugs.

input: string Array apple

output: Location of "B", [x,y]
"""


def sc(apple):
    for i in range(len(apple)):
        if "B" in apple[i]:
            return [i, apple[i].index("B")]
