from node import Node

board = []
width = 0
height = 0

def make_board(content):
    global height
    global width
    global board

    rows = content.split("\n")

    for row in rows:
        height += 1
        temp = []
        for e in list(row):

            if(height == 1):
                width += 1

            node = Node(0,0,e)
       
            temp.append(node)
        board.append(temp)

def make_graph():
    row_count = 0
    for row in board:
        col_count = 0
        for node in row:

            if(row_count == 0 and col_count == 0):
                node.addNeighbour(board[row_count][col_count + 1])
                node.addNeighbour(board[row_count + 1][col_count])

            elif(row_count == 0 and col_count == width-1):
                node.addNeighbour(board[row_count][col_count - 1])
                node.addNeighbour(board[row_count + 1][col_count])

            elif(row_count == height-1 and col_count == 0):
                node.addNeighbour(board[row_count][col_count + 1])
                node.addNeighbour(board[row_count - 1][col_count])

            elif(row_count == height-1 and col_count == width-1):
                node.addNeighbour(board[row_count][col_count - 1])
                node.addNeighbour(board[row_count - 1][col_count])

            elif(row_count == 0):
                node.addNeighbour(board[row_count][col_count - 1])
                node.addNeighbour(board[row_count][col_count + 1])
                node.addNeighbour(board[row_count + 1][col_count])

            elif(row_count == height-1):
                node.addNeighbour(board[row_count][col_count - 1])
                node.addNeighbour(board[row_count][col_count + 1])
                node.addNeighbour(board[row_count - 1][col_count])

            elif(col_count == 0):
                node.addNeighbour(board[row_count][col_count + 1])
                node.addNeighbour(board[row_count + 1][col_count])
                node.addNeighbour(board[row_count - 1][col_count])

            elif(col_count == width-1):
                node.addNeighbour(board[row_count][col_count - 1])
                node.addNeighbour(board[row_count + 1][col_count])
                node.addNeighbour(board[row_count - 1][col_count])
            
            else:
                node.addNeighbour(board[row_count][col_count-1])
                node.addNeighbour(board[row_count][col_count+1])
                node.addNeighbour(board[row_count+1][col_count])
                node.addNeighbour(board[row_count-1][col_count])

            col_count += 1

        row_count += 1


def main():
    f = open("boards/board-1-1.txt", "r")
    content = f.read()
    f.close()
    make_board(content)
    make_graph()
    print(content)


if __name__ == "__main__":
    main()