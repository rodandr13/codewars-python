"""
In this exercise, you will create a function that takes an integer,
i. With it you must do the following:

Find all of its multiples up to and including 100,

Then take the digit sum of each multiple (eg. 45 -> 4 + 5 = 9),

And finally, get the total sum of each new digit sum.

Note: If the digit sum of a number is more than 9 (eg. 99 -> 9 + 9 = 18)
then you do NOT have to break it down further until it reaches one digit.
"""
"""
def procedure(n):
    return sum(int(d) for i in range(n, 101, n) for d in str(i))
"""


def procedure(i):
    return sum([sum(map(int, list(str(x)))) for x in range(101) if x % i == 0])


assert procedure(30) == 18
assert procedure(12) == 72
