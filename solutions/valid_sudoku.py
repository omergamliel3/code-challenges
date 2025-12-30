"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # each row must contain digits without repetition. TIME: O(1), SPACE: O(1)
        for row in board:
            for cell in row:
                if cell.isdigit():
                    if row.count(cell) > 1:
                        return False

        # each column must contain digits without repetition. TIME: O(1), SPACE: O(n)
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                cell = board[j][i]
                if cell.isdigit() and cell in seen:
                    return False

                seen.add(cell)

        # each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition. TIME: O(1), SPACE: O(n)
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                seen = set()
                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        cell = board[r][c]
                        if cell.isdigit() and cell in seen:
                            return False
                        seen.add(cell)

        return True


def main():
    s = Solution()
    board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                           ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                           ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(f"Valid board: {s.isValidSudoku(board1)}")
    print(f"Valid board: {s.isValidSudoku(board2)}")


if __name__ == "__main__":
    main()
