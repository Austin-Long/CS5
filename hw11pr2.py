#
# hw11pr2.py
#
# Name: Austin Long
#
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

    def emptyLeft(self, a, b):
        """returns True if the calling object has an open cell to the left of a,b
           Returns False if a,b is not a legal column number, and if a,b is occupied
        """
        if b-1 < 0 or b >= self.width:
            return False
        if a < 0 or a >= self.height:
            return False
        elif self.data[a][b-1] != " ":
            return False
        else:
            return True

    def emptyRight(self, a, b):
        """returns True if the calling object has an open cell to the right of a,b
           Returns False if a,b is not a legal column number, and if a,b is occupied
        """
        if b < 0 or b+1 >= self.width:
            return False
        if a < 0 or a >= self.height:
            return False
        elif self.data[a][b+1] != " ":
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


    def colsToWin(self,ox):
        """takes one argument a string ox, returns a list of columns where ox can
           move in the next turn in order to win and finish the game
        """
        lt = []
        for i in range(self.width):
            if self.allowsMove(i):
                self.addMove(i, ox)
                if self.winsFor(ox):
                    lt += [i]
                self.delMove(i)
        return lt

    def aiMove(self,ox):
        """accepts a single argument, ox
           returns a single integer, which must be a legal column:
           If there is a way for ox to win, then aiMove MUST return
           that move (that column number). It must win when it can.
           There may be more than one way to win: in this case, any one of those winning
           column moves may be returned.
           If there is NO way for ox to win, but there IS a way for ox to block the opponent's
           four-in-a-row, then aiMove MUST return a move that blocks its opponent's
           four-in-a-row. Again, it should not look more than one move ahead for its opponent.
           If there are no wins, but multiple ways to block the opponent, then aiMove should return
           any one of those ways to block the opponent. (Even though the opponent might win in a different way.)
           If there is NO way for ox to win NOR a way for ox to block the opponent
           from winning, then aiMove should return a move of your (the programmer's)
           choice—but it must be a legal move. We won't call aiMove when the board is full.
        """
        if ox == 'X':
          if self.colsToWin('X') != []:         #Win
              return random.choice(self.colsToWin('X'))
          else:         # You can not win
              if self.colsToWin('O') != []:  # Check if your opponent can win and block!
                  return random.choice(self.colsToWin('O'))
              else: # No one can win
                  for i in range(self.height):  #Check for two in a row (spaces on each side) and place move to the right
                      for j in range(self.width):
                          if inarow_Neast('O', i, j, self.data, 2) and self.emptyLeft(i,j) and self.emptyRight(i,j+1):
                              return j+2

                  if self.allowsMove(3):     # Go in middle column
                      return 3
                  elif self.allowsMove(2):
                      return 2
                  elif self.allowsMove(4):
                      return 4
                  elif self.allowsMove(5):
                      return 5
                  elif self.allowsMove(1):
                      return 1
                  elif self.allowsMove(0):
                      return 0
                  elif self.allowsMove(6):
                      return 6

        elif ox == 'O':
          if self.colsToWin('O') != []:         #Win
              return random.choice(self.colsToWin('O'))
          else:         # You can not win
              if self.colsToWin('X') != []:  # Check if your opponent can win and block!
                  return random.choice(self.colsToWin('X'))
              else: # No one can win
                  for i in range(self.height):  #Check for two in a row and place checker to the right
                      for j in range(self.width):
                          if inarow_Neast('X', i, j, self.data, 2) and self.emptyLeft(i,j) and self.emptyRight(i,j+1):
                              return j+2

                  if self.allowsMove(3):     # Go in middle column
                      return 3
                  elif self.allowsMove(2):
                      return 2
                  elif self.allowsMove(4):
                      return 4
                  elif self.allowsMove(5):
                      return 5
                  elif self.allowsMove(1):
                      return 1
                  elif self.allowsMove(0):
                      return 0
                  elif self.allowsMove(6):
                      return 6




    def hostGame(self):
        """hosts a game of connect for, 'X' will always go first"""
        print("Welcome to Connect Four! \n")
        print(self)
        player = input('Would you like to be \'X\' or \'O\'?')
        player = player.upper()
        if player == 'X':
            comp = 'O'
        elif player == 'O':
            comp = 'X'
        a = 1
        b = 1
        while a == b:
            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("Choose a column(" + player +"): "))
                self.addMove(users_col, player)
                print(self)

                if self.allowsMove(users_col) == False:
                    for i in range(self.width):
                        if self.allowsMove(i) == True:
                            users_col = i

            if self.winsFor(player):
                print("Player " + player + " gets the Win!")
                return

            if self.isFull():
                print('tie')
                return

            comp_col = -1
            while not self.allowsMove(comp_col):
                comp_col = self.aiMove(comp)

                self.addMove(comp_col, comp)
                print("Computer turn")
                print(self)

                if self.allowsMove(comp_col) == False:
                    for i in range(self.width):
                        if self.allowsMove(i) == True:
                            comp_col = i

            if self.winsFor(comp):
                print('The Machine Wins!')
                return
            if self.isFull():
                print('tie')
                return
