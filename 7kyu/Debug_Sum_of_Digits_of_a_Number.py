"""
Debug   function getSumOfDigits that takes positive integer to calculate sum
of it's digits. Assume that argument is an integer.
"""


def get_sum_of_digits(num):
    digits = list(map(int, str(num)))
    return sum(digits)
