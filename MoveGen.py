
"""
  Move Object:
  
  (type_of_move, start_pos, end_pos)
  type_of_move:
    1: unknown
    2: safe
    3: capture
    4: check
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
                moves += (self.getPieceLegalMoves(ind))
        return moves

    def getPieceLegalMoves(self, pos):
        boardVal = self.board.boardArr[pos]
        if boardVal == 0:
            return []
        piece = boardVal % 10
        color = 20 if boardVal >= 20 else 10
        if piece == 0:    # pawn
            pass
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
