

class Board:

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

    LETTER = {'-': 00,
              'P': 10, 'N': 11, 'B': 12, 'R': 13, 'Q': 14, 'K': 15,
              'p': 20, 'n': 21, 'b': 22, 'r': 23, 'q': 24, 'k': 25}

    PIECES = {-1: '·', -2: ' ',  # black, white □
              10: '♙', 11: '♘', 12: '♗', 13: '♖', 14: '♕', 15: '♔',  # white
              20: '♟', 21: '♞', 22: '♝', 23: '♜', 24: '♛', 25: '♚'}  # black

    def __init__(self, init='default'):
        if init == 'default' or not init:
            self.boardArr = Board.genDefaultBoard()
        elif init == 'empty':
            self.boardArr = [0] * 64
        elif type(init[0]) is str:
            self.boardArr = Board.convertLetterToBoard(init)
        else:
            self.boardArr = init

    def getPrettyBoard(self):
        out = []
        for i in range(7, -1, -1):
            line = [''] * 8
            for ind, val in enumerate(self.boardArr[8*i:8*i+8]):
                if val == 0:
                    val = -1 if ind % 2 == i % 2 else -2    # -1: black, -2: white
                line[ind] = Board.PIECES[val]
            out.append(' '.join(line))
        return out

    def convertBoardToLetter(self):
        return ''.join([next(key for key, value in Board.LETTER.items() if value == i) for i in self.boardArr])

    def __str__(self):
        out = ''
        for i in range(7, -1, -1):
            out += ' '.join([str(let) if let != 0 else '00' for let in self.boardArr[8*i:8*i+8]]) + '\n'
        return out

    def __iter__(self):
        return iter(self.boardArr)

    def __getitem__(self, item):  # (row, col)
        return self.boardArr[8*item[0] + item[1]]

    def __setitem__(self, key, value):
        self.boardArr[8*key[0] + key[1]] = Board.LETTER[value]

    @staticmethod
    def convertLetterToBoard(letterBoard):
        tmp = [Board.LETTER[i] for i in letterBoard.replace(' ', '')]
        out = []
        for i in range(7, -1, -1):
            out += tmp[8*i:8*i+8]
        return out

    @staticmethod
    def genDefaultBoard():
        return Board.convertLetterToBoard('r n b q k b n r'
                                          'p p p p p p p p'
                                          '- - - - - - - -'
                                          '- - - - - - - -'
                                          '- - - - - - - -'
                                          '- - - - - - - -'
                                          'P P P P P P P P'
                                          'R N B Q K B N R')
