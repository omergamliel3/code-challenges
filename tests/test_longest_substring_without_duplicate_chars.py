import unittest

from parameterized import parameterized

from solutions.longest_substring_without_duplicate_chars import lengthOfLongestSubstring


class TestLengthOfLongestSubstring(unittest.TestCase):
    @parameterized.expand([
        ("abcabcbb", 3),
        ("bbbbbbb", 1),
        ("abbb", 2),
        ("abcde abdcef", 7),
        ("pwwkew", 3),
    ])
    def test_given_string_then_return_length_of_longest_substring(self, string: str, expectedLength: int):
        length = lengthOfLongestSubstring(string)
        self.assertEqual(length, expectedLength)


if __name__ == "__main__":
    unittest.main()
