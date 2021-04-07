import typing

from typing import List


def is_valid(matrix: List[List[int]]) -> bool:
    # check matrix has 9 rows
    if len(matrix) != 9:
        return False
    for row in range(9):
        # check matrix has 9 columns
        if len(matrix[row]) != 9:
            return False
        for col in range(9):
            # check all numbers are between 0 and 9
            if matrix[row][col] < 0 or matrix[row][col] > 9:
                return False
            # check validity of the number only if it is != 0
            if matrix[row][col] != 0:
                for i in range(9):
                    # check no equal number on the same row
                    if i != col and matrix[row][i] == matrix[row][col]:
                        return False
                    # check no equal number on the same column
                    if i != row and matrix[i][col] == matrix[row][col]:
                        return False
                # TODO: check no equal number in the same block

    return True


def pretty_print(matrix: List[List[int]]):
    to_print = ""
    for row in range(9):
        for col in range(9):
            to_print += str(matrix[row][col]) + "  "
        to_print += "\n"
    print(to_print)


if __name__ == '__main__':
    input_matrix = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]
    print(f"Input matrix:")
    pretty_print(input_matrix)
    print(f"Valid: {is_valid(input_matrix)}")
