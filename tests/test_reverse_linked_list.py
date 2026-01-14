from typing import Optional
import unittest
from parameterized import parameterized

from solutions.reverse_linked_list import ListNode, reverse_list


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


class TestReverseLinkedList(unittest.TestCase):
    @parameterized.expand([
        # --- Edge cases ---
        ([],),
        ([1],),

        # --- Simple sequences ---
        ([1, 2, 3],),
        ([1, 2, 3, 4],),
        ([1, 2, 3, 4, 5],),
    ])
    def test_given_linked_list_then_return_reversed(self, input_values: list[int]):
        original_head = build_linked_list(input_values)
        original_nodes = get_node_sequence(original_head)

        reversed_head = reverse_list(original_head)
        reversed_nodes = get_node_sequence(reversed_head)

        self.assertListEqual(original_nodes, list(reversed(reversed_nodes)))


if __name__ == "__main__":
    unittest.main()
