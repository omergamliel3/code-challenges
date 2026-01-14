from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def reverse_list_naive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    original_nodes: list[ListNode] = []

    current = head
    while current:
        original_nodes.append(current)
        current = current.next

    reveresed_nodes = list(reversed(original_nodes))
    for i in range(len(reveresed_nodes) - 1):
        reveresed_nodes[i].next = reveresed_nodes[i + 1]

    reveresed_nodes[-1].next = None
    return reveresed_nodes[0]


def main():
    pass


if __name__ == "__main__":
    main()
