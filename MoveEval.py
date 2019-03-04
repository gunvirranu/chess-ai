from MoveGen import MoveGen
from MinMax import MinMax


class MoveEval:

    """
     Pawn:    +0
     Knight:  +1
     Bishop:  +2
     Rook:    +3
     Queen:   +4
     King:    +5
    """

    PIECE_VALUE = [1, 3, 3, 5, 9, 42069]  # lmao

    def __init__(self, moveGen, player):
        self.player = player
        self.moveGen = moveGen
        self.board = self.moveGen.board

    def boardHeuristic(self):
        boardVal = 0
        for ind, val in enumerate(self.board.boardArr):
            if val == 0:
                continue
            boardVal += MoveEval.PIECE_VALUE[val % 10] * (+1 if 0 <= val - self.player <= 5 else -1)
        return boardVal

    # TODO: Write smartBoardHeuristic which uses previous board heuristic and move to quickly calculate new value
    def smartBoardHeuristic(self, currentHeuristic, move):  # Must be BEFORE move is applied
        pass

    def getMove(self, maxDepth=None):
        return MinMax(self, maxDepth).getMove()
