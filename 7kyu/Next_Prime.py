"""

Get the next prime number!

You will get a numbern (>= 0) and your task is to find the next prime number.

Make sure to optimize your code: there will numbers tested up to about 10^12.
"""
"""
ver2
from gmpy2 import next_prime
"""
"""
ver3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n
"""

import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def next_prime(n):
    if n <= 1:
        return 2
    prime = n
    found = False
    while not found:
        prime = prime + 1
        if is_prime(prime):
            found = True
    return prime
