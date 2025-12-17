import unittest
from parameterized import parameterized

from solutions.merge_intervals import merge


class TestMergeIntervals(unittest.TestCase):
    @parameterized.expand([
        # --- Single interval ---
        ([[1, 3]], [[1, 3]]),

        # --- Simple overlapping ---
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),

        # --- Touching boundaries (inclusive overlap) ---
        ([[1, 4], [4, 5]], [[1, 5]]),

        # --- Unsorted input ---
        ([[4, 7], [1, 4]], [[1, 7]]),
        ([[8, 10], [1, 3], [2, 6]], [[1, 6], [8, 10]]),

        # --- Fully contained intervals ---
        ([[1, 10], [2, 3], [4, 8]], [[1, 10]]),

        # --- No overlap ---
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),

        # --- Multiple merges into one ---
        ([[1, 4], [2, 5], [3, 6]], [[1, 6]]),

        # --- Duplicate intervals ---
        ([[1, 3], [1, 3], [1, 3]], [[1, 3]]),

        # --- Zero-length intervals ---
        ([[1, 1], [1, 2], [2, 2]], [[1, 2]]),

        # --- Chain overlap ---
        ([[1, 2], [2, 3], [3, 4]], [[1, 4]]),

        # --- Large range ---
        ([[0, 10000], [5, 10], [20, 30]], [[0, 10000]]),
    ])
    def test_given_intervals_then_return_merged_overlapping(
        self,
        intervals: list[list[int]],
        expected_merged_intervals: list[list[int]],
    ):
        res = merge(intervals)
        self.assertEqual(res, expected_merged_intervals)


if __name__ == "__main__":
    unittest.main()
