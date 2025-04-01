# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        lst = []

        def helper(node, prefix):
            if not node:
                prefix.append("None")
            else:
                prefix.append(str(node.val))
                helper(node.left, prefix)
                helper(node.right, prefix)

        helper(root, lst)
        return ",".join(lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dq = deque(data.split(","))

        def helper(dq):
            first = dq.popleft()
            if first == "None":
                return None

            root = TreeNode(int(first))
            root.left = helper(dq)
            root.right = helper(dq)
            return root

        return helper(dq)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
