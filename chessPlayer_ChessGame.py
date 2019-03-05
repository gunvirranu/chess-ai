from chessPlayer_Board import Board
from chessPlayer_MoveGen import MoveGen
from chessPlayer_MoveEval import MoveEval


class ChessGame:

    def __init__(self, player, initBoard=None):
        if player not in (10, 20):
            raise ValueError('Player must be 10 (white) or 20 (black).')
        else:
            self.player = player
        if type(initBoard) == Board:
            self.board = initBoard
        else:
            self.board = Board(initBoard)
        self.moveGen = MoveGen(self.board, self.player)
        self.moveEval = MoveEval(self.moveGen, self.player)

    def makeMove(self, move, checkLegal=False):
        if not move:
            return False
        if checkLegal:
            if move[0] < 0 or move[0] > 64 or move[1] < 0 or move[1] > 64:
                if move not in self.moveGen.getPiecePseudoLegalMoves(move):
                    return False
        self.board.makeMoveForce(move)
        return True

    def getMove(self, maxDepth=None):
        return self.moveEval.getMove(maxDepth=maxDepth)

