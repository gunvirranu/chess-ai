from random import choice


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

    def minimax(self, moves):
        return None

    def oneLook(self, moves):
        moveVal = [0] * len(moves)
        for i in range(len(moves)):
            self.board.makeMoveForce(moves[i])
            # TODO: Can cache board heuristic as the only values changed are the ones moved
            moveVal[i] = self.boardHeuristic()
            self.board.undoMove()
        return moves[moveVal.index(max(moveVal))]

    def randomMove(self, moves):
        # TODO: Random move does NOT take a win if possible
        # If King in check, respond
        kingHits = self.moveGen.isKingInCheck()
        if kingHits:
            return self.kingCheckResponse()
        return choice(moves)

    def getMove(self, moveType='oneLook'):

        moves = self.moveGen.getPlayerLegalMoves()
        if len(moves) == 0:
            return None

        # TODO: Choose better move
        if moveType == 'random':
            return self.randomMove(moves)
        elif moveType == 'oneLook':
            return self.oneLook(moves)
        elif moveType == 'minimax':
            return self.minimax(moves)
        else:
            raise ValueError("Enter valid move choose type")

    def kingCheckResponse(self):
        kingPos = self.moveGen.getKingPos()
        if not kingPos: return None
        allMoves = self.moveGen.getPlayerLegalMoves()
        responseMoves = []
        for move in allMoves:
            self.board.makeMoveForce(move)
            if not self.moveGen.isKingInCheck(move[1] if move[0] == kingPos else kingPos):
                responseMoves.append((move, self.boardHeuristic()))
            self.board.undoMove()
        if not responseMoves:
            return None
        return max(responseMoves, key=lambda x: x[1])[0]
