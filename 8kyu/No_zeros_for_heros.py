"""
Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
"""
"""
def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n
"""


def no_boring_zeros(n):
    if n == 0:
        return n
    result = n
    while result % 10 == 0:
        result //= 10
    return result
