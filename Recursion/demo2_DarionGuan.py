# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #2 - Recursion
# Application: Pascal's Triangle
# Description: This is a test driver the triangle() function from
#              DarionGuanLab2.py
# File Dependencies: DarionGuanLab2.py
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuanLab2.py
# Date: 2/7/23

import DarionGuanLab2 as pascal


# Test cases for lines 0-6
print(pascal.triangle(0))
print(pascal.triangle(1))
print(pascal.triangle(2))
print(pascal.triangle(3))
print(pascal.triangle(4))
print(pascal.triangle(5))
print(pascal.triangle(6))

# Test case for length of first name + last name:
# Name: Darion Guan
# Length = 10
print(pascal.triangle(10))

# Commented out run
"""
/Users/darionguan/PycharmProjects/pythonProject/venv/bin/python /Users/
darionguan/PycharmProjects/pythonProject/Lab#2Recursion/demo2_DarionGuan.py 
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

Process finished with exit code 0
"""
