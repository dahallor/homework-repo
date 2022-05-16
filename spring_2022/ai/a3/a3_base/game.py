import sys
import util

class Player:
    def __init__(self, char):
        self.char = char

    def choose_action(self, state, node, tree):
        pass

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play(self, state, node, tree):
        states = []
        while state.game_over() == False:
            state = self.p1.choose_action(state, node, tree)
            states.append(state.clone())
            util.pprint(state)
            if state.winner() != None:
                break
            state = self.p2.choose_action(state, node, tree)
            util.pprint(state)
            states.append(state.clone())
            if state.winner() != None:
                break
        winner = state.winner()
        print("{} Wins!".format(winner))
        util.pprint(states)
        