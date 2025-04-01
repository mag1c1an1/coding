# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from math import inf
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -inf

        def dfs(root, k):
            if not root:
                return
            dfs(root.left, k - 1)
            if k == 0:
                nonlocal ans
                ans = root.val
                return
            dfs(root.right, k - 1)

        return ans
