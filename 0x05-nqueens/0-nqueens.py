#!/usr/bin/python3
""" N queens problem """
import sys

global n, solutions
solutions = []
n = 0
def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                
                solutions.append([i, j])
    print(solutions)

def createTemplate(n):
    board = []
    for c in range(n):
        board.append(['' for i in range(n)])
    if nqueens(board, 0) == False:
        print("Solution does not exist")
        return False
 
    printSolution(board, n)
    return True


def nqueens(board, col):
    if col >= n:
        return True
 
    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):
 
        if isSafe(board, i, col):
 
            # Place this queen in board[i][col]
            board[i][col] = 1
 
            # Recur to place rest of the queens
            if nqueens(board, col + 1) == True:
                return True
 
            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0
 
    # If the queen can not be placed in any row in
    # this column col then return false
    return False


def isSafe(board, row, col):
    """check if the queen is safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens n')
        exit(1)
    
    try:
        stdNumber = int(sys.argv[1])
        if type(int) == int or float:
            if stdNumber < 4:
                print('N must be at least 4')
                exit(1)
            n = stdNumber
            createTemplate(n)
    except ValueError:
        print('N must be a number')
        exit(1)
