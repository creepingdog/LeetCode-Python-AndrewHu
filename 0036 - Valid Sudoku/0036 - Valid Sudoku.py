from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.


    A partially filled sudoku which is valid.

    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

    Example 1:

    Input:
    [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: true

    Example 2:

    Input:
    [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being
        modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

    Note:

        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.
        The given board contain only digits 1-9 and the character '.'.
        The given board size is always 9x9.

    >>> is_valid_sudoku([\
      ["5","3",".",".","7",".",".",".","."],\
      ["6",".",".","1","9","5",".",".","."],\
      [".","9","8",".",".",".",".","6","."],\
      ["8",".",".",".","6",".",".",".","3"],\
      ["4",".",".","8",".","3",".",".","1"],\
      ["7",".",".",".","2",".",".",".","6"],\
      [".","6",".",".",".",".","2","8","."],\
      [".",".",".","4","1","9",".",".","5"],\
      [".",".",".",".","8",".",".","7","9"]\
    ])
    True
    >>> is_valid_sudoku([\
      ["8","3",".",".","7",".",".",".","."],\
      ["6",".",".","1","9","5",".",".","."],\
      [".","9","8",".",".",".",".","6","."],\
      ["8",".",".",".","6",".",".",".","3"],\
      ["4",".",".","8",".","3",".",".","1"],\
      ["7",".",".",".","2",".",".",".","6"],\
      [".","6",".",".",".",".","2","8","."],\
      [".",".",".","4","1","9",".",".","5"],\
      [".",".",".",".","8",".",".","7","9"]\
    ])
    False
    """
    SIZE = 9
    row_checks = [dict() for i in range(SIZE)]
    col_checks = [dict() for i in range(SIZE)]
    block_checks = [dict() for i in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            num = board[i][j]
            if num == '.':
                continue
            if num in row_checks[i]:
                # print('i={}, j={}, num={} already in row_checks={}'.format(i, j, num, row_checks[i]))
                return False
            else:
                row_checks[i][num] = 1
            #
            if num in col_checks[j]:
                # print('i={}, j={}, num={} already in col_checks={}'.format(i, j, num, col_checks[j]))
                return False
            else:
                col_checks[j][num] = 1
            #
            block_i = i // 3
            block_j = j // 3
            block_check_index = block_i * 3 + block_j
            if num in block_checks[block_check_index]:
                # print('i={}, j={}, block_i={}, block_j={}, num={} already in block_checks={}'.format(i, j, block_i, block_j, num, block_checks[block_check_index]))
                return False
            else:
                block_checks[block_check_index][num] = 1
            #
        #
    #
    return True
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
