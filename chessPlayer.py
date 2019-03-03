from GameManager import AIvAIGame, HumanvAIGame
from ChessGame import ChessGame


init = '- K - - - - - - \
        - - - - - - - - \
        - - - - - - - - \
        - - - - - - - - \
        - - - - - - - - \
        - - B - - - - - \
        - r - R - - - - \
        k - - - - - - -'

game = ChessGame(20, init)
print(game)
move = game.getMove()
print(move)

# game = AIvAIGame()
# game.playUntilDone()

# game = AIvAIGame()
# game.playNTimes(100)

# game = HumanvAIGame(10)
# game.play()
