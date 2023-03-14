# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #5 - Graphs
# Description: Vertex Class
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuannode.py
# Date: 3/14/23

class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}
        self.visited = False
        self.previous = None
        self.distance = None

    # Vertex id accessor
    def getVertexID(self):
        return self.id

    # Vertex weight accessor
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    # Distance accessor
    def getDistance(self):
        if self.previous is None:
            # The distance to first vertex is 0
            return 0
        else:
            queue = [self]
            distance = 0
            while len(queue) > 0:
                vertex = queue.pop(0)
                for neighbor in vertex.adjacent:
                    if not neighbor.visited:
                        neighbor.visited = True
                        neighbor.previous = vertex
                        queue.append(neighbor)
                        if neighbor == self.previous:
                            # Found previous vertex, return the distance
                            return distance + 1
                distance += 1

    # Vertex connections accessor
    def getConnections(self):
        return self.adjacent.keys()

    # Set distance attribute
    def setDistance(self, distance):
        self.distance = distance

    # Set previous attribute
    def setPrevious(self, id):
        self.previous = id

    # Adds vertex neighbor id and weight into adjacency list
    def addNeighbor(self, neighbor, weight=None):
        self.adjacent[neighbor] = weight

    # Helpers:
    # Return vertex string representation
    def __str__(self):
        return '{} neighbors: {}'.format(
            self.id, [x.id for x in self.adjacent])
