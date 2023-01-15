"""
Task:
You need to write a function grid that returns an alphabetical grid of size
NxN, where a = 0, b = 1, c = 2....

Examples:
grid(4)

a b c d
b c d e
c d e f
d e f g
"""


from string import ascii_lowercase


def grid(N):
    if N < 0:
        return None
    result = []
    for i in range(N):
        result.append(' '.join(list(ascii_lowercase[i:N+i])))
    return '\n'.join(result)