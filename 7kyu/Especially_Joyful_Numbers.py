"""
Positive integers that are divisible exactly by the sum of their digits are
called Harshad numbers. The first few Harshad numbers are:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, ...

We are interested in Harshad numbers where the product of its digit sum s and
s with the digits reversed, gives the original number n.
"""


def number_joy(n):
    numbers = [int(i) for i in str(n)]
    num_sum = sum(numbers)
    num_sum_reverse = int(str(num_sum)[::-1])
    return num_sum * num_sum_reverse == n


assert number_joy(1997) == False
assert number_joy(1998) == False
assert number_joy(1729) == True