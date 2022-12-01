"""
Some people just have a first name; some people have first and last names and
some people have first, middle and last names.

You task is to initialize the middle names (if there is any).
"""
"""
def initializeNames(name):
    names = name.split()
    names[1:-1] = map(lambda n: n[0] + '.', names[1:-1])
    return ' '.join(names)
"""


def initialize_names(name):
    names = name.split()
    result = ""
    if len(names) <= 2:
        return " ".join(names)
    for i in range(1, len(names) - 1):
        result += names[i][:1] + ". "
    result = f"{names[0]} {result}{names[-1]}"
    return result
