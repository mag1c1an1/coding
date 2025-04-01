# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def helper(i, j):
            if i >= j:
                return None
            idx = i + (j - i) // 2
            print(i, j, idx)
            root = TreeNode(nums[idx])
            root.left = helper(i, idx)
            root.right = helper(idx + 1, j)
            return root

        return helper(0, n)
