

class Node:

    def __init__(self, cost, name, isStart, isGoal):
        self.name = name
        self.cost = cost
        self.heuristic_cost = 0
        self.neighbours = []
        self.isStart = isStart
        self.isGoal = isGoal

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def add_heuristic_cost(self, cost):
        self.heuristic_cost = cost

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name