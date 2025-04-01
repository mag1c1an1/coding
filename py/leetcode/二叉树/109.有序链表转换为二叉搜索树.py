# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def mid(node, end):
            slow = fast = node
            while fast != end and fast.next != end:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build(l, r):
            if l == r:
                return None
            m = mid(l, r)
            root = TreeNode(m.val)
            root.left = build(l, m)
            root.right = build(m.next, r)
            return root

        return build(head, None)
