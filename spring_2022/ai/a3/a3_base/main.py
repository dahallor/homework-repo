from agent import *
from game import *
from util import *
from human import *
from connect3 import *
import sys
import pdb




if __name__ == '__main__':
    p1 = sys.argv[1]
    p2 = sys.argv[2]

    match p1:
        case "human":
            p1 = HumanPlayer()
        case "random":
            p1 = RandomPlayer()
        case "minimax":
            p1 = MinimaxPlayer()
        case _:
            raise Exception("Invalid player type, please try again")

    match p2:
        case "human":
            p2 = HumanPlayer()
        case "random":
            p2 = RandomPlayer()
        case "minimax":
            p2 = MinimaxPlayer()
        case _:
            raise Exception("Invalid player type, please try again")



    state = State()
    game = Game(p1, p2)
    game.play(state)

