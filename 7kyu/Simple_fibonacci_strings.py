"""
f0 = '0'
f1 = '01'
f2 = '010' = f1 + f0
f3 = '01001' = f2 + f1
You will be given a number and your task is to return the nth fibonacci string.
For example:
solve(2) = '010'
solve(3) = '01001'
"""
"""
def solve(n):
    a,b = '01'
    for _ in range(n): a,b = a+b,a
    return a
"""

fib = {}


def solve(n):
    if n in fib:
        return fib[n]
    else:
        if n == 0:
            value = '0'
        elif n == 1:
            value = '01'
        else:
            value = solve(n - 1) + solve(n - 2)
            fib[n] = value
    return value
