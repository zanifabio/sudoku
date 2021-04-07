from typing import List, Optional, Tuple


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
                # check no equal number in the same block
                block_starting_row = int(row / 3) * 3
                block_starting_col = int(col / 3) * 3
                for i in range(block_starting_row, block_starting_row + 3):
                    for j in range(block_starting_col, block_starting_col + 3):
                        if i != row and j != col and matrix[i][j] == matrix[row][col]:
                            return False
    return True


def pretty_print(matrix: List[List[int]]):
    to_print = ""
    for row in range(9):
        for col in range(9):
            to_print += str(matrix[row][col]) + "  "
        to_print += "\n"
    print(to_print)


# def first(matrix: List[List[int]]) -> Optional[Tuple[int, int]]:
#     for row in range(9):
#         for col in range(9):
#             if matrix[row][col] == 0:
#                 for i in range(1,10):
#                     matrix[row][col] = i
#                     if is_valid(matrix):
#                         return row, col
#     return
#
#
# def next(matrix: List[List[int]], row: int, col: int):
#     for i in range()

def solve(matrix: List[List[int]]):
    if not is_valid(matrix):
        return
    for row in range(9):
        for col in range(9):
            if matrix[row][col] != 0:
                continue
            for num in range(1, 10):
                matrix[row][col] = num
                solve(matrix)
                matrix[row][col] = 0
            return
    print("Result:")
    pretty_print(matrix)


if __name__ == '__main__':
    input_matrix = [
        [9, 3, 0, 0, 1, 0, 0, 7, 2],
        [6, 7, 0, 2, 0, 3, 0, 5, 4],
        [8, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 5, 0, 0, 0, 7, 0, 8, 0],
        [3, 0, 0, 0, 4, 0, 0, 0, 1],
        [0, 9, 0, 6, 0, 0, 0, 2, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 8],
        [2, 4, 0, 9, 0, 5, 0, 3, 7],
        [7, 1, 0, 0, 3, 0, 0, 4, 6]
    ]
    print("Input matrix:")
    pretty_print(input_matrix)
    solve(input_matrix)
    # print(f"Valid: {is_valid(input_matrix)}")
