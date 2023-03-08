# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #4 - Binary Trees
# Application: Finding MAX in Binary Trees
# Description: This application uses a node implementation to create binary
#              trees. It provides basic and auxiliary binary tree operations
#              as well as an operation to find the maximum element in the tree.
# File Dependencies: N/A
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuanLab4.py
# Date: 3/7/2023

class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.leftChild = None
        self.rightChild = None

    # Insert an element into a tree
    def insert_left(self, new_node):
        if self.leftChild is None:
            self.leftChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, new_node):
        if self.rightChild is None:
            self.rightChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def delete(self, key):
        # No children
        if self.key == key and self.leftChild is None and \
                self.rightChild is None:
            return None

        # One child
        if self.key == key and self.leftChild is None:
            return self.rightChild
        if self.key == key and self.rightChild is None:
            return self.leftChild

        # Two children
        if self.key == key and self.leftChild is not None and \
                self.rightChild is not None:
            successor = self.rightChild
            while successor.leftChild is not None:
                successor = successor.leftChild
            self.key = successor.key
            self.rightChild = self.rightChild.delete(successor.key)

        if key < self.key:
            if self.leftChild is not None:
                self.leftChild = self.leftChild.delete(key)

        if key > self.key:
            if self.rightChild is not None:
                self.rightChild = self.rightChild.delete(key)

        return self

    # Search for an element
    def search(self, value):
        if self.key == value:
            return True
        elif self.leftChild and value < self.key:
            return self.leftChild.search(value)
        elif self.rightChild and value > self.key:
            return self.rightChild.search(value)
        else:
            return False

    # Traverse the tree (preorder, inorder, and postorder)
    # Preorder: root, left, right
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    # Inorder: left, root, right
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    # Postorder: left, right, root
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    # Find the size of the tree
    def size(self):
        if self.leftChild and self.rightChild:
            return 1 + self.leftChild.size() + self.rightChild.size()
        elif self.leftChild:
            return 1 + self.leftChild.size()
        elif self.rightChild:
            return 1 + self.rightChild.size()
        else:
            return 1

    # Find the height of the tree
    def height(self):
        if self.leftChild is None and self.rightChild is None:
            return 0
        elif self.leftChild is None:
            return 1 + self.rightChild.height()
        elif self.rightChild is None:
            return 1 + self.leftChild.height()
        else:
            return 1 + max(self.leftChild.height(), self.rightChild.height())

    # Find the max element in the binary tree using a recursive solution
    def find_max(self):
        if self.rightChild is None and self.leftChild is None:
            return self.key
        elif self.rightChild is None:
            left = self.leftChild.find_max()
            return max(self.key, left)
        elif self.leftChild is None:
            right = self.rightChild.find_max()
            return max(self.key, right)
        else:
            left = self.leftChild.find_max()
            right = self.rightChild.find_max()
            return max(self.key, left, right)


# Find the size of the tree
def size(node):
    if node is None:
        return 0
    else:
        return 1 + size(node.leftChild) + size(node.rightChild)
