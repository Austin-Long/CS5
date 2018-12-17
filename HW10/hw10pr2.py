#
# hw10pr2.py
#
# Name: Austin Long
#
def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """Drops a check into the board, accepts two arguments:
           the col and the one character string 'X' or 'O'
        """
        for i in range(self.height):
            if self.data[i][col] != " ":
                self.data[i-1][col] = ox
                return
        self.data[self.height-1][col] = ox

    def clear(self):
        """clears the board that calls it"""
        for row in range(self.height):
            self.data =[" "]*self.width

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        """returns True if the calling object does allow a move into column c
           Returns False if c is not a legal column number, and if c is full
        """
        if c < 0 or c >= self.width:
            return False
        elif self.data[0][c] != " ":
            return False
        else:
            return True

    def isFull(self):
        """returns True if the calling object is completely full of checkers. False
           otherwise
        """
        for c in range(self.width):
            if self.allowsMove(c) == True:
                return False
        return True

    def delMove(self, c):
        """removes the top checker from the column c, if the column is empty, then
           do nothing
        """
        for i in range(self.height):
            if self.data[i][c] != " ":
                self.data[i][c] = " "
                return

    def winsFor(self, ox):
        """returns True if there are four checkers of type ox in a row on the
           board, False otherwise
           Accepts: a 1-character checker, either 'O' or 'X'
        """
        for i in range(self.height):
            for j in range(self.width):
                if inarow_Neast(ox, i, j, self.data, 4) or \
                inarow_Nnortheast(ox, i, j, self.data, 4) or \
                inarow_Nsouth(ox, i, j, self.data, 4) or \
                inarow_Nsoutheast(ox, i, j, self.data, 4):
                    return True
        return False

    def hostGame(self):
        """hosts a game of connect for, 'X' will always go first"""
        print("Welcome to Connect Four! \n")
        print(self)
        a = 1
        b = 1
        while a == b:
            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("Choose a column(X): "))

            self.addMove(users_col, 'X')
            print(self)

            if self.winsFor('X'):
                 print("Player X gets the Win!")
                 return

            if self.isFull():
                print('tie')
                return

            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("Choose a column(O): "))

            self.addMove(users_col, 'O')
            print(self)

            if self.winsFor('O'):
                print('Player O Wins!')
                return
            if self.isFull():
                print('tie')
                return
