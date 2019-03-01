from Board import Board
from MoveGen import MoveGen
from MoveEval import MoveEval


class ChessGame:

    def __init__(self, player, init=None):
        if player not in (10, 20):
            raise ValueError('Player must be 10 (white) or 20 (black).')
        else:
            self.player = player
        self.board = Board(init)
        self.moveGen = MoveGen(self.board, self.player)
        self.moveEval = MoveEval(self.moveGen, self.player)

    def __str__(self):
        out = '\n'
        out += 'Gunvir\'s Sick-Ass Chess Game LMAO\n'
        out += 'Player: ' + 'White\n' if self.player == 10 else 'Black\n'
        out += '  ╔═════════════════╗\n'
        for i, line in enumerate(self.board.getPrettyBoard()):
            out += str(7-i) + ' ║ ' + line + ' ║\n'
        out += '  ╚═════════════════╝\n'
        out += '    0 1 2 3 4 5 6 7 \n'
        return out


init = '- - - - - - - - \
        - - - - - - - - \
        - - - - - - - - \
        - - - - - - - - \
        - - - - - - - - \
        - - - - - - - - \
        - - - - - - - - \
        - - - - - - - - '


def versus():
    game1 = ChessGame(10)
    game2 = ChessGame(20)
    i = 0
    while True:
        print(game1)
        move1 = game1.moveEval.goodMove()
        if not move1:
            break
        game1.board.makeMoveForce(move1)
        game2.board.makeMoveForce(move1)
        print(game1)
        move2 = game2.moveEval.goodMove()
        if not move2:
            break
        game2.board.makeMoveForce(move2)
        game1.board.makeMoveForce(move2)
        i += 1
    print('Ran out of moves')
    print(i)


versus()


def playHuman():
    game = ChessGame(20)
    while True:
        print(game)
        while True:
            try:
                col1, row1 = input('Which piece to move [x y] -> ').split(' ')
                col2, row2 = input('Where to place [x y] -> ').split(' ')
                pos1 = 8*int(row1) + int(col1)
                pos2 = 8*int(row2) + int(col2)
                if 0 <= pos1 < 64 and 0 <= pos2 < 64:
                    move = (pos1, pos2)
                    if move in game.moveGen.getPiecePseudoLegalMoves(pos1):
                        break
            except Exception:
                pass
        game.board.makeMoveForce(move)
        print(game)
        move = game.moveEval.goodMove()
        print(move)
        game.board.makeMoveForce(move)
