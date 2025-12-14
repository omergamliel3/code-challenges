"""
Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
- The '.' character indicates empty cells.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'.
- It is guaranteed that the input board has only one solution.
"""


from typing import Optional


Board = list[list[str]]
DIGITS = set("123456789")


class Cell:
    row: int
    col: int

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col


def get_digist() -> set[str]:
    return DIGITS.copy()


def is_board_completed(board: Board) -> bool:
    for row in board:
        for cell in row:
            if is_cell_empty(cell):
                return False

    return True


def is_cell_empty(cell: str) -> bool:
    return cell == '.'


def get_candidates(board: Board, cell: Cell) -> set[str]:
    row = cell.row
    col = cell.col

    if not is_cell_empty(board[row][col]):
        return set()

    used = set[str]()

    # Row
    used.update(board[row])

    # Column
    for r in range(9):
        used.add(board[r][col])

    # Box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            used.add(board[r][c])

    candidates = get_digist() - used
    return candidates


def find_best_empty_cell(board) -> Optional[Cell]:
    best: Optional[Cell] = None
    min_candidates = 10

    for row in range(9):
        for col in range(9):
            if is_cell_empty(board[row][col]):
                cell = Cell(row, col)
                candidates = get_candidates(board, cell)
                count = len(candidates)

                if count < min_candidates:
                    min_candidates = count
                    best = cell

    return best


def solve_sudoku(board: Board):
    empty_cell = find_best_empty_cell(board)
    if not empty_cell:
        return True

    for digit in get_candidates(board, empty_cell):
        row = empty_cell.row
        col = empty_cell.col
        board[row][col] = digit

        if solve_sudoku(board):
            return True

        board[row][col] = "."

    return False


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
        "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solve_sudoku(board)


if __name__ == "__main__":
    main()
