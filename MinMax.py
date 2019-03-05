import MoveEval
import MoveGen


class MinMax:

    # `MAX_DEPTH` MUST be minimum 2 to handle illegal moves
    DEFAULT_MAX_DEPTH = 4

    def __init__(self, moveEval, maxDepth):
        self.moveEval = moveEval
        self.player = moveEval.player
        self.moveGen = moveEval.moveGen
        self.board = moveEval.board
        self.MAX_DEPTH = maxDepth if maxDepth else MinMax.DEFAULT_MAX_DEPTH
        self.movesEvaluated = 0

        self.opp = 20 if self.player == 10 else 10
        self.oppGen = MoveGen.MoveGen(self.board, self.opp)
        self.oppEval = MoveEval.MoveEval(self.oppGen, self.opp)

    def getMove(self):
        if self.moveGen.isCheckmate():
            return None, None
        currentHeuristic = self.moveEval.boardHeuristic()
        move, score, candidateMoves = self.negamax(depth=0, alpha=-9999999, beta=+9999999, color=1, currentHeuristic=currentHeuristic)
        # Ensure move is legal to prevent AI from killing self lmao
        # TODO: Figure out a better way to do this
        if move not in self.moveGen.getPlayerMoves(legal=True):
            return MinMax(self.moveEval, self.MAX_DEPTH-1).getMove()
        return move, score, candidateMoves

    def negamax(self, depth, alpha, beta, color, currentHeuristic):

        if depth == self.MAX_DEPTH:
            return None, color * currentHeuristic

        gen = self.moveGen if color == 1 else self.oppGen
        moves = gen.getPlayerMoves(legal=False)
        if not moves:
            return None, None

        bestScore = -99999999
        bestMove = None
        moveScores = []

        for move in moves:

            # to prioritize moves now rather than later
            newHeuristic = 0.90 * self.moveEval.smartBoardHeuristic(currentHeuristic, move)

            if self.board.boardArr[move[1]] % 10 == 5:
                negaScore = -color * newHeuristic

            else:
                self.board.makeMoveForce(move)
                negaScore = self.negamax(depth + 1, -beta, -alpha, -color, newHeuristic)[1]
                self.board.undoMove()
                if negaScore is None:
                    continue

            moveScores.append((move, -negaScore))

            bestMove = bestMove if bestScore >= -negaScore else move
            bestScore = max(bestScore, -negaScore)
            alpha = max(alpha, bestScore)
            if alpha > beta:
                break

        if not moveScores:
            return None, None

        if depth == 0:
            # print('# of moves evaluated:', self.movesEvaluated)
            pass
        else:
            moveScores = []

        return bestMove, bestScore, moveScores

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
            print('# of moves evaluated:', self.movesEvaluated)

        return bestMove, bestScore
