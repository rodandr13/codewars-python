"""
number	price (cents)
n < 5	100
n >= 5 and n < 10	95
n >= 10	90
"""


def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif 5 <= n < 10:
        return n * 95
    return n * 90
