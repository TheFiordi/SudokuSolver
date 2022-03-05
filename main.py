
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(board):
    #solves using backtracking

    pos = findEmpty(board)

    if not pos:
        return True
    else:
        row, col = pos

    for i in range(1, len(board[0])+1):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0 #if it can't find a solution it reset the previous step
    return False



def valid(board, num, pos):
    #check the column
    for i in range(len(board)):
        if (board[i][pos[1]] == num and pos[1]!= i):
            return False

    #check the line
    for j in range(len(board[0])):
        if(board[pos[0]][j] == num and pos[0]!=j ):
            return False

    #check the boxx
    square_x = pos[0] // 3
    square_y = pos[1] // 3

    for i in range(square_x*3, square_x*3 + 3):
       for j in range(square_y * 3, square_y*3 + 3):
           if board[i][j] == num and (i,j) != pos:
               return False

    return True


def print_board(board):

    print()
    for i in range(len(board)):

        if(i % 3 == 0 and i!=0):
            print("--------------------")

        for j in range(len(board[0])):
            if(j % 3 == 0 and j != 0):
                print("|", end="")
            print(board[i][j], end=" ")
        print()

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None


print_board(board)
solve(board)
print_board(board)







