"""
I have four positive integers, A, B, C and D, where A < B < C < D. The input
is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order.
Your task is to return the value of D.
"""


def alphabet(ns):
    a, b, c1, c2, _, _, _, cd = sorted(ns)
    return cd / c2 if a * b == c1 else cd / c1
