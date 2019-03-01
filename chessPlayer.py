from Board import Board


class ChessGame:

    def __init__(self, player, init=None):
        if player not in (10, 20):
            raise ValueError('Player must be 10 (white) or 20 (black).')
        else:
            self.player = player
        self.board = Board(init)

    def printGame(self):
        print()
        print('Gunvir\'s Sick-Ass Chess Game LMAO')
        print('Player:', 'White' if self.player == 10 else 'Black')
        print('  ╔═════════════════╗')
        for i, line in enumerate(self.board.getPrettyBoard()):
            print(i, '║', line, '║')
        print('  ╚═════════════════╝')
        print('    a b c d e f g h ')


game = ChessGame(10)
game.printGame()
