# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #1 - Basic Data Structures: Linked Lists and Stacks
# Application: Balancing Symbols
# Description: This application uses a linked list stack implementation to
#     discern if an input string consists of a balanced specified opening
#     or closing symbols
# File Dependencies: DarionGuannode.py, DarionGuanstack.py
# Time Complexity: O(N)
# Space Complexity: O(N)
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuana1.py
# Date: 1/31/23

import DarionGuanstack as st


# Test driver implementation
# Non characters are ignored
# Opening symbols are pushed
# Closing characters results in return of 0 if stack is empty - otherwise pop
# If popped character does not correspond to the top of stack, return 0
def driver(test):
    s = st.Stack.create_stack()
    for char in test:
        if opening(char):
            s.push(char)
        elif closing(char) and s.is_empty():
            return 0
        elif closing(char) and not s.is_empty():
            popped = s.pop()
            if not correspond(popped, char):
                return 0
        else:
            continue
    return 1


# Check if symbols correspond
def correspond(popped, char):
    if (popped == '(' and char == ')') or (popped == '{' and char == '}') \
            or (popped == '[' and char == ']'):
        return True
    else:
        return False


# Validate opening symbol
def opening(char):
    result = False
    special = "({["
    for i in special:
        if char == i:
            result = True
    return result


# Validates closing symbol
def closing(char):
    result = False
    special = "]})"
    for i in special:
        if char == i:
            result = True
    return result


# Testing specification:

# Test of balanced symbols
test1 = "([|])"
test2 = "() (() [()])"
test3 = "{{([][])}()}"

test4 = "[a]"  # Non symbol handling
test5 = "[])"  # Pop attempt on empty stack
test6 = "(]"  # Incorrect pairing

print(driver(test1))
print(driver(test2))
print(driver(test3))
print(driver(test4))
print(driver(test5))
print(driver(test6))

# Commented out run
"""
/Users/darionguan/PycharmProjects/pythonProject/venv/bin/python /Users/
darionguan/PycharmProjects/pythonProject/DarionGuana1.py 
1
1
1
1
0
0

Process finished with exit code 0

"""