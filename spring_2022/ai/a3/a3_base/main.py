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
            p1 = HumanPlayer("X")
        case "random":
            p1 = RandomPlayer("X")
        case "minimax":
            p1 = MinimaxPlayer("X")
        case _:
            raise Exception("Invalid player type, please try again")

    match p2:
        case "human":
            p2 = HumanPlayer("O")
        case "random":
            p2 = RandomPlayer("O")
        case "minimax":
            p2 = MinimaxPlayer("O")
        case _:
            raise Exception("Invalid player type, please try again")

    state = State()
    game = Game(p1, p2)
    game.play(state)
    #pdb.set_trace()

