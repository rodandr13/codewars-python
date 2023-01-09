"""
In this Kata, you will be given an integer array and your task is to return
the sum of elements occupying prime-numbered indices.

The first element of the array is at index 0.

Good luck!
"""


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def total(arr):
    result = 0
    if not arr:
        return 0
    for i in range(2, len(arr)):
        if is_prime(i):
            print(i)
            result += arr[i]
    return result

