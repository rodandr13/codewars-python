"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    result = []
    zeros = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zeros.append(lst[i])
        else:
            result.append(lst[i])
    result.extend(zeros)
    return result


call = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
result = [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert move_zeros(call) == result
