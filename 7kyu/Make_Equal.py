"""
Given an array of integers a and integers t and x, count how many elements
in the array you can make equal to t by increasing / decreasing it by
x (or doing nothing). EASY!

# ex 1

a = [11, 5, 3]
t = 7
x = 2

count(a, t, x) # => 3
you can make 11 equal to 7 by subtracting 2 twice
you can make 5 equal to 7 by adding 2
you can make 3 equal to 7 by adding 2 twice
"""


def count(a, t, x):
    if x == 0:
        return len([num for num in a if x == 0 and num == t])
    return len([num for num in a if (num - t) % x == 0])
