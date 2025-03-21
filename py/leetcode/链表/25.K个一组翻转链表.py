from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 注意使用dummy
# 知道所有指针的指向


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        p0 = dummy = ListNode(next=head)
        prev, curr = None, head
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            nxt = p0.next
            nxt.next = curr
            p0.next = prev
            p0 = nxt
        return dummy.next

