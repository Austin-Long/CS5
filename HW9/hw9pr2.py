#
# hw9pr2.py
#
# Name:Austin Long
#

# here is a function for printing 2D arrays
#  (lists-of-lists) of data

import random

def print2d(A):
    """print2d prints a 2D array, A
       as rows and columns
       Argument: A, a 2D list of lists
       Result: None (no return value)
    """
    NR = len(A)
    NC = len(A[0])

    for r in range(NR):      # NR = =numrows
        for c in range(NC):  # NC == numcols
            print(A[r][c], end = ' ')
        print()

    return None  # this is implied anyway,
    # when no return statement is present

# some tests for print2d
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
print("2-row, 3-col A is")
print2d(A)

A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
print("4-row, 2-col A is")
print2d(A)


# create a 2D array from a 1D string
def createA(NR, NC, s):
    """Returns a 2D array with
       NR rows (numrows) and
       NC cols (numcols)
       using the data from s: across the
       first row, then the second, etc.
       only test it with enough data!
    """
    A = []
    for r in range(NR):
        newrow = []
        for c in range(NC):
            newrow += [s[0]] # add that char
            s = s[1:]        # get rid of that first char
        A += [newrow]
    return A

# a couple of tests for createA:
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
newA = createA(2, 3, 'X OOXO')
assert newA == A
print("Is newA == A? Should be True:", newA == A)

A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
newA = createA(4, 2, 'XO XOOOX')
assert newA == A

def inarow_3east(ch, r_start, c_start, A):
    """This should start from r_start and c_start and check for three-in-a-row eastward of element ch, returning True or False"""
    NR = len(A)
    NC = len(A[0])

    if r_start >= NR:
        return False
    if c_start > NC - 3:
        return False

    for i in range(3):
        if A[r_start][c_start + i] != ch:
            return False
    return True

def inarow_3south(ch, r_start, c_start, A):
    """This should start from r_start and c_start and check for three-in-a-row southward of element ch, returning True or False, as appropriate"""
    NR = len(A)
    NC = len(A[0])

    if r_start >= NR - 3: # out of bounds in rows
        return False
    if c_start > NC: # out of bounds in cols
        return False

    for i in range(3):
        if A[r_start + i][c_start] != ch: #check for mismatches
            return False
    return True

def inarow_3southeast(ch, r_start, c_start, A):
    """his should start from r_start and c_start and check for three-in-a-row southeastward of element ch, returning True or False"""
    NR = len(A)
    NC = len(A[0])

    if r_start >= NR - 2: # out of bounds in rows
        return False
    if c_start > NC - 2: # out of bounds in cols
        return False

    for i in range(3):
        if A[r_start + i][c_start + i] != ch: #check for mismatches
            return False
    return True

def inarow_3northeast(ch, r_start, c_start, A):
    """This should start from r_start and c_start and check for three-in-a-row northeastward of element ch, returning True or False"""
    NR = len(A)
    NC = len(A[0])

    if r_start >= NR: # out of bounds in rows
        return False
    if c_start >= NC - 3: # out of bounds in cols
        return False

    for i in range(3):
        if A[r_start - i][c_start - i] != ch: #check for mismatches
            return False
    return True

# tests of inarow_3east
A = createA(3, 4, 'XXOXXXOOOOOO')
#print2d(A)
assert inarow_3east('X', 0, 0, A) == False
assert inarow_3east('O', 2, 1, A) == True
assert inarow_3east('X', 2, 1, A) == False
assert inarow_3east('O', 2, 2, A) == False

# tests of inarow_3south
A = createA(4, 4, 'XXOXXXOXXOO OOOX')
#print2d(A)
assert inarow_3south('X', 0, 0, A) == True
assert inarow_3south('O', 2, 2, A) == False
assert inarow_3south('X', 1, 3, A) == False
assert inarow_3south('O', 42, 42, A) == False

# tests of inarow_3southeast
A = createA(4, 4, 'XOOXXXOXX XOOOOX')
#print2d(A)
assert inarow_3southeast('X', 1, 1, A) == True
assert inarow_3southeast('X', 1, 0, A) == False
assert inarow_3southeast('O', 0, 1, A) == True
assert inarow_3southeast('X', 2, 2, A) == False

# tests of inarow_3northeast
A = createA(4, 4, 'XOXXXXOXXOXOOOOX')
#print2d(A)
assert inarow_3northeast('X', 2, 0, A) == True
assert inarow_3northeast('O', 3, 0, A) == True
assert inarow_3northeast('O', 3, 1, A) == False
assert inarow_3northeast('X', 3, 3, A) == False



def inarow_Neast(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for N-in-a-row eastward of element ch, returning True or False"""
    NR = len(A)
    NC = len(A[0])

    if r_start >= NR:
        return False
    if c_start > NC - N:
        return False

    for i in range(N):
        if A[r_start][c_start + i] != ch:
            return False
    return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for N-in-a-row southward of element ch, returning True or False"""
    NR = len(A)
    NC = len(A[0])

    if r_start > NR - N: # out of bounds in rows
        return False
    if c_start > NC: # out of bounds in cols
        return False

    for i in range(N):
        if A[r_start + i][c_start] != ch: #check for mismatches
            return False
    return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for N-in-a-row southeastward of element ch, returning True or False,"""
    NR = len(A)
    NC = len(A[0])

    if r_start >= NR - (N-1): # out of bounds in rows
        return False
    if c_start >= NC - (N-1): # out of bounds in cols
        return False

    for i in range(N):
        if A[r_start + i][c_start + i] != ch: #check for mismatches
            return False
    return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for N-in-a-row northeastward of element ch, returning True or False"""
    NR = len(A)
    NC = len(A[0])

    if r_start >= NR: # out of bounds in rows
        return False
    if c_start >= NC - (N-1): # out of bounds in cols
        return False

    for i in range(N):
        if A[r_start - i][c_start + i] != ch: #check for mismatches
            return False
    return True


# tests of inarow_Neast
A = createA(5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
# print2d(A)
assert inarow_Neast('O', 1, 1, A, 4) == True
assert inarow_Neast('O', 1, 3, A, 2) == True
assert inarow_Neast('X', 3, 2, A, 4) == False
assert inarow_Neast('O', 4, 0, A, 5) == True


# tests of inarow_Nsouth
A = createA(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
# print2d(A)
assert inarow_Nsouth('X', 0, 0, A, 5) == False
assert inarow_Nsouth('O', 1, 1, A, 4) == True
assert inarow_Nsouth('O', 0, 1, A, 6) == False
assert inarow_Nsouth('X', 4, 3, A, 1) == True


# tests of inarow_Nsoutheast
A = createA(5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX')
# print2d(A)
assert inarow_Nsoutheast('X', 1, 1, A, 4) == True
assert inarow_Nsoutheast('O', 0, 1, A, 3) == False
assert inarow_Nsoutheast('O', 0, 1, A, 2) == True
assert inarow_Nsoutheast('X', 3, 0, A, 2) == False


# tests of inarow_Nnortheast
A = createA(5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX')
# print2d(A)
assert inarow_Nnortheast('X', 4, 0, A, 5) == True
assert inarow_Nnortheast('O', 4, 1, A, 4) == True
assert inarow_Nnortheast('O', 2, 0, A, 2) == False
assert inarow_Nnortheast('X', 0, 3, A, 1) == False
