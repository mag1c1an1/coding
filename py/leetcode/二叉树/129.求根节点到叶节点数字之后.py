# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if not node.left and not node.right:
                ans += node.val
            if node.left:
                dq.append(node.left)
                node.left.val = node.val * 10 + node.left.val
            if node.right:
                dq.append(node.right)
                node.right.val = node.val * 10 + node.right.val
        return ans
