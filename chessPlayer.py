# from GameManager import AIvAIGame, HumanvAIGame
from ChessGame import ChessGame


def nebuBoardTranslator(nebuBoard):
    goodBoard = []
    for i in range(8):
        goodBoard += nebuBoard[8*i:8*i+8][::-1]
    return goodBoard


def nebuMoveTranslator(move):
    row1 = move[0] // 8
    row2 = move[1] // 8
    col1 = 7 - (move[0] % 8)
    col2 = 7 - (move[1] % 8)
    return [8*row1 + col1, 8*row2 + col2]


def chessPlayer(nebuBoard, player):

    if len(nebuBoard) != 64 or player not in (10, 20):
        return False, None, None, None
    board = nebuBoardTranslator(nebuBoard)

    game = ChessGame(player=player, initBoard=board)
    move, score, candidateMoveTree = game.getMove(maxDepth=4)

    if not move:
        return False, None, None, None
    move = nebuMoveTranslator(move)
    candidateMoveTree = [[nebuMoveTranslator(i[0]), i[1]] for i in candidateMoveTree]

    return [True, move, candidateMoveTree, candidateMoveTree]


# init = 'k - - - - - - - \
#         - - - - - - - R \
#         - R - - - - - - \
#         - - - - - - - - \
#         - - - - - - - - \
#         - - - - - - - - \
#         p - - - - - - - \
#         - p - - - - - K'
#
# game = ChessGame(20, init)
# move = game.getMove()
# print(game)
# game.makeMove(move[0])
# print(game)
# print(move)

# game = AIvAIGame(5, 3)
# game.playUntilDone(printStuff=True)

# game = AIvAIGame(3, 3)
# game.playNTimes(10)

# game = HumanvAIGame(10, 4)
# game.play()
