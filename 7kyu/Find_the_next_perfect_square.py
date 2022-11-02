"""
You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square then -1 should be returned.
You may assume the parameter is non-negative.
"""


def find_next_square(sq):
    num_sqrt = sq ** 0.5
    if num_sqrt % 1 == 0:
        return (round(num_sqrt) + 1) ** 2
    return -1


assert find_next_square(121) == 144
assert find_next_square(625) == 676
assert find_next_square(319225) == 320356