# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #2 - Recursion
# Application: Pascal's Triangle
# Description: This application uses recursion to return the nth line of
#       Pascal's triangle based on input n, a non-negative integer
# File Dependencies: N/A
# Time Complexity: O(2^N)
# Space Complexity: O(N)
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuanLab2.py
# Date: 2/7/23

def triangle(n):
    if n == 0:
        return [1]
    else:
        current = []
        prev = triangle(n - 1)
        for i in range(0, len(prev) + 1):
            if i == 0 or i == len(prev):
                current.append(prev[i - 1])
            else:
                current.append(prev[i - 1] + prev[i])
        return current
