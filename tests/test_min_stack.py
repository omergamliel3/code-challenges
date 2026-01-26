import unittest
from parameterized import parameterized

from solutions.min_stack import MinStack


class TestMinStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = MinStack()


class TestBasicOperations(TestMinStack):
    def test_given_single_push_then_top_returns_value(self) -> None:
        self.stack.push(5)
        self.assertEqual(5, self.stack.top())

    def test_given_single_push_then_getMin_returns_value(self) -> None:
        self.stack.push(5)
        self.assertEqual(5, self.stack.getMin())

    def test_given_push_and_pop_then_stack_is_empty(self) -> None:
        self.stack.push(10)
        self.stack.pop()
        self.assertTrue(len(self.stack._stack) == 0)


class TestMultiplePushes(TestMinStack):
    @parameterized.expand([
        ("ascending_order", [1, 2, 3], 3, 1),
        ("descending_order", [3, 2, 1], 1, 1),
        ("mixed_order", [2, 1, 3], 3, 1),
        ("all_same", [5, 5, 5], 5, 5),
        ("negative_values", [-3, -1, -2], -2, -3),
        ("mixed_signs", [-1, 0, 1], 1, -1),
    ])
    def test_given_multiple_pushes_then_top_and_min_correct(
        self,
        _,
        values: list[int],
        expected_top: int,
        expected_min: int,
    ) -> None:
        for val in values:
            self.stack.push(val)
        self.assertEqual(expected_top, self.stack.top())
        self.assertEqual(expected_min, self.stack.getMin())


class TestPopBehavior(TestMinStack):
    def test_given_pop_non_min_value_then_min_unchanged(self) -> None:
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(1, self.stack.getMin())

    def test_given_pop_min_value_then_min_updates(self) -> None:
        self.stack.push(2)
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(2, self.stack.getMin())

    def test_given_pop_when_duplicates_of_min_then_min_correct(self) -> None:
        self.stack.push(1)
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(1, self.stack.getMin())


class TestBoundaryValues(TestMinStack):
    @parameterized.expand([
        ("max_int", 2**31 - 1),
        ("min_int", -(2**31)),
        ("zero", 0),
    ])
    def test_given_boundary_value_then_operations_work(
        self, _, value: int
    ) -> None:
        self.stack.push(value)
        self.assertEqual(value, self.stack.top())
        self.assertEqual(value, self.stack.getMin())
        self.stack.pop()


class TestSequenceOfOperations(TestMinStack):
    def test_given_example_sequence_then_returns_expected(self) -> None:
        self.stack.push(-2)
        self.stack.push(0)
        self.stack.push(-3)
        self.assertEqual(-3, self.stack.getMin())
        self.stack.pop()
        self.assertEqual(0, self.stack.top())
        self.assertEqual(-2, self.stack.getMin())

    def test_given_alternating_push_pop_then_min_tracked(self) -> None:
        self.stack.push(3)
        self.assertEqual(3, self.stack.getMin())

        self.stack.push(1)
        self.assertEqual(1, self.stack.getMin())

        self.stack.push(2)
        self.assertEqual(1, self.stack.getMin())

        self.stack.pop()
        self.assertEqual(1, self.stack.getMin())

        self.stack.pop()
        self.assertEqual(3, self.stack.getMin())

    def test_given_decreasing_sequence_then_all_values_tracked(self) -> None:
        values = [5, 4, 3, 2, 1]
        for val in values:
            self.stack.push(val)
            self.assertEqual(val, self.stack.getMin())

        for expected_min in range(1, 6):
            self.assertEqual(expected_min, self.stack.getMin())
            self.stack.pop()

    def test_given_increasing_sequence_then_first_always_min(self) -> None:
        values = [1, 2, 3, 4, 5]
        for val in values:
            self.stack.push(val)
            self.assertEqual(1, self.stack.getMin())


class TestEqualValues(TestMinStack):
    def test_given_multiple_equal_min_values_then_pop_preserves(self) -> None:
        self.stack.push(1)
        self.stack.push(1)
        self.stack.push(1)
        self.assertEqual(1, self.stack.getMin())

        self.stack.pop()
        self.assertEqual(1, self.stack.getMin())

        self.stack.pop()
        self.assertEqual(1, self.stack.getMin())


class TestInternalState(TestMinStack):
    def test_given_new_min_pushed_then_min_stack_updated(self) -> None:
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(2)
        self.assertEqual([5, 3, 2], self.stack._min_values_stack)

    def test_given_min_popped_then_min_stack_updated(self) -> None:
        self.stack.push(2)
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual([2], self.stack._min_values_stack)

    def test_given_values_pushed_then_min_value_property_works(self) -> None:
        self.stack.push(10)
        self.stack.push(5)
        self.assertEqual(5, self.stack._min_value)


if __name__ == "__main__":
    unittest.main()
