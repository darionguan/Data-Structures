# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #3 - Practical Problems Using Trees
# Application: WWW List Collector
# Description: This is a test driver for the ListCollector class from
#              DarionGuanLab3.py
# File Dependencies: DarionGuanLab3.py
# Time Complexity: O(N)
# Space Complexity: O(N)
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuanLab3.py
# Date: 2/28/23

from DarionGuanLab3 import ListCollector


def driver(test):
    # Read and edit text of HTML to ignore spaces and line breaks
    with open(test, 'r', encoding='utf-8') as infile:
        content = infile.read()
    index = content.splitlines()
    test_string = ''
    for line in index:
        test_string += line.strip()

    parser = ListCollector()
    parser.feed(test_string)
    return parser.getLists()


def main():
    print(driver('lists.html'))


if __name__ == "__main__":
    main()

# Commented out run
"""
/Users/darionguan/PycharmProjects/pythonProject/venv/bin/python /Users/
darionguan/PycharmProjects/pythonProject/Lab#3PracticalProblemsUsingTrees/
demo3_DarionGuan.py 
[['An item', 'Another', 'And another one'], ['Item one', 'Item two', 
'Item three', 'Item four']]

Process finished with exit code 0
"""
