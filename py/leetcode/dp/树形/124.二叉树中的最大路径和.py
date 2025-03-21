from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


# 枚举拐点
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(root):
            if not root:
                return 0
            l_v = dfs(root.left)

            r_v = dfs(root.right)
            nonlocal ans
            ans = max(ans, l_v + r_v + root.val)
            return max(max(l_v, r_v) + root.val, 0)

        return int(ans)
