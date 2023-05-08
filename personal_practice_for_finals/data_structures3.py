#!/usr/bin/env python3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n * log(n)) for both space and time
def sorted_array_to_bst(array):
    if not array:
        return None

    mid = len(array) // 2
    root = TreeNode(array[mid])

    # Divide and conquer: create left and right subtrees recursively
    root.left = sorted_array_to_bst(array[:mid])
    root.right = sorted_array_to_bst(array[mid+1:])

    return root

#space complexity is between O(log(n)) and O(n)
# time O(n)
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.val, end=' ')
        inorder_traversal(node.right)

if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7]
    root = sorted_array_to_bst(sorted_array)

    print("Inorder traversal of the balanced BST:")
    inorder_traversal(root)
    print()
