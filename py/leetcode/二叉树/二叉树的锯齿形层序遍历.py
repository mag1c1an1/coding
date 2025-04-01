# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        ans = []
        left = True
        while dq:
            tmp = []
            for _ in range(len(dq)):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            ans.append(tmp[::-1] if len(ans) % 2 else tmp)
        return ans
