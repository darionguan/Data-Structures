# CS3C Advanced Algorithms and Data Structures Using Python
# Lab #5 - Graphs
# Description: Graph Class
# Development Environment: PyCharm 2022.3.1
# Version: Python 3.9
# Solution File: DarionGuannode.py
# Date: 3/14/23

from DarionGuanvertex import Vertex


class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    # Get vertex id identified by parameter
    def getVertex(self, id):
        if id in self.vertDictionary[id]:
            return self.vertDictionary[id]
        else:
            return None

    # Accessor for all vertices of graph
    def getVertices(self):
        return self.vertDictionary.keys()

    # Adds a vertex node to the graph
    def addVertex(self, vertex):
        self.vertDictionary[vertex.id] = vertex
        self.numVertices += 1

    def __contains__(self, id):
        '''
        Overload the in operator to support:
            g = Graph()
            g.add_vertex(Vertex(42))
            42 in g -> True
        '''
        return id in self.vertDictionary

    # Adds a directed weight edge
    def addEdge(self, from_id, to_id, weight=None):
        if from_id not in self.vertDictionary:
            self.addVertex(Vertex(from_id))
        if to_id not in self.vertDictionary:
            self.addVertex(Vertex(to_id))
        self.vertDictionary[from_id].addNeighbor(
            self.vertDictionary[to_id], weight)

    # Sets previous attribute of the current parameter
    def setPrevious(self, current, previous):
        current.setPrevious(previous)

    # Helpers
    # Iterator to access all nodes in graph
    def iterator(self):
        return iter(self.vertDictionary.values())

    # Generates an inclusive list from -> to: weight of all edges in the graph
    def getEdges(self):
        edges = []
        for vertex in self.iterator():
            for neighbor in vertex.getConnections():
                weight = vertex.getWeight(neighbor)
                edges.append((vertex.id, neighbor.id, weight))
        return edges
