
from node import Node

def A_star(start_node, goal_node):
    evaluated_nodes = []

    discovered_nodes = []
    discovered_nodes.append(start_node)

    came_from = {}

    g_scores = {}
    g_scores[start_node] = 0

    f_scores = {}
    f_scores[start_node] = start_node.heuristic_cost

    while discovered_nodes:
        current = find_lowest_f_score(discovered_nodes,f_scores)

        if current.isGoal:
            return reconstruct_path(came_from,current)

        discovered_nodes.remove(current)
        evaluated_nodes.append(current)

        for neighbour in current.neighbours:
            if neighbour in evaluated_nodes:
                continue
            
            tent_g_score = g_scores[current] + neighbour.cost

            if neighbour not in discovered_nodes:
                discovered_nodes.append(neighbour)
            elif tent_g_score >= g_scores[neighbour]:
                continue
            
            came_from[neighbour] = current
            g_scores[neighbour] = tent_g_score
            f_scores[neighbour] = g_scores[neighbour] + neighbour.heuristic_cost


def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
        if current.name != 'A':
            current.name = "o"

    return len(path)

def find_lowest_f_score(nodes, f_scores):
    result = nodes[0]
    
    for node in nodes:

        if(f_scores[node] < f_scores[result]):
            result = node
    
    return result