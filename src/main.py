from GameManager import AIvAIGame, HumanvAIGame


if __name__ == '__main__':

    # Can pass an (optional) initial board configuration to GameManager
    # init = '- - - - - k - - \
    #         p p - - b r - - \
    #         - - - - - - - - \
    #         - - - - - - - P \
    #         - P - - - P P - \
    #         - - - - - - - - \
    #         - - Q K - - - - \
    #         - - - - - - - -'

    # Arguments are `difficult` (actually max-depth of game tree lookahead)
    # game = AIvAIGame(4, 5)
    # game.playUntilDone(printStuff=True)

    # game = AIvAIGame(3, 2)
    # game.playNTimes(10)     # Warning, this can take a very long time

    # 10 : white, 20 : black
    game = HumanvAIGame(10, aiMaxDepth=4)
    game.play()

