# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #4 - Binary Trees
# Application: Finding MAX in Binary Trees
# Description: This is a test driver for the BinaryTree class from
#              DarionGuanLab4.py
# File Dependencies: DarionGuanLab4.py
# Time Complexity (of .findmax()): O(N)
# Space Complexity (of .findmax()): O(N)
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuanLab4.py
# Date: 3/7/2023

from DarionGuanLab4 import BinaryTree


def driver():
    r = BinaryTree(3)
    r.insert_left(2)
    r.leftChild.insert_left(1)
    r.insert_right(5)
    r.rightChild.insert_left(4)
    r.rightChild.insert_right(6)
    r.rightChild.rightChild.insert_right(7)

    print('Preorder traversal:')
    r.preorder()
    print('Inorder traversal:')
    r.inorder()
    print('Postorder traversal:')
    r.postorder()
    print('Max node:')
    print(r.find_max())
    print('Size:')
    print(r.size())
    print('Height:')
    print(r.height())


def main():
    driver()


if __name__ == "__main__":
    main()

# Commented out run
'''
/Users/darionguan/PycharmProjects/pythonProject/venv/bin/python /Users/
darionguan/PycharmProjects/pythonProject/Lab#4BinaryTree/demo4_DarionGuan.py 
Preorder traversal:
3
2
1
5
4
6
7
Inorder traversal:
1
2
3
4
5
6
7
Postorder traversal:
1
2
4
7
6
5
3
Max node:
7
Size:
7
Height:
3

Process finished with exit code 0
'''