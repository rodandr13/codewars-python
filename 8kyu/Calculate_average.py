"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""


def find_average(numbers):
    if numbers:
        return sum(numbers)/len(numbers)
    return 0
