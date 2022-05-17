from numpy import Infinity
from game import *
import random
import math
import pdb

class RandomPlayer(Player):
    def __init__(self, char):
        super().__init__(char)

    def choose_action(self, state):
        actions = state.actions(self.char)
        options = len(actions)
        selection = random.randint(0, options-1)
        state.execute(actions[selection])
        return state

class MinimaxPlayer(Player):
    def __init__(self, char):
        super().__init__(char)
        self.values = {
            "win" : 1,
            "tie" : 0,
            "lose" : -1,
            "penality": .75}

    def choose_action(self, state):
        selection = self.minimax(state)
        state.execute(selection)
        return state
        
    def minimax(self, state):
        actions = state.actions(self.char)
        #selection = max(self._min_value(state.clone()))
        for i in range(len(actions)):
            action = actions[i]
            clone = state.clone()
            clone.execute(action)
            pdb.set_trace()
        #return selection

    def _max_value(self, state):
        test = self.terminal_test(state)
        if test != None:
            return test * self.values["penality"]
        else:    
            maxValue = -math.inf

    def _min_value(self, state):
        test = self.terminal_test(state)
        if test != None:
            return test * self.values["penality"]
        else:    
            minValue = math.inf
            clone = state.clone()
            actions = clone.actions()
            for action in actions:
                min(self._max_values)



    def terminal_test(self, state):
        if state.game_over == True:
            winner = state.winner
            if winner == self.char:
                return self.values["win"]
            if (self.char == "X" and winner == "O") or (self.char == "O" and winner == "X"):
                return self.values["lose"]
            else:
                return self.values["tie"]
        else:
            return None


