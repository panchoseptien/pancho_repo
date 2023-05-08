#!/usr/bin/env python3
'''
Title:      tree.py
Abstract:   Implement a binary tree read and walk functions.
Author:     Francisco Septien Quintana
Email:      fquinta@nd.edu
Estimate:   25 minutes
Date:       11/01/2022
Questions:
    1. What is the worst-case time complexity of tree_read()?
        O(n)
    2. What is the worst-case time complexity of tree_walk()?
        O(n)
    3. In tree_walk(), how did you modify BFS to print all the nodes on one
    comma separated line?
        Instead of printing each node separately, I accumulated their values in a 
        list and used the join function to print the list as a comma-separated line.
    4. In tree_walk(), how did you remove any trailing invalid nodes from your
    output?
        I used a while loop to remove the 0 after the last element of the tree 
'''

from dataclasses import dataclass
from collections import deque

# Classes

@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None

# Functions

def tree_read(array, index=0):
    ''' Return a node-based tree from the given array of values in BFS format.
    >>> tree_read([1, 2, 3])
    Node(value=1, left=Node(value=2, left=None, right=None), right=Node(value=3, left=None, right=None))
    >>> tree_read([1, 2, 3, 4, 0, 0, 6])
    Node(value=1, left=Node(value=2, left=Node(value=4, left=None, right=None), right=None), right=Node(value=3, left=None, right=Node(value=6, left=None, right=None)))
    '''
    if index >= len(array) or array[index] == 0:
        return None

    root = Node(value=array[index])
    root.left = tree_read(array, 2 * index + 1)
    root.right = tree_read(array, 2 * index + 2)

    return root

def tree_walk(root):
    ''' Print out the tree in level-by-level order with each level on the same
    line.
    >>> tree_walk(tree_read([1, 2, 3]))
    1, 2, 3
    >>> tree_walk(tree_read([1, 2, 3, 4, 0, 0, 6]))
    1, 2, 3, 4, 0, 0, 6
    '''
    if not root:
        return ""

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        if not node:
            values.append(0)
            continue

        values.append(node.value)

        queue.append(node.left)       
        queue.append(node.right)

    # Remove trailing invalid nodes (zeros)
    while values and values[-1] == 0:
        values.pop()

    print(', '.join(str(value) for value in values))