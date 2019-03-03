from MoveGen import MoveGen


class MoveEval:

    """
     Pawn:    +0
     Knight:  +1
     Bishop:  +2
     Rook:    +3
     Queen:   +4
     King:    +5
    """

    PIECE_VALUE = [10, 30, 30, 50, 90, 42069]  # lmao

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

    def minimax(self):
        moves = self.moveGen.getPlayerLegalMoves(legal=False)
        if len(moves) == 0:
            return None
        return None

    def getMove(self, moveType='onelook'):
        if moveType == 'random':
            return self.randomMove()
        elif moveType == 'onelook':
            return self.oneLook()
        elif moveType == 'minimax':
            return self.minimax()
        else:
            raise ValueError("Enter valid move choose type ['random', 'oneLook', 'minimax']")

    def oneLook(self):
        moves = self.moveGen.getPlayerLegalMoves(legal=False)
        if len(moves) == 0:
            return None
        moveVal = [0] * len(moves)
        for i in range(len(moves)):
            self.board.makeMoveForce(moves[i])
            moveVal[i] = self.boardHeuristic()
            self.board.undoMove()
        return moves[moveVal.index(max(moveVal))]

    def randomMove(self):

        # Checkmate opponent king if possible
        pseduoMoves = self.moveGen.getPlayerLegalMoves(legal=False)
        oppGen = MoveGen(self.board, 20 if self.player == 10 else 10)
        kingKillers = [move for move in pseduoMoves if move[1] == oppGen.getKingPos()]
        if kingKillers:
            return kingKillers[0]

        # If King in check, evade
        legalMoves = self.moveGen.getPlayerLegalMoves(legal=True)
        kingHits = self.moveGen.isKingInCheck()
        if kingHits:
            kingPos = self.moveGen.getKingPos()
            if kingPos is None: return None

            responseMoves = []
            for move in legalMoves:
                self.board.makeMoveForce(move)
                if not self.moveGen.isKingInCheck(move[1] if move[0] == kingPos else kingPos):
                    responseMoves.append((move, self.boardHeuristic()))
                self.board.undoMove()
            if not responseMoves:
                return None
            return max(responseMoves, key=lambda x: x[1])[0]

        # Random legal move
        if not legalMoves:
            return None
        from random import randrange
        return legalMoves[randrange(0, len(legalMoves))]
