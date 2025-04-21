from typing import List

# 翻转 None 标记法

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def preorder(root: TreeNode) -> List[int]:
    # root left right
    ans = stk = []
    if root:
        stk.append(root)
    while stk:
        node = stk.pop()
        if node:
            # [right left root none]
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
            stk.append(node)
            stk.append(None)
        else:
            node = stk.pop()
            ans.append(node.val)
    return ans


def inorder(root: TreeNode) -> List[int]:
    # left root right
    ans = stk = []
    if root:
        stk.append(root)
    while stk:
        node = stk.pop()
        if node:
            # [right root none left]
            if node.right:
                stk.append(node.right)
            stk.append(node)
            stk.append(None)
            if node.left:
                stk.append(node.left)
        else:
            node = stk.pop()
            ans.append(node.val)
    return ans


def postorder(root: TreeNode) -> List[int]:
    # left right root
    ans = stk = []
    if root:
        stk.append(root)
    while stk:
        node = stk.pop()
        if node:
            # [root none right left]
            stk.append(node)
            stk.append(None)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
        else:
            node = stk.pop()
            ans.append(node.val)
    return ans