"""
Make the 2D list by the sequential integers started by the head number.
See the example test cases for the expected output.
"""


def make_2d_list(head, row, col):
    """
    result = []
    count = head
    for r in range(row):
        result.append([])
        for c in range(col):
            result[r].append(count)
            count += 1
    """
    result = [[head + r * col + c for c in range(col)] for r in range(row)]

    return result


assert make_2d_list(1,2,3) == [[1, 2, 3], [4, 5, 6]]
assert make_2d_list(2,3,4) == [[2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13]]
assert make_2d_list(5,6,1) == [[5], [6], [7], [8], [9], [10]]
