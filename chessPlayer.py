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
            out += str(8-i) + ' ║ ' + line + ' ║\n'
        out += '  ╚═════════════════╝\n'
        out += '    a b c d e f g h \n'
        return out


game = ChessGame(10)
print(game)
print(game.board)
print(game.moveGen.getAllPlayerMoves())
