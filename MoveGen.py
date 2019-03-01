from Board import Board

"""
  Move Object:  
  (start_pos, end_pos)
"""

"""
  White: Offset = 10
  Black: Offset = 20
  
  Pawn:    +0
  Knight:  +1
  Bishop:  +2
  Rook:    +3
  Queen:   +4
  King:    +5
"""


class MoveGen:

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def getAllPlayerMoves(self):
        moves = []
        for ind, val in enumerate(self.board):
            if val == 0:
                continue
            color = 20 if val >= 20 else 10
            if color == self.player:
                moves += self.getPieceLegalMoves(ind)
        return moves

    def getPieceLegalMoves(self, pos):
        boardVal = self.board.boardArr[pos]
        if boardVal == 0:
            return []
        piece = boardVal % 10
        if piece == 0:    # pawn
            return self.genPawnMoves(pos)
        elif piece == 1:  # knight
            pass
        elif piece == 2:  # bishop
            pass
        elif piece == 3:  # rook
            pass
        elif piece == 4:  # queen
            pass
        elif piece == 5:  # king
            pass
        return []

    # row: int(pos/8), col: pos % 8

    def genPawnMoves(self, pos):
        val = self.board.boardArr[pos]
        if val % 10 != 0:
            return []
        color = 20 if val >= 20 else 10
        upDown = -1 if color == 20 else +1
        moves = []
        # TODO: Handle pawn promotion
        if color == 10 and pos >= 48:
            pass
        elif color == 20 and pos < 16:
            pass
        elif self.board.boardArr[pos + 8*upDown] == 0:
            moves.append((pos, pos + 8*upDown))
        # Capture diagonally
        nineMove = pos + 9*upDown
        if (color == 10 and pos % 8 != 7) or (color == 20 and pos % 8 != 0):
            if self.board.boardArr[nineMove] != 0 and not (0 <= self.board.boardArr[nineMove] - color <= 5):
                moves.append((pos, nineMove))
        sevenMove = pos + 7*upDown
        if (color == 10 and pos % 8 != 0) or (color == 20 and pos % 8 != 7):
            if self.board.boardArr[sevenMove] != 0 and not (0 <= self.board.boardArr[sevenMove] - color <= 5):
                moves.append((pos, sevenMove))
        return moves
