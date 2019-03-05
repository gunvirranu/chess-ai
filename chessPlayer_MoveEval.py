import chessPlayer_MinMax


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
            boardVal += self.getPosHeuristicVal(pos=ind, val=val)
        return boardVal

    def getPosHeuristicVal(self, pos, val):
        if val == 0:
            return 0
        pieceVal = self.PIECE_VALUE[val % 10]
        side = +1 if 0 <= val - self.player <= 5 else -1
        if val == 15:
            posVal = self.KING_EVAL_WHITE[pos]
        elif val == 25:
            posVal = self.KING_EVAL_BLACK[pos]
        elif val % 10 == 4:
            posVal = self.QUEEN_EVAL[pos]
        elif val == 13:
            posVal = self.ROOK_EVAL_WHITE[pos]
        elif val == 23:
            posVal = self.KING_EVAL_BLACK[pos]
        elif val == 12:
            posVal = self.BISHOP_EVAL_WHITE[pos]
        elif val == 23:
            posVal = self.BISHOP_EVAL_BLACK[pos]
        elif val % 10 == 1:
            posVal = self.KNIGHT_EVAL[pos]
        elif val == 10:
            posVal = self.PAWN_EVAL_WHITE[pos]
        elif val == 20:
            posVal = self.PAWN_EVAL_BLACK[pos]
        else:
            posVal = 0
        return (pieceVal + posVal) * side

    def smartBoardHeuristic(self, currentHeuristic, move):  # Must be BEFORE move is applied
        movePiece = self.board.boardArr[move[0]]
        landPiece = self.board.boardArr[move[1]]
        # Remove value from piece about to be moved
        currentHeuristic -= self.getPosHeuristicVal(pos=move[0], val=movePiece)
        # Remove value from piece that gets landed on
        if landPiece != 0:
            currentHeuristic -= self.getPosHeuristicVal(pos=move[1], val=landPiece)
        # Add value from piece that gets moved to new spot
        currentHeuristic += self.getPosHeuristicVal(pos=move[1], val=movePiece)
        return currentHeuristic

    def getMove(self, maxDepth=None):
        return chessPlayer_MinMax.MinMax(self, maxDepth).getMove()

    KING_EVAL_WHITE = [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0, -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0]

    KING_EVAL_BLACK = [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0, -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]

    QUEEN_EVAL = [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0, -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5, -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0, -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0, -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]

    ROOK_EVAL_WHITE = [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    ROOK_EVAL_BLACK = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]

    BISHOP_EVAL_WHITE = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0, -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0, -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0, -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

    BISHOP_EVAL_BLACK = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0, -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0, -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0, -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

    KNIGHT_EVAL = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0, -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0, -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0, -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0, -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0, -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0, -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0, -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]

    PAWN_EVAL_WHITE = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, 0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5, 0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, 1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    PAWN_EVAL_BLACK = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, 0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, 0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5, 0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
