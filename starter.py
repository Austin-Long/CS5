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
        self.data = [[" "]*self.width for row in range(self.height)]

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

class Player:

    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        output = ""
        output += "Player for "+self.symbol+"\n"
        output += "  with tiebreak: " + self.tieRule+"\n"
        output += "  and ply == " + str(self.ply)+"\n"
        return output

    def oppChar(self):
        """ Return the opposite game piece character. """
        if self.symbol == "O": return "X"
        else: return "O"

    def scoreBoard(self, b):
        """ Return the score for the given board b."""
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppChar()):
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self, scores):
        """ Return column number of move based on self.tbt. """

    def scoresFor(self, b):
        """ Return a list of scores for board d, one score for each column
            of the board. """

    def nextMove(self, b):
        """ Takes a board as input and returns the next move for this player
            where a move is a column in which the player should place its
            game piece. """


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
