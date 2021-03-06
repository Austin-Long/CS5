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
