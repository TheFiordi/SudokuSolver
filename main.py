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
    row, col = pos
    
    #check the column

    for i in range(len(board)):
        if (board[i][col] == num and row!= i):
            return False

    #check the line
    for j in range(len(board[0])):
        if(board[row][j] == num and col!=j ):
            return False

    #check the boxx
    square_x = (row//3)*3
    square_y = (col//3)*3

    for i in range(square_x, square_x + 3):
       for j in range(square_y, square_y+ 3):
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




