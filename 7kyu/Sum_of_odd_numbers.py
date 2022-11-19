"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting
at index 1) e.g.: (Input --> Output)
"""


def row_sum_odd_numbers(n):
    return n * n * n


assert row_sum_odd_numbers(1) == 1
assert row_sum_odd_numbers(2) == 8
assert row_sum_odd_numbers(13) == 2197
