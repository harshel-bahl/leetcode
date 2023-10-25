# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols = len(board), len(board[0])

        for rowI in range(rows):
            row = board[rowI]

            vals = []
            for val in row:
                if val not in vals and val != ".":
                    vals.append(val)
                elif val == ".":
                    pass
                else:
                    return False

        for colI in range(cols):
            col_vals = []
            for rowI in range(rows):
                if board[rowI][colI] not in col_vals and board[rowI][colI] != ".":
                    col_vals.append(board[rowI][colI])
                elif board[rowI][colI] == ".":
                    pass
                else:
                    return False
                
        for rowI1 in range(0, rows, 3):
            for colI1 in range(0, cols, 3):

                box_vals = []

                for rowI2 in range(rowI1, rowI1 + 3):
                    for colI2 in range(colI1, colI1 + 3):
                        if board[rowI2][colI2] not in box_vals and board[rowI2][colI2] != ".":
                            box_vals.append(board[rowI2][colI2])
                        elif board[rowI2][colI2] == ".":
                            pass
                        else:
                            return False

        return True

solution = Solution()

print(solution.isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], 
                                    ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
                                    [".", "9", "8", ".", ".", ".", ".", "6", "."], 
                                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
                                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
                                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
                                    [".", "6", ".", ".", ".", ".", "2", "8", "."], 
                                    [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
                                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
                                    ))
