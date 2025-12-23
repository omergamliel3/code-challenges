import unittest
from parameterized import parameterized

from solutions.simplify_path import simplify_path


class TestSimplifyPath(unittest.TestCase):
    @parameterized.expand([
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
    ])
    def test_given_path_then_return_simplified(self, path: str, expected_path: str):
        self.assertEqual(simplify_path(path), expected_path)


if __name__ == "__main__":
    unittest.main()
