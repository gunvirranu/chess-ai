from random import choice


class MoveEval:

    def __init__(self, moveGen, player):
        self.player = player
        self.moveGen = moveGen
        self.board = self.moveGen.board

    def boardHeuristic(self):
        return 1

    def getMove(self, moveType='random'):

        # If King in check, respond
        kingHits = self.moveGen.isKingInCheck()
        if kingHits:
            return self.kingCheckResponse()

        moves = self.moveGen.getPlayerLegalMoves()
        if len(moves) == 0:
            return None

        # TODO: Choose better move
        if moveType == 'random':
            return choice(moves)
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
