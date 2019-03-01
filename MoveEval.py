from random import choice


class MoveEval:

    def __init__(self, moveGen, player):
        self.player = player
        self.moveGen = moveGen
        self.board = self.moveGen.board

    def goodMove(self):
        moves = self.moveGen.getAllPlayerMoves()
        if len(moves) == 0:
            return None
        return choice(moves)
