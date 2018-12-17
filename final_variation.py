# Connect 4 Game Board
# final_variation.py
# Austin Long and Charles Mangum

import random
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

def inarow(row, A):
        """returns true if row is full and false otherwise
        """
        H = len(A)
        W = len(A[0])
        count = 0
        if row < 0 or row > H - 1:
            return False # out of bounds row
            # loop over each location _offset_ i
        for i in range(W):
            if A[i] == 'O' or 'X':
                count += 1

        if count == (W - 1):
            return True
        else:
            return False


class Board:

    def __init__( self, width=6, height=7 ):
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
        for row in range( self.height):
            s += ' '   # add the spacer character
            s+= '|'
            for col in range( self.width ):
                s += self.data[row][col] + ' '
            s += '|' + str(row%10)
            s += '\n'
        return s       # the board is complete, return it

    def addMove(self, row, ox):
        """ Add the game piece ox (either 'X' or 'O') to column col. """
        for j in range(self.width):
            if self.data[row][j] != " ":
                self.data[row][j-1] = ox
                return
        self.data[row][self.width -1] = ox

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

    def allowsMove(self, row):
        """ Return True if adding a game piece in the given row is
            permitted and return False otherwise. """
        if row < 0 or row >= self.height:
            return False
        elif self.data[row][0] != " ":
            return False
        else:
            return True

    def isFull(self):
        """ Return True if the game board is full and False otherwise. """
        for c in range(self.width):
            if self.allowsMove(c) == True:
                return False
        return True

    def delMove(self, row):
        """ leftmost the topmost game piece from the given column. """
        for i in range(self.width):
            if self.data[row][i] != " ":
                self.data[row][i] = " "
                return
    def delRow(self, row):
        """delete row"""
        for i in range(self.width):
             self.data[row][i] = " "
    def moveDown(self):
        for j in range(self.width):
            for j in range(self.width):
                self.data[i][j] = [i-1][j]

    def flip(self):
        """flips the board 180 degrees"""



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

    def playGame(b, px, po):
        """ plays a game of Connect Four
            p1 and p2 are objects of type Player OR
            the string 'human'.
        """

        print("Welcome to Sideways C4 \n")
        nextPieceToMove = "X"
        nextPlayerToMove = px
        while px and po != 'human':
            col = nextPlayerToMove.nextMove(b)

            b.addMove(col, nextPieceToMove)
            print(b)
            if b.winsFor(nextPieceToMove):
                print(nextPieceToMove + ' Wins')
                return
            if nextPieceToMove == "X":
                nextPieceToMove = "O"
            elif nextPieceToMove == "O":
                nextPieceToMove = "X"

            if nextPlayerToMove == px:
                nextPlayerToMove = po
            elif nextPlayerToMove == po:
                nextPlayerToMove = px



        if px == 'human':
            print('You are going to be ' + po.oppChar() + 'Good Luck!')
            player = po.oppChar()
            comp = po.ox
            a = 1
            b = 1
            while a == b:
                users_col = -1
                while not b.allowsMove(users_col):
                    users_col = int(input("Choose a row(" + player +"): "))
                    b.addMove(users_col, player)
                    print(b)

                    if b.allowsMove(users_col) == False:
                        for i in range(b.width):
                            if b.allowsMove(i) == True:
                                users_col = i

                if b.winsFor(player):
                    print("Human gets the Win!")
                    return

                if b.isFull():
                    print('tie')
                    return

                comp_col = -1
                while not b.allowsMove(comp_col):
                    comp_col = po.nextMove(b)

                    b.addMove(comp_col, comp)
                    print("Computer turn")
                    print(b)

                    if b.allowsMove(comp_col) == False:
                        for i in range(b.width):
                            if b.allowsMove(i) == True:
                                comp_col = i

                if b.winsFor(comp):
                    print('The Machine Wins!')
                    return
                if b.isFull():
                    print('tie')
                    return


        elif po == 'human':
            print('You are going to be ' + px.oppChar() + ' Good Luck!')
            player = px.oppChar()
            comp = px.ox

            while 1 == 1:
                users_col = -1
                while not b.allowsMove(users_col):
                    users_col = int(input("Choose a row(" + player +"): "))
                    b.addMove(users_col, player)
                    print(b)

                    if b.allowsMove(users_col) == False:
                        for i in range(b.width):
                            if b.allowsMove(i) == True:
                                users_col = i

                if b.winsFor(player):
                    print("Player " + player + " gets the Win!")
                    return

                if b.isFull():
                    print('tie')
                    return

                comp_col = -1
                while not b.allowsMove(comp_col):
                    comp_col = px.nextMove(b)

                    b.addMove(comp_col, comp)
                    print("Computer turn")
                    print(b)

                    if b.allowsMove(comp_col) == False:
                        for i in range(b.width):
                            if b.allowsMove(i) == True:
                                comp_col = i

                if b.winsFor(comp):
                    print('The Machine Wins!')
                    return
                if b.isFull():
                    print('tie')
                    return


class Player:

    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt.lower()
        self.ply = ply

    def __repr__(self):
        output = ""
        output += "Player for " + self.ox
        output += " with tiebreak: " + self.tbt
        output += " and ply == " + str(self.ply)
        return output

    def oppChar(self):
        """ Return the opposite game piece character. """
        if self.ox == "O":
            return "X"
        else:
            return "O"

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
        max = -10
        for s in scores:
            if s > max:
                max = s
        ls = []
        for i in range(len(scores)):
            if scores[i] == max:
                ls.append(i)
        if self.tbt == "Up":
                return ls[0]
        elif self.tbt == "Down":
                return ls[-1]
        else:
                return random.choice(ls)


    def scoresFor(self, b):
        """ Return a list of scores for board d, one score for each column
            of the board. """
        ls = [self.scoreBoard(b)] * b.height
        for i in range(b.height):
            if b.allowsMove(i) == False:
                ls[i] = -1
            elif self.ply != 0:
                b.addMove(i, self.ox)
                score = self.scoreBoard(b)
                if score == 100.0:
                    ls[i] = 100.0
                else:
                    op = Player(self.oppChar(), self.tbt, self.ply-1)
                    bestOp = max(op.scoresFor(b))
                    ls[i] = 100.0 - bestOp
                b.delMove(i)
        return ls


    def nextMove(self, b):
        """ Takes a board as input and returns the next move for this player
            where a move is a column in which the player should place its
            game piece. """
        scores = self.scoresFor(b)
        return self.tiebreakMove(scores)


    def main():
        """ Human versus AI game.  No code to write here! """
        k = int(input("Enter ply (level from 0 to 5): "))
        px = "human"
        po = Player("O", "LEFT", k)
        b = Board(7, 6)
        playGame(b, px, po)
