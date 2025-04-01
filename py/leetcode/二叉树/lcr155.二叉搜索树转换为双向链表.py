"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        if not root:
            return root
        head, pre = None, None

        # 中序遍历
        def dfs(cur):
            nonlocal head, pre
            if not cur:
                return
            dfs(cur.left)
            if pre:
                pre.right = cur
                cur.left = pre
            if not head:
                head = cur
            pre = cur
            dfs(cur.right)

        dfs(root)
        head.left = pre
        pre.right = head
        return head
