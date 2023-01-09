"""
Write a function

alternate_sort(l)
that combines the elements of an array by sorting the elements ascending by
their absolute value and outputs negative and non-negative integers
alternatingly (starting with the negative value, if any).

E.g.

alternate_sort([5, -42, 2, -3, -4, 8, -9,]) == [-3, 2, -4, 5, -9, 8, -42]
alternate_sort([5, -42, 2, -3, -4, 8, 9]) == [-3, 2, -4, 5, -42, 8, 9]
alternate_sort([5, 2, -3, -4, 8, -9]) == [-3, 2, -4, 5, -9, 8]
alternate_sort([5, 2, 9, 3, 8, 4]) == [2, 3, 4, 5, 8, 9]
"""


def alternate_sort(l):
    non_negative = []
    negative = []
    result = []
    for num in l:
        if num >= 0:
            non_negative.append(num)
        else:
            negative.append(num)
    negative.sort(reverse=True)
    non_negative.sort()
    for i in range(max(len(negative), len(non_negative))):
        if i < len(negative):
            result.append(negative[i])
        if i < len(non_negative):
            result.append(non_negative[i])
    return result
