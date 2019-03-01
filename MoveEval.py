from random import choice


class MoveEval:

    def __init__(self, moveGen, player):
        self.player = player
        self.moveGen = moveGen
        self.board = self.moveGen.board

    def boardHeuristic(self):
        return 1

    def getMove(self, moveType='random'):

        # If in check, respond
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
        allMoves = self.moveGen.getPlayerLegalMoves()
        responseMoves = []
        for move in allMoves:
            self.board.makeMoveForce(move)
            newKingHits = self.moveGen.isKingInCheck()
            if not newKingHits:
                responseMoves.append((move, self.boardHeuristic()))
            self.board.undoMove()
        if not responseMoves:
            return None
        return max(responseMoves, key=lambda x: x[1])[0]
