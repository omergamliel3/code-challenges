import unittest

from parameterized import parameterized

from solutions.count_collisions_on_road import CountCollisions


class CountCollisionsOnRoad(unittest.TestCase):
    def setUp(self) -> None:
        self.count_collisions = CountCollisions()
        return super().setUp()

    @parameterized.expand([
        ("RLRSLL", 5),
        ("LLLRRR", 0),
        ("RRRRL", 5),
        ("LR", 0),
        ("RL", 2)
    ])
    def test_given_directions_then_return_collision_count(self, directions_string: str, expected_count: int):
        count = self.count_collisions.countCollisions(directions_string)
        self.assertEqual(count, expected_count)


if __name__ == "__main__":
    unittest.main()
