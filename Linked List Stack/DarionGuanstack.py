# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #1 - Basic Data Structures: Linked Lists and Stacks
# Application: Balancing Symbols
# Description: Stack Class supporting basic stack operations
# File Dependencies: DarionGuannode.py
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuanstack.py
# Date: 1/31/23

import DarionGuannode as nd


class Stack:
    # Constructor with optional parameter value
    def __init__(self, data=None):
        self.head = None
        if data is not None:
            self.head = nd.Node()
            self.head.set_data(data)

    # Push a node onto the top of the stack
    def push(self, data):
        if self.head is None:
            self.head = nd.Node()
            self.head.set_data(data)

        # Temp contains 'data' and 'next' from the existing Node
        # Head is assigned to a new Node
        # Data of the new Node is set to input from the push() method
        # Next of the new Node is set to temp
        else:
            temp = self.head
            self.head = nd.Node()
            self.head.set_data(data)
            self.head.set_next(temp)

    # Remove top node on the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        else:
            popped = self.head.get_data()
            self.head = self.head.get_next()
            return popped

    # Checks if top node exists
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.get_data()

    # Checks if stack is empty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Class method to create a Stack
    @classmethod
    def create_stack(cls):
        return Stack()

    # Release all nodes in the stack
    def delete_stack(self):
        if self.is_empty():
            raise Exception("Cannot clear an empty stack")
        else:
            self.head = None
