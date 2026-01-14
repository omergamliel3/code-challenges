"""
Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def reverse_list_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head:
        return None

    if left == right:
        return head

    prev = None
    current = head
    pos = 0

    orig_right = None
    orig_left = None

    after_right = None
    before_left = None

    while current:
        pos += 1
        next_node = current.next

        if pos == left - 1:
            before_left = current
        elif pos == left:
            orig_left = current
        elif pos == right:
            orig_right = current
            current.next = prev
        elif left < pos <= right:
            current.next = prev
        elif pos == right + 1:
            after_right = current

        prev = current
        current = next_node

    if before_left and orig_right:
        before_left.next = orig_right

    if orig_left:
        orig_left.next = after_right

    return orig_right if left == 1 else head
