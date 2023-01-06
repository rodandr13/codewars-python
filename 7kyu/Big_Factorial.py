"""
The factorial of a number, n!, is defined for whole numbers as the product
of all integers from 1 to n.

For example, 5! is 5 * 4 * 3 * 2 * 1 = 120

Most factorial implementations use a recursive function to determine the value
of factorial(n). However, this blows up the stack for large values
of n - most systems cannot handle stack depths much greater than 2000 levels.

Write an implementation to calculate the factorial of arbitrarily large
numbers, without recursion.

Rules
n < 0 should return nil/ None
n = 0 should return 1
n > 0 should return n!
"""


def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
