

class Node:

    def __init__(self, cost, heuristic_cost, name):
        self.name = name
        self.cost = cost
        self.heuristic_cost = heuristic_cost
        self.neighbours = []

    def addNeighbour(self, node):
        self.neighbours.append(node)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name