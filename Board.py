# Connect 4 Game Board

class Board:

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def getWidth():
        return self.width

    def getHeight():
        return self.height

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        for col in range( self.width ):
            s += ' ' + str(col%10)
        s += '\n'
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ Add the game piece ox (either 'X' or 'O') to column col. """
        for i in range(self.height):
            if self.data[i][col] != " ":
                self.data[i-1][col] = ox
                return
        self.data[self.height-1][col] = ox

    def clear(self):
        """ Clear the game board of all game pieces. """
        for row in range(self.height):
            self.data =[" "]*self.width

    def setBoard(self, moveString):
        """ Set the board using an input string representation. """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, col):
        """ Return True if adding a game piece in the given column is
            permitted and return False otherwise. """
        if c < 0 or c >= self.width:
            return False
        elif self.data[0][c] != " ":
            return False
        else:
            return True

    def isFull(self):
        """ Return True if the game board is full and False otherwise. """
        for c in range(self.width):
            if self.allowsMove(c) == True:
                return False
        return True

    def delMove(self, col):
        """ Delete the topmost game piece from the given column. """
        for i in range(self.height):
            if self.data[i][c] != " ":
                self.data[i][c] = " "
                return
    def winsFor(self, ox):
        """ Return True if the game has been won by player ox where ox
            is either 'X' or 'O'. """
        for i in range(self.height):
            for j in range(self.width):
                if inarow_Neast(ox, i, j, self.data, 4) or \
                inarow_Nnortheast(ox, i, j, self.data, 4) or \
                inarow_Nsouth(ox, i, j, self.data, 4) or \
                inarow_Nsoutheast(ox, i, j, self.data, 4):
                    return True
        return False



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
