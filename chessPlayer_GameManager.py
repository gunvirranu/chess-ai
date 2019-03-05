from chessPlayer_ChessGame import ChessGame


class TwoPlayerChess:

    def __init__(self):
        self.white = ChessGame(10)
        self.black = ChessGame(20, initBoard=self.white.board)

    def makeWhiteMove(self, move, checkLegal=False):
        return self.white.makeMove(move, checkLegal)

    def makeBlackMove(self, move, checkLegal=False):
        return self.black.makeMove(move, checkLegal)

    def printBoard(self):
        print(self.white)

    def kingStatus(self):  # 0: neither, 1: white king, 2: black king, 3: both kings
        x = 1 if self.white.moveGen.getKingPos() else 0
        y = 2 if self.black.moveGen.getKingPos() else 0
        return x + y

    def printGameStatus(self):
        stat = self.kingStatus()
        if stat == 0:
            print('You done goofed, neither have a king.')
        elif stat == 1:
            print('White won!')
        elif stat == 2:
            print('Black won!')
        else:
            pass


class AIvAIGame(TwoPlayerChess):

    def __init__(self, whiteMaxDepth=None, blackMaxDepth=None):
        super().__init__()
        self.whiteMaxDepth = whiteMaxDepth
        self.blackMaxDepth = blackMaxDepth
        self.count = 0

    def playOneMove(self, printBoards=True):

        move = self.white.getMove(maxDepth=self.whiteMaxDepth)[0]
        if not move:
            return False
        self.makeWhiteMove(move, checkLegal=False)
        if printBoards:
            print(self.white)

        move = self.black.getMove(maxDepth=self.blackMaxDepth)[0]
        if not move:
            return False
        self.makeBlackMove(move, checkLegal=False)
        if printBoards:
            print(self.black)

        self.count += 1
        return True

    def playNMoves(self, n, printBoards=True):
        print('Playing', n, 'rounds:')
        for i in range(n):
            stat = self.playOneMove(printBoards)
            if not stat:
                break
        print('Played', n, 'rounds.')
        self.printGameStatus()

    def playUntilDone(self, printStuff=True):
        sameCount = 0
        last = None
        while self.kingStatus() == 3:
            stat = self.playOneMove(printStuff)
            if not stat:
                break
            # Cycle counter
            new = self.white.moveEval.boardHeuristic()
            if new == last:
                sameCount += 1
            else:
                sameCount = 0
            last = new
            if sameCount >= 20:
                if printStuff: print('Cycle detected!')
                break
        if printStuff:
            self.printGameStatus()
            print('Turns played: ', self.count)

    def playNTimes(self, n):

        winStats = [0, 0]
        for i in range(n):
            print('Currently playing:', i)
            self.playUntilDone(printStuff=False)

            stat = self.kingStatus()
            if stat == 1:
                winStats[0] += 1
            elif stat == 2:
                winStats[1] += 1
            else:
                if self.white.moveEval.boardHeuristic() > self.black.moveEval.boardHeuristic():
                    winStats[0] += 1
                else:
                    winStats[1] += 1

            self.white = ChessGame(10)
            self.black = ChessGame(20, initBoard=self.white.board)

        print('\nWin Count (%) :')
        print('White:', winStats[0], ' (', winStats[0] / n, ')')
        print('Black:', winStats[1], ' (', winStats[1] / n, ')')
        return winStats


class HumanvAIGame(TwoPlayerChess):

    def __init__(self, human, aiMaxDepth=None):
        super().__init__()
        self.human = human
        self.ai = 10 if human == 20 else 20
        self.aiMaxDepth = aiMaxDepth
        self.first = self.human if self.human == 10 else self.ai

    def getHumanMove(self):
        col1, row1 = input('Which piece to move [x y] -> ').split(' ')
        col2, row2 = input('Where to place [x y] -> ').split(' ')
        pos1 = 8 * int(row1) + int(col1)
        pos2 = 8 * int(row2) + int(col2)
        return pos1, pos2

    def play(self):
        while self.kingStatus() == 3:

            print(self.white)
            if self.first == self.human:
                while not self.makeWhiteMove(self.getHumanMove(), checkLegal=True):
                    pass
            else:
                move = self.white.getMove(maxDepth=self.aiMaxDepth)[0]
                self.makeWhiteMove(move)
                print('AI chose move:  ', move[0], '->', move[1])

            print(self.black)
            if self.first == self.ai:
                while not self.makeBlackMove(self.getHumanMove(), checkLegal=True):
                    pass
            else:
                move = self.black.getMove(maxDepth=self.aiMaxDepth)[0]
                self.makeBlackMove(move)
                print('AI chose move:  ', move[0], '->', move[1])

        self.printGameStatus()
