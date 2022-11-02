import copy


def reverse_on_diagonals(matrix):
    result = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        result[i][i] = matrix[-i-1][-i-1]
        result[i][-i-1] = matrix[-i-1][i]

    return result


matrix_1_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_1_out = [[9, 2, 7], [4, 5, 6], [3, 8, 1]]
matrix_2_in = [[[239]]]
matrix_2_out = [[[239]]]
matrix_3_in = [[1, 10], [100, 1000]]
matrix_3_out = [[1000, 100], [10, 1]]

assert reverse_on_diagonals(matrix_1_in) == matrix_1_out
assert reverse_on_diagonals(matrix_2_in) == matrix_2_out
assert reverse_on_diagonals(matrix_3_in) == matrix_3_out
