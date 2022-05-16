from game import *
import random

class RandomPlayer(Player):
    def __init__(self, char):
        super().__init__()
        self.char = char

    def choose_action(self, state):
        actions = state.actions(self.char)
        options = len(actions)
        selection = random.randint(0, options-1)
        state.execute(actions[selection])
        return state

class MinimaxPlayer(Player):
    def __init__(self, char):
        super().__init__()
        self.char = char

    def eval(self):
        #assigns value to any final game states
        pass