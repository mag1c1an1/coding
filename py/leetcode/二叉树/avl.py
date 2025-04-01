# coding: utf-8
class AVLNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def __init__(self):
        self.root = None

    def find(self, val):
        return self._find(self.root, val)

    def _find(self, node, val):
        if not node:
            return False

        if node.val > val:
            # 比当前节点的值小，继续递归查找当前节点的左子树
            return self._find(node.left, val)
        elif node.val < val:
            # 比当前节点的值大，继续递归查找当前节点的右子树
            return self._find(node.right, val)
        else:
            return True

    def insert(self, val):
        if self.find(val):
            return

        if not self.root:
            self.root = AVLNode(val)
        else:
            self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return AVLNode(val)

        if node.val > val:
            # 比当前节点的值小，继续递归查找当前节点的左子树
            node.left = self._insert(node.left, val)
        elif node.val < val:
            # 比当前节点的值大，继续递归查找当前节点的右子树
            node.right = self._insert(node.right, val)

        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1

        # 插入之后，需要重平衡
        return self._re_balance(node)

    @staticmethod
    def _get_height(node):
        if not node:
            return 0

        return node.height

    def _diff_left_right_height(self, node):
        if not node:
            return 0

        return self._get_height(node.left) - self._get_height(node.right)

    def _re_balance(self, node):
        if not node:
            return

        diff_l_r_height = self._diff_left_right_height(node)

        if diff_l_r_height > 1:
            if self._get_height(node.left.left) > self._get_height(
                    node.left.right):
                return self._rotate_single_right(node)
            else:
                return self._rotate_left_right(node)
        elif diff_l_r_height < -1:
            if self._get_height(node.right.left) < self._get_height(
                    node.right.right):
                return self._rotate_single_left(node)
            else:
                return self._rotate_right_left(node)

        return node

    def _rotate_single_right(self, node):
        """node为需要调整的子树根节点"""
        # 原根节点的左子树节点作为新根节点
        new_node = node.left
        # 原根节点的左子树指向新根节点的原右子树
        node.left = new_node.right
        # 新根节点的新右子树指向原根节点
        new_node.right = node
        # 更新原根节点的最大高度
        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1
        # 更新新根节点的最大高度
        new_node.height = max(self._get_height(new_node.left),
                              self._get_height(new_node.right)) + 1
        return new_node

    def _rotate_single_left(self, node):
        """node为需要调整的子树根节点"""
        # 原根节点的右子树节点作为新根节点
        new_node = node.right
        # 原根节点的右子树指向新根节点的原左子树
        node.right = new_node.left
        # 新根节点的新左子树指向原根节点
        new_node.left = node
        # 更新原根节点的最大高度
        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1
        # 更新新根节点的最大高度
        new_node.height = max(self._get_height(new_node.left),
                              self._get_height(new_node.right)) + 1
        return new_node

    def _rotate_left_right(self, node):
        """node为需要调整的子树根节点"""
        # 先将原根节点的左子树左旋，作为原根节点的新左子树
        node.left = self._rotate_single_left(node.left)
        # 将原根节点右旋
        return self._rotate_single_right(node)

    def _rotate_right_left(self, node):
        """node为需要调整的子树根节点"""
        # 先将原根节点的右子树右旋，作为原根节点的新右子树
        node.right = self._rotate_single_right(node.right)
        # 将原根节点左旋
        return self._rotate_single_left(node)

    def delete(self, val):
        if not self.find(val):
            return False
        else:
            self._delete(self.root, val)
            return True

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if node.left:
            return self._find_min(node.left)
        else:
            return node

    def _delete(self, node, val):
        if not node:
            return

        if val < node.val:
            # 比当前节点的值小，继续查找当前节点的左子树
            self._delete(node.left, val)
        elif val > node.val:
            # 比当前节点的值大，继续查找当前节点的右子树
            self._delete(node.right, val)
        else:
            # 已找到需要删除的节点
            if node.left and node.right:
                # 待删除的节点同时有左右子树时，找到该节点的右子树的最小值覆盖该节点的值
                node.val = self._find_min(node.right).val
                # 然后转换为删除该节点右子树下该最小值对应节点
                node.right = self._delete(node.right, node.val)
            else:
                # 待删除的节点只有左右子树之一时，将待删除节点指针指向该子树，后续从该节点开始，从下向上依次调整该条路径上的平衡
                node = node.left if not node.right else node.right

        if not node:
            return

        node.height = max(self._get_height(node.left),
                          self._get_height(node.right)) + 1

        # 插入之后，需要重平衡
        return self._re_balance(node)


if __name__ == '__main__':
    test = AVLTree()
    test.insert(1)
    test.insert(2)
    test.insert(3)
    print(test.find(3))
    test.delete(2)
    print(test.find(2))
    print(test.find(3))

