from random import choice


class MoveEval:

    def __init__(self, moveGen, player):
        self.player = player
        self.moveGen = moveGen
        self.board = self.moveGen.board

    def boardHeuristic(self):
        return 1

    def goodMove(self):

        # If in check, respond
        kingHits = self.moveGen.isKingInCheck()
        if kingHits:
            print('IN CHECK')
            return self.kingCheckResponse()

        # TODO: Choose better move
        moves = self.moveGen.getAllPlayerMoves()
        if len(moves) == 0:
            return None
        return choice(moves)

    def kingCheckResponse(self):
        allMoves = self.moveGen.getAllPlayerMoves()
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
