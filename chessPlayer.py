from GameManager import AIvAIGame, HumanvAIGame
from ChessGame import ChessGame


init = '- - - - - k - - \
        p p - - b r - - \
        - - - - - - - - \
        - - - - - - - P \
        - P - - - P P - \
        - - - - - - - - \
        - - Q K - - - - \
        - - - - - - - -'

game = ChessGame(10, init)
move = game.getMove(maxDepth=4)
# print(game)
# game.makeMove(move[0])
print(game)
# print(move)

# game = AIvAIGame(3, 2)
# game.playUntilDone(printStuff=True)

# game = AIvAIGame(3, 2)
# game.playNTimes(10)

# game = HumanvAIGame(10)
# game.play()
