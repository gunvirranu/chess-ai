

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
                moves += self.getPiecePseudoLegalMoves(ind)
        return moves

    # TODO: Check for legalities such as putting king in check
    def getPiecePseudoLegalMoves(self, pos):
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
            return self.genQueenMoves(pos)
        elif piece == 5:  # king
            return self.genKingMoves(pos)
        else:
            return []

    def isKingInCheck(self):
        pos = None
        for ind in range(64):
            if self.board.boardArr[ind] == 0:
                continue
            if self.board.boardArr[ind] == self.player + 5:  # King found
                pos = ind
                break
        if not pos:
            return None
        # TODO: sketchy king check check
        oppMoveGen = MoveGen(self.board, 20 if self.player == 10 else 10)
        kingHits = [move[0] for move in oppMoveGen.getAllPlayerMoves() if move[1] == pos]
        if kingHits:
            return kingHits
        return None

    def genKingMoves(self, pos):
        val = self.board.boardArr[pos]
        if val % 10 != 5: return []
        color = 20 if val >= 20 else 10
        moves = []

        # Iterate through every possible direction
        for i in (-9, -8, -7, -1, 1, 7, 8, 9):
                if 0 <= (pos+i) // 8 < 8 and 0 <= (pos+i) % 8 < 8:
                    if self.board.boardArr[pos+i] == 0 or not (0 <= self.board.boardArr[pos+i] - color <= 5):
                        moves.append((pos, pos+i))

        return moves

    def genQueenMoves(self, pos):
        val = self.board.boardArr[pos]
        if val % 10 != 4: return []
        color = 20 if val >= 20 else 10
        moves = []

        # Bishop substitution
        self.board.boardArr[pos] = color + 2
        moves += self.genBishopMoves(pos)

        # Rook substitution
        self.board.boardArr[pos] = color + 3
        moves += self.genRookMoves(pos)

        self.board.boardArr[pos] = val
        return moves

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

        # Iterate through all possible knight moves
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
        # Move forward
        elif self.board.boardArr[pos + 8*upDown] == 0:
            moves.append((pos, pos + 8*upDown))

        # Capture diagonally
        nineMove = pos + 9*upDown
        if ((0 <= nineMove < 64) and color == 10 and nineMove % 8 != 7) or (color == 20 and nineMove % 8 != 0):
            if self.board.boardArr[nineMove] != 0 and not (0 <= self.board.boardArr[nineMove] - color <= 5):
                moves.append((pos, nineMove))

        # Capture other diagonal
        sevenMove = pos + 7*upDown
        if ((0 <= nineMove < 64) and color == 10 and sevenMove % 8 != 0) or (color == 20 and sevenMove % 8 != 7):
            if self.board.boardArr[sevenMove] != 0 and not (0 <= self.board.boardArr[sevenMove] - color <= 5):
                moves.append((pos, sevenMove))

        return moves
