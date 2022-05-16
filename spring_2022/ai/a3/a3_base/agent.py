from numpy import Infinity
from game import *
import random
import math

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
            self.win : 1,
            self.lose : -1,
            self.tie : 0,
            self.penality: .75}

    def choose_action(self, state, node, tree):
        actions = state.actions(self.char)
        selection = self.eval(state, actions, node, tree)
        state.execute(selection)
        return state
        
    def eval(self, state, actions, node, tree):
        selection = max(self._min_value(state.clone()))
        return selection

    def _max_value(self, state, node, tree):
        pass

    def _min_value(self, state, node, tree):
        test = self.terminal_test(self, state)
        if test != None:
            return test
        else:    
            minValue = math.inf


    def terminal_test(self, state):
        if state.game_over == True:
            winner = state.winner
            if winner == self.char:
                return self.values[self.win]
            if (self.char == "X" and winner == "O") or (self.char == "O" and winner == "X"):
                return self.values[self.lose]
            else:
                return self.values[self.tie]
        else:
            return None

class Node:
    def __init__(self, clone, id = 1, parent_id = None):
        self.clone = clone
        self.id = id
        self.parent_id = parent_id
        self.value = None
        self.data_node = [self.id, self.clone, self.value, self.parent_id]

class Tree:
    def __init__(self):
        self.tree = []

    def addToTree(self, data_node):
        self.tree.append(data_node)

    def clearTree(self):
        self.tree = []
