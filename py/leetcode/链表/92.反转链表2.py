from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 注意可以使用dummy
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        p0 = dummy = ListNode(next=head)
        for _ in range(left - 1):
            p0 = p0.next

        prev, curr = None, p0.next
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        nxt = p0.next
        nxt.next = curr
        p0.next = prev
        return dummy.next
