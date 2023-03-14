# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #5 - Graphs
# Application: Graph Abstract Data Type Representation
# Description: This application implements a graph abstract data type via
#              nodes/vertices.
# File Dependencies: DarionGuanvertex.py, DarionGuangraph.py
# Time Complexity: .addEdge(): O(1)
#                  .addVertex(): O(1)
#                  .getEdges(): O(V+E)
# Space Complexity: .addEdge(): O(1)
#                   .addVertex(): O(1)
#                   .getEdges(): O(V+E)
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuannode.py
# Date: 3/14/23

from DarionGuanvertex import Vertex
from DarionGuangraph import Graph


def driver():
    g = Graph()
    g.addVertex(Vertex('a'))
    g.addVertex(Vertex('b'))
    g.addVertex(Vertex('c'))
    g.addVertex(Vertex('d'))
    g.addVertex(Vertex('e'))
    g.addEdge('a', 'b', 4)
    g.addEdge('a', 'c', 1)
    g.addEdge('b', 'a', 3)
    g.addEdge('b', 'd', 2)
    g.addEdge('c', 'a', 1)
    g.addEdge('c', 'b', 5)
    print(g.getEdges())


def main():
    driver()


if __name__ == "__main__":
    main()

# Commented out run
'''
/Users/darionguan/PycharmProjects/pythonProject/venv/bin/python /Users/
darionguan/PycharmProjects/pythonProject/Lab#5Graphs/demo5_DarionGuan.py 
[('a', 'b', 4), ('a', 'c', 1), ('b', 'a', 3), ('b', 'd', 2), ('c', 'a', 1), 
('c', 'b', 5)]

Process finished with exit code 0

'''