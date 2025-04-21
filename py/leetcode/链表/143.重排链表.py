# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode({self.val})"

    def __repr__(self):
        return self.__str__()


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
        while two:
            tmp1, tmp2 = one.next, two.next
            one.next = two
            two.next = tmp1
            one = tmp1
            two = tmp2
        return


def buildList(nums):
    dummy = ListNode(0)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def printList(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print("None")


nums = [1, 2, 3, 4]
head = buildList(nums)
Solution().reorderList(head)
printList(head)
