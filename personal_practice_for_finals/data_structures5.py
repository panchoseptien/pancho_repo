#!/usr/bin/env python3
# this is a continuation of the code that implements a binary search tree 

from collections import deque

class AVLTree:
    # ... (existing code) ...

    def bfs_traversal(self):
        if not self.root:
            return []

        traversal = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            traversal.append(node.key)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return traversal

    def dfs_traversal(self):
        return self._dfs_traversal(self.root)

    def _dfs_traversal(self, node):
        if not node:
            return []

        left_traversal = self._dfs_traversal(node.left)
        right_traversal = self._dfs_traversal(node.right)
        return [node.key] + left_traversal + right_traversal

if __name__ == "__main__":
    avl_tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        avl_tree.insert(key)

    print("Inorder traversal of the AVL tree:", avl_tree.inorder_traversal())
    print("BFS traversal of the AVL tree:", avl_tree.bfs_traversal())
    print("DFS traversal of the AVL tree:", avl_tree.dfs_traversal())
