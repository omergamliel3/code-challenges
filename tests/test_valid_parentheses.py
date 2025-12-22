import unittest

from parameterized import parameterized

from solutions.valid_parentheses import is_valid_parentheses


class TestValidParentheses(unittest.TestCase):
    @parameterized.expand([
        ("()",),
        ("()[]{}",),
        ("([])",),
    ])
    def test_given_valid_string_then_return_true(self, input: str):
        self.assertTrue(is_valid_parentheses(input))

    @parameterized.expand([
        ("(]",),
        ("([)]",),
    ])
    def test_given_invalid_string_then_return_false(self, input: str):
        self.assertFalse(is_valid_parentheses(input))


if __name__ == "__main__":
    unittest.main()
