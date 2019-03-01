from Board import Board

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
            return self.genKnightMoves(pos)
        elif piece == 2:  # bishop
            return self.genBishopMoves(pos)
        elif piece == 3:  # rook
            return self.genRookMoves(pos)
        elif piece == 4:  # queen
            pass
        elif piece == 5:  # king
            pass
        return []

    def genRookMoves(self, pos):
        val = self.board.boardArr[pos]
        if val % 10 != 3: return []
        color = 20 if val >= 20 else 10
        col = pos % 8
        moves = []

        # Up
        onPos = pos + 8
        while onPos // 8 < 8 and self.board.boardArr[onPos] == 0:
            moves.append((pos, onPos))
            onPos += 8
        if onPos // 8 < 8 and not (0 <= self.board.boardArr[onPos] - color <= 5):
            moves.append((pos, onPos))

        # Down
        onPos = pos - 8
        while onPos // 8 >= 0 and self.board.boardArr[onPos] == 0:
            moves.append((pos, onPos))
            onPos -= 8
        if onPos // 8 >= 0 and not (0 <= self.board.boardArr[onPos] - color <= 5):
            moves.append((pos, onPos))

        # Right
        onPos = pos + 1
        while col < onPos % 8 < 8 and self.board.boardArr[onPos] == 0:
            moves.append((pos, onPos))
            onPos += 1
        if col < onPos % 8 < 8 and not (0 <= self.board.boardArr[onPos] - color <= 5):
            moves.append((pos, onPos))

        # Left
        onPos = pos - 1
        while (0 <= onPos % 8 < col) and self.board.boardArr[onPos] == 0:
            moves.append((pos, onPos))
            onPos -= 1
        if 0 <= onPos % 8 < col and not (0 <= self.board.boardArr[onPos] - color <= 5):
            moves.append((pos, onPos))

        return moves

    def genBishopMoves(self, pos):
        val = self.board.boardArr[pos]
        if val % 10 != 2: return []
        color = 20 if val >= 20 else 10
        col = pos % 8
        moves = []

        # Up Right
        onPos = pos + 9
        while onPos // 8 < 8 and col < onPos % 8 < 8 and self.board.boardArr[onPos] == 0:
            moves.append((pos, onPos))
            onPos += 9
        if onPos // 8 < 8 and col < onPos % 8 < 8 and not (0 <= self.board.boardArr[onPos] - color <= 5):
            moves.append((pos, onPos))

        # Up Left
        onPos = pos + 7
        while onPos // 8 < 8 and onPos % 8 < col and self.board.boardArr[onPos] == 0:
            moves.append((pos, onPos))
            onPos += 7
        if onPos // 8 < 8 and onPos % 8 < col and not (0 <= self.board.boardArr[onPos] - color <= 5):
            moves.append((pos, onPos))

        # Down Left
        onPos = pos - 9
        while onPos // 8 >= 0 and onPos % 8 < col and self.board.boardArr[onPos] == 0:
            moves.append((pos, onPos))
            onPos -= 9
        if onPos // 8 >= 0 and onPos % 8 < col and not (0 <= self.board.boardArr[onPos] - color <= 5):
            moves.append((pos, onPos))

        # Down Right
        onPos = pos - 7
        while onPos // 8 >= 0 and col < onPos % 8 < 8 and self.board.boardArr[onPos] == 0:
            moves.append((pos, onPos))
            onPos -= 7
        if onPos // 8 >= 0 and col < onPos % 8 < 8 and not (0 <= self.board.boardArr[onPos] - color <= 5):
            moves.append((pos, onPos))

        return moves

    def genKnightMoves(self, pos):
        val = self.board.boardArr[pos]
        if val % 10 != 1: return []
        color = 20 if val >= 20 else 10
        row, col = pos // 8, pos % 8
        moves = []

        for i, j in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            if 0 <= row+i < 8 and 0 <= col+j < 8:
                if self.board[(row+i, col+j)] == 0 or not (0 <= self.board[(row+i, col+j)] - color <= 5):
                    moves.append((pos, 8*(row+i) + col+j))
        return moves

    def genPawnMoves(self, pos):
        val = self.board.boardArr[pos]
        if val % 10 != 0: return []
        color = 20 if val >= 20 else 10
        upDown = -1 if color == 20 else +1
        moves = []

        # TODO: Handle pawn promotion
        if color == 10 and pos >= 48:
            pass
        elif color == 20 and pos < 16:
            pass
        # Straight capture
        elif self.board.boardArr[pos + 8*upDown] == 0:
            moves.append((pos, pos + 8*upDown))

        # Capture diagonally
        nineMove = pos + 9*upDown
        if (color == 10 and pos % 8 != 7) or (color == 20 and pos % 8 != 0):
            if self.board.boardArr[nineMove] != 0 and not (0 <= self.board.boardArr[nineMove] - color <= 5):
                moves.append((pos, nineMove))
        sevenMove = pos + 7*upDown

        # Capture other diagonal
        if (color == 10 and pos % 8 != 0) or (color == 20 and pos % 8 != 7):
            if self.board.boardArr[sevenMove] != 0 and not (0 <= self.board.boardArr[sevenMove] - color <= 5):
                moves.append((pos, sevenMove))

        return moves
