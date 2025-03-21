# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 前一半会自己引用自己,最后一个节点早就被引用好了

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        def split(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        half = split(head)
        half = reverse(half)
        # merge
        one = head
        two = half
        while two.next:
            tmp1, tmp2 = one.next, two.next
            one.next = two
            two.next = tmp1
            one = tmp1
            two = tmp2
        return
