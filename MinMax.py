import MoveEval


class MinMax:

    # `MAX_DEPTH` MUST be minimum 2 to handle illegal moves

    DEFAULT_MAX_DEPTH = 3

    def __init__(self, moveEval, maxDepth):
        self.moveEval = moveEval
        self.player = moveEval.player
        self.moveGen = moveEval.moveGen
        self.board = moveEval.board
        self.MAX_DEPTH = maxDepth if maxDepth else MinMax.DEFAULT_MAX_DEPTH
        self.movesEvaluated = 0

        self.opp = 20 if self.player == 10 else 10
        self.oppGen = MoveEval.MoveGen(self.board, self.opp)
        self.oppEval = MoveEval.MoveEval(self.oppGen, self.opp)

    def getMove(self):
        if self.moveGen.isCheckmate():
            return None, None
        return self.minMaxRecursor(depth=0)

    def minMaxRecursor(self, depth):

        if depth == self.MAX_DEPTH:
            return None, self.moveEval.boardHeuristic()

        if depth % 2 == 0:
            moves = self.moveGen.getPlayerMoves(legal=False)
        else:
            moves = self.oppGen.getPlayerMoves(legal=False)
        if not moves:
            return None, None

        self.movesEvaluated += len(moves)
        moveScores = []
        for move in moves:

            if self.board.boardArr[move[1]] % 10 == 5:
                kingKillFlag = True
            else:
                kingKillFlag = False

            self.board.makeMoveForce(move)
            downMove, score = self.minMaxRecursor(depth=(depth+1 if not kingKillFlag else self.MAX_DEPTH))
            self.board.undoMove()
            if score is not None:
                moveScores.append((move, score))

        if not moveScores:
            return None, None
        if depth % 2 == 0:
            bestMove, bestScore = max(moveScores, key=lambda x: x[1])
        else:
            bestMove, bestScore = min(moveScores, key=lambda x: x[1])

        if depth == 0:
            print(moveScores)
            print('# of moves evaluated:', self.movesEvaluated)

        return bestMove, bestScore
