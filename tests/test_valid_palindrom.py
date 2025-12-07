import unittest
from parameterized import parameterized

from solutions.valid_palindrom import ValidPalindrome


class TestValidPalindrome(unittest.TestCase):

    def setUp(self) -> None:
        self.palindrome = ValidPalindrome()
        return super().setUp()

    @parameterized.expand([
        ("A man, a plan, a canal: Panama",),
        (" ",),
        ("abcddcba",),
        ("aba aba aba aba, aba",),
    ])
    def test_given_valid_palindrom_then_return_true(self, input: str):
        is_palindrome = self.palindrome.isPalindrome(input)
        self.assertTrue(is_palindrome)

    @parameterized.expand([
        ("race a car",),
        ("omer loves cats",),
        ("wish, you, where, here, pink, floyd",),
        ("abaa",),
    ])
    def test_given_invalid_palindrom_then_return_false(self, input: str):
        is_palindrome = self.palindrome.isPalindrome(input)
        self.assertFalse(is_palindrome)


if __name__ == "__main__":
    unittest.main()
