
import time
import random
from main import valid

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]




list = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]

def isSolutionUnique(i, j, board, count):
    if(i==9):
        i=0
        j=j+1
        if(j ==9):
            return count+1

    if board[i][j] != 0:
        return isSolutionUnique(i+1, j, board, count)

    for num in range(1, 10):
        if(count >=2 ):
            break
        if valid(board, num, (i, j)):
            board[i][j] = num
            count = isSolutionUnique(i+1,j,board, count)
    
    board[i][j] = 0
    return count

def createSeed(row, col, board):
    
    if(row==9):
        row=0
        col=col+1
        if(col ==9):
            return True
    
    if(board[row][col] !=0):
        createSeed(row+1,col,board)    
    
    numbers = [1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)

    for num in numbers:
        if valid(board,num, (row, col)):
            board[row][col] = num  
            if createSeed(row+1, col, board):
                return True
    else:            
        board[row][col] = 0
        return False


def createBoard(board):
    random.shuffle(list)
    difficulty = random.randint(55,64)
    
    for i in range(0, difficulty):
        prev = board[list[i][0]][list[i][1]] 
        board[list[i][0]][list[i][1]] = 0
        if isSolutionUnique(0,0,board,0)>1:
            board[list[i][0]][list[i][1]] = prev

