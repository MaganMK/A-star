
from node import Node

def A_star(start_node, goal_node):
    evaluated_nodes = [] # Nodes we have evaluated and are done with

    discovered_nodes = [] # Nodes we have found, but not evaluated yet. When this set is empty we are done
    discovered_nodes.append(start_node)

    # Keeping track of the node each node came from. This is updated as we find a better path
    came_from = {}

    # The cost from start node to current node
    g_scores = {}
    g_scores[start_node] = 0

    # The sum of g_score and the heuristic cost of current node
    f_scores = {}
    f_scores[start_node] = start_node.heuristic_cost


    while discovered_nodes:
        current = find_lowest_f_score(discovered_nodes,f_scores) # Whe evaluate the node with lowest f_score (essentially our best bet so far)

        if current.isGoal: # We are done
            return reconstruct_path(came_from,current)

        # The node is no longer just a discovered node, it is evaluated
        discovered_nodes.remove(current)
        evaluated_nodes.append(current)

        # We discover the neighbours of the current node
        for neighbour in current.neighbours:
            
            # If it is already evaluated, we have already discovered it 
            if neighbour in evaluated_nodes:
                continue
            
            # The g_score of each neighbour, based on the path from our current node
            tent_g_score = g_scores[current] + neighbour.cost

            if neighbour not in discovered_nodes: # We have found a new node
                discovered_nodes.append(neighbour)
            elif tent_g_score >= g_scores[neighbour]: # The node has been found before and our new g_score is not better 
                continue
            
            # The path is the best for now
            came_from[neighbour] = current
            g_scores[neighbour] = tent_g_score
            f_scores[neighbour] = g_scores[neighbour] + neighbour.heuristic_cost


# Looking at where each node came from, changing the node to "+" to represent it as a node in out best path
def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
        if current.name != 'A':
            current.name = "+"

    return len(path)

# Method for finding the our best option thus far
def find_lowest_f_score(nodes, f_scores):
    result = nodes[0]
    
    for node in nodes:

        if(f_scores[node] < f_scores[result]):
            result = node
    
    return result