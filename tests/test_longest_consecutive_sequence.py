import unittest
from parameterized import parameterized

from solutions.longest_consecutive_sequence import longest_consecutive


class TestLongestConsecutiveSequence(unittest.TestCase):
    @parameterized.expand([
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([1, 2, 3, 4], 4),
    ])
    def test_given_array_then_return_length_of_longest_consecutive_sequence(self, input: list[int], expected_length: int):
        self.assertEqual(longest_consecutive(input), expected_length)


if __name__ == "__main__":
    unittest.main()
