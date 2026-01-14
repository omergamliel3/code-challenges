from typing import Optional, TypedDict
import unittest
from parameterized import parameterized

from solutions.reverse_linked_list_between import ListNode, reverse_list_between


class TestCase(TypedDict):
    input_values: list[int]
    left: int
    right: int
    description: str


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def get_node_sequence(head: Optional[ListNode]) -> list[ListNode]:
    nodes = []
    current = head

    while current:
        nodes.append(current)
        current = current.next

    return nodes


TEST_CASES: list[TestCase] = [
    {
        "input_values": [1, 2, 3],
        "left": 1,
        "right": 3,
        "description": "Reverse entire list of 3 elements",
    },
    {
        "input_values": [1, 2, 3],
        "left": 2,
        "right": 3,
        "description": "Reverse last 2 elements of 3-element list",
    },
    {
        "input_values": [1, 2, 3, 4],
        "left": 1,
        "right": 3,
        "description": "Reverse first 3 elements of 4-element list",
    },
    {
        "input_values": [1, 2, 3, 4, 5],
        "left": 2,
        "right": 4,
        "description": "Reverse middle 3 elements of 5-element list",
    },
]


class TestReverseLinkedListBetween(unittest.TestCase):
    @parameterized.expand([
        (test_case["input_values"], test_case["left"], test_case["right"]) for test_case in TEST_CASES
    ])
    def test_given_linked_list_then_return_reversed_between(self, input_values: list[int], left: int, right: int):
        original_head = build_linked_list(input_values)
        original_nodes = get_node_sequence(original_head)

        reversed_head = reverse_list_between(original_head, left, right)
        reversed_nodes = get_node_sequence(reversed_head)

        self.assertListEqual(
            original_nodes[:left - 1], reversed_nodes[:left - 1])
        self.assertListEqual(
            original_nodes[left - 1:right],
            list(reversed(reversed_nodes[left - 1:right]))
        )
        self.assertListEqual(original_nodes[right:], reversed_nodes[right:])


if __name__ == "__main__":
    unittest.main()
