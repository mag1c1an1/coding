class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    # key
    root.left = build_tree(preorder[1 : mid + 1], inorder[:mid])
    # key
    root.right = build_tree(preorder[mid + 1 :], inorder[mid + 1 :])
    return root


def update_tree(node):
    if not node:
        return 0
    left_sum = update_tree(node.left)
    right_sum = update_tree(node.right)
    old_val = node.val
    node.val = left_sum + right_sum
    return node.val + old_val


def inorder_tra(node):
    if not node:
        return []

    return inorder_tra(node.left) + [node.val] + inorder_tra(node.right)


if __name__ == "__main__":
    inorder = list(map(int, input().split()))
    preorder = list(map(int, input().split()))

    root = build_tree(preorder, inorder)
    update_tree(root)
    print(" ".join(map(str, inorder_tra(root))))
