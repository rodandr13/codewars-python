"""
Your task is to return the sum of Triangular Numbers up-to-and-including
the nth Triangular Number.

Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.)
obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."
"""


def sum_triangular_numbers(n):
    result = []
    counter = 0
    for i in range(1, n + 1):
        result.append(0.5 * i * (i+1))
    return sum(result)
