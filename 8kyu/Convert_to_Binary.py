"""
Given a non-negative integer n, write a function to_binary/ToBinary which
returns that number in a binary format.
"""


def to_binary(n):
    return int(str(bin(n)).lstrip('08b'))
