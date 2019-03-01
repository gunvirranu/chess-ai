from Board import Board
from MoveGen import MoveGen


class ChessGame:

    def __init__(self, player, init=None):
        if player not in (10, 20):
            raise ValueError('Player must be 10 (white) or 20 (black).')
        else:
            self.player = player
        self.board = Board(init)
        self.moveGen = MoveGen(self.board, self.player)

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

game = ChessGame(10, init=init)
print(game)
# print(game.board)
moves = game.moveGen.getAllPlayerMoves()
print(moves)
