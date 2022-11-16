"""
Complete the function that returns an array of length n, starting with the
given number x and the squares of the previous number.
If n is negative or zero, return an empty array/list.
"""

"""
def squares(x,n):
    return [x**(2**i) for i in range(n)]
"""


def squares(x, n):
    result = []
    for _ in range(n):
        result += [x]
        x = x ** 2
    return result


assert squares(2, 5) == [2, 4, 16, 256, 65536]
assert squares(3, 3) == [3, 9, 81]
assert squares(5, 3) == [5, 25, 625]