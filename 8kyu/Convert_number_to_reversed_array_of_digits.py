"""
Given a random non-negative number, you have to return the digits of this
number within an array in reverse order.
"""

"""
def digitize(n):
    list_numbers = [int(number) for number in str(n)]
    list_numbers.reverse()
    return list_numbers
"""


def digitize(n):
    return map(int, str(n)[::-1])
