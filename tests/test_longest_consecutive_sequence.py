import unittest
from parameterized import parameterized

from solutions.longest_consecutive_sequence import longest_consecutive


class TestLongestConsecutiveSequence(unittest.TestCase):
    @parameterized.expand([
        # Edge cases
        ([], 0),
        ([1], 1),
        ([5, 5, 5], 1),

        # Basic consecutive sequences
        ([1, 2], 2),
        ([2, 1], 2),
        ([10, 11, 12], 3),

        # Non-consecutive elements
        ([1, 3, 5, 7], 1),

        # Negative numbers
        ([-1, -2, -3, -4], 4),
        ([-2, -1, 0, 1, 2], 5),

        # Mixed negative and positive
        ([-1, 1, 0], 3),

        # Duplicates with gaps
        ([1, 2, 2, 3], 3),
        ([4, 2, 1, 6, 5, 3, 3], 6),

        # Large gaps
        ([100, 300, 200, 1], 1),

        # Multiple sequences, pick longest
        ([1, 2, 3, 10, 11, 12, 13], 4),

        # Single long sequence with noise
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -2, 6], 7),
    ])
    def test_given_array_then_return_length_of_longest_consecutive_sequence(
        self,
        input: list[int],
        expected_length: int
    ):
        self.assertEqual(longest_consecutive(input), expected_length)


if __name__ == "__main__":
    unittest.main()
