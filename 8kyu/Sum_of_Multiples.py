"""
Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples
"""


def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return "INVALID"
    return sum([x for x in range(n, m) if x % n == 0])
