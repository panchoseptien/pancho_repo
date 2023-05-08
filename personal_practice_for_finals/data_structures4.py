#!/usr/bin/env python3
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1:
            if key < node.left.key:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        elif balance < -1:
            if key > node.right.key:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        result = []
        if node:
            result = self._inorder_traversal(node.left)
            result.append(node.key)
            result += self._inorder_traversal(node.right)
        return result


if __name__ == "__main__":
    avl_tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        avl_tree.insert(key)

    print("Inorder traversal of the AVL tree:", avl_tree.inorder_traversal())
