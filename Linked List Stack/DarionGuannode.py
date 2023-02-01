# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #1 - Basic Data Structures: Linked Lists and Stacks
# Description: Node Class of a Singly Linked List
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuannode.py
# Date: 1/31/23

class Node:
    def __init__(self):
        self.data = None
        self.next = None

    # Getter for node data
    def get_data(self):
        return self.data

    # Setter for node data
    def set_data(self, char):
        if self.validate_string(char):
            self.data = char
            return True
        else:
            return False

    # Validate string
    @staticmethod
    def validate_string(char):
        return isinstance(char, str)

    # Getter for node next
    def get_next(self):
        return self.next

    # Setter for node next
    def set_next(self, node):
        if not self.points_to_node():
            self.next = node
            return True
        else:
            return False

    # Checks if node points to another node
    def points_to_node(self):
        return self.get_next() is not None
