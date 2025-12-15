import unittest
from parameterized import parameterized

from solutions.valid_anagram import is_anagram


class TestValidAnagram(unittest.TestCase):
    @parameterized.expand([
        ("anagram", "nagaram"),
        ("listen", "silent"),
        ("evil", "vile"),
        ("aabbcc", "abcabc"),
        ("", ""),
        ("a", "a"),
    ])
    def test_given_valid_anagram_then_return_true(self, first: str, second: str):
        self.assertTrue(is_anagram(first, second))

    @parameterized.expand([
        ("rat", "car"),
        ("hello", "bello"),
        ("aabb", "ab"),
        ("test", "tseta"),
        ("abc", "abd"),
    ])
    def test_given_invalid_anagram_then_return_false(self, first: str, second: str):
        self.assertFalse(is_anagram(first, second))


if __name__ == "__main__":
    unittest.main()
