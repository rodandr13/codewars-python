"""
Your task, is to create NxN multiplication table, of size provided in parameter.
for example, when given size is 3:
1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
"""


def multiplication_table(size):
    result = [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]
    return result


assert multiplication_table(3) == [[1,2,3],[2,4,6],[3,6,9]]
