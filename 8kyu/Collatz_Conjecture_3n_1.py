"""
The Collatz conjecture (also known as 3n+1 conjecture) is a conjecture that applying the following algorithm to any number we will always eventually reach one:

[This is writen in pseudocode]
if(number is even) number = number / 2
if(number is odd) number = 3*number + 1
"""


def hotpo(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
    return count
