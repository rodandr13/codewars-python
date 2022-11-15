"""
Complete the function that takes a non-negative integer n as input, and
returns a list of all the powers of 2 with the exponent ranging from 0 to n
( inclusive ).
"""


def powers_of_two(n):
    return [2 ** x for x in range(n+1)]

