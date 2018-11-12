#
# hw9pr1.py - Game of Life lab
#
# Name:Austin Long
#

import random
from copy import deepcopy

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """returns a new 2D list of height rows and width columns,
        all data elements are 0"""
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for row in A:               # row is the whole row
        print()
        for col in row:         # col is the individual element
            print(col, end='')  # print that element


def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(w, h):
    """returns a 2D array that has all live cells-with a value of 1-except
       for a one-cell wide border of empty cells around the 2D array"""
    A = createBoard(w, h)

    for row in range(1, h-1):
        for col in range(1, w-1):
            if row == h-1:
                A[row][col] = 0
            elif col == w-1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(w, h):
    """returns an array of randomly assigned 1's and 0's ecept that the oter edge
       of the array is only 0's"""
    A = createBoard(w, h)

    for row in range(1, h-1):
        for col in range(1, w-1):
            if random.choice([0, 1]) == 1:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def copy(A):
    """Returns a Deep copy of the 2D array A"""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width -1):
            newA[row][col] = A[row][col]
    return newA


def innerReverse(A):
    """Returns a copy of A, with the values equal to 1 now equal to 0 and vice versa"""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width -1):
            if A[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    return newA

def countNeighbors(row, col, A):
    """return the number of live neighbors for a cell in the board A at a particular row and col."""
    h = len(A)
    w = len(A[0])
    count = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if abs(x) + abs(y) != 0:
                count += A[row+x][col+y]
    return count

def next_life_generation(A):
    """Makes a copy of A and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
    newA = deepcopy(A)
    height = len(newA)
    width = len(newA[0])

    for row in range(1, height - 1):
        for col in range(1, width -1):
            x = countNeighbors(row, col, A)
            if x < 2 or x > 3:
                newA[row][col] = 0
            elif x == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]
    return newA
