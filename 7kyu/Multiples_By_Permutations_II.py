"""
We have two consecutive integers k1 and k2, k2 = k1 + 1

We need to calculate the lowest strictly positive integer n, such that:
the values nk1 and nk2 have the same digits but in different order.

E.g.# 1:

k1 = 100
k2 = 101
n = 8919
#Because 8919 * 100 = 891900
and      8919 * 101 = 900819
"""


def find_lowest_int(k):
    n = 1
    while True:
        k1_list = sorted(str(k * n))
        k2_list = sorted(str((k + 1) * n))
        if k1_list == k2_list:
            return n
        n += 1
