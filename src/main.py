from node import Node
import math
from a_star_algorithm import A_star

# A few global variables that we will need in both make_board and make_graph 
board = []
width = 0
height = 0
goal_coor = (0,0)
goal_node = None
start_node = None

def make_board(content):
    global height
    global width
    global board
    global goal_coor
    global goal_node
    global start_node

    # We iterate through our input-file
    # Keeping track of (x,y)-coordinate of each node and saving the height and width of the board
    rows = content.split("\n")
    y_coor = 0
    for row in rows:
        height += 1
        x_coor = 0
        temp = []
        for e in list(row):

            if(height == 1):
                width += 1

            # Creating a nodes correlating with the input-char
            if e == 'A':
                node = Node(0,e,True,False)
                start_node = node
            elif e == 'B':
                goal_coor = (x_coor,y_coor)
                node = Node(1,e,False,True)
                goal_node = node
            elif e == '#':
                node = Node(1000000,e,False,False) # Blocked paths are given the cost 1 million, making them the never-the-best choice
            elif e == 'w':
                node = Node(100,e,False,False)
            elif e == 'm':
                node = Node(50,e,False,False)
            elif e == 'f':
                node = Node(10,e,False,False)
            elif e == 'g':
                node = Node(5,e,False,False)
            elif e == 'r':
                node = Node(1,e,False,False)
            else:
                node = Node(1,e,False,False)

            temp.append(node)
            x_coor += 1
        y_coor += 1
        board.append(temp)

# Simple method to print the board, making sure we can keep see the result
def print_board():
    result = ""

    for row in board:
        for node in row:
            result += str(node)
        result += "\n"
    
    print(result)


def make_graph():
    row_count = 0
    for row in board:
        col_count = 0
        for node in row:
            heur_cost = math.sqrt( ((row_count-goal_coor[1])**2)+((col_count-goal_coor[0])**2) ) # Calculating a heuristic cost based on Euclidian distance
            node.add_heuristic_cost(heur_cost)

            # Giving each node the correct neighbours, in a straigth-forward fashion.
            if(row_count == 0 and col_count == 0):
                node.add_neighbour(board[row_count][col_count + 1])
                node.add_neighbour(board[row_count + 1][col_count])

            elif(row_count == 0 and col_count == width-1):
                node.add_neighbour(board[row_count][col_count - 1])
                node.add_neighbour(board[row_count + 1][col_count])

            elif(row_count == height-1 and col_count == 0):
                node.add_neighbour(board[row_count][col_count + 1])
                node.add_neighbour(board[row_count - 1][col_count])

            elif(row_count == height-1 and col_count == width-1):
                node.add_neighbour(board[row_count][col_count - 1])
                node.add_neighbour(board[row_count - 1][col_count])

            elif(row_count == 0):
                node.add_neighbour(board[row_count][col_count - 1])
                node.add_neighbour(board[row_count][col_count + 1])
                node.add_neighbour(board[row_count + 1][col_count])

            elif(row_count == height-1):
                node.add_neighbour(board[row_count][col_count - 1])
                node.add_neighbour(board[row_count][col_count + 1])
                node.add_neighbour(board[row_count - 1][col_count])

            elif(col_count == 0):
                node.add_neighbour(board[row_count][col_count + 1])
                node.add_neighbour(board[row_count + 1][col_count])
                node.add_neighbour(board[row_count - 1][col_count])

            elif(col_count == width-1):
                node.add_neighbour(board[row_count][col_count - 1])
                node.add_neighbour(board[row_count + 1][col_count])
                node.add_neighbour(board[row_count - 1][col_count])
            
            else:
                node.add_neighbour(board[row_count][col_count-1])
                node.add_neighbour(board[row_count][col_count+1])
                node.add_neighbour(board[row_count+1][col_count])
                node.add_neighbour(board[row_count-1][col_count])

            col_count += 1

        row_count += 1


def main():
    f = open("boards/board-2-4.txt", "r")
    content = f.read()
    f.close()
    make_board(content) # The first step is to create a 2d array with each element being a node
    make_graph() # This step adds heuristic cost and neighbours to each node, effectively creating our graph 
    print_board() # The board is printed before searching for the shortest path
    print("Path length: " + str(A_star(start_node,goal_node))) # Searching for the shortest path and printing the length A-star found
    print_board() # Printing the result board


if __name__ == "__main__":
    main()