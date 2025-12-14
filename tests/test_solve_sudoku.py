import unittest
from parameterized import parameterized

from solutions.solve_sudoku import solve_sudoku
from solutions.valid_sudoku import Solution as SudokuValidator


BOARD_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                        ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


class TestSolveSudoku(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = SudokuValidator()

    @parameterized.expand([
        (BOARD_1,),
    ])
    def test_given_valid_board_then_solve(self, board: list[list[str]]):
        solve_sudoku(board)

        for row in board:
            for cell in row:
                self.assertTrue(cell.isdigit())

        is_valid_board = self.validator.isValidSudoku(board)
        self.assertTrue(is_valid_board)


if __name__ == "__main__":
    unittest.main()
