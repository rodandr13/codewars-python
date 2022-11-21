"""
We need a function prime_bef_aft() that gives the largest prime below a
certain given value n,

befPrime or bef_prime (depending on the language),

and the smallest prime larger than this value,

aftPrime/aft_prime (depending on the language).
"""
"""
from gmpy2 import is_prime, next_prime

def prime_bef_aft(num):
    return [next(filter(is_prime, range(num-1, 1, -1))), next_prime(num)]
"""


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def prime_bef_aft(num):
    befPrime = None
    aftPrime = None
    forward = num
    back = num

    while (True):
        if not befPrime:
            back -= 1
            if is_prime(back):
                befPrime = back
                break

    while (True):
        if not aftPrime:
            forward += 1
            if is_prime(forward):
                aftPrime = forward
                break

    return [befPrime, aftPrime]


assert prime_bef_aft(100) == [97, 101]
assert prime_bef_aft(97) == [89, 101]
assert prime_bef_aft(101) == [97, 103]
