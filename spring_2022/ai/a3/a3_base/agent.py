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
        self.id = 1
        self.values = {
            "win" : 1,
            "tie" : 0,
            "lose" : -1,
            "penality": .75}

    def choose_action(self, state):
        tree = Tree()
        clone = state.clone()
        root = Node(self.id, clone, None, None)
        root = root.createNode()
        tree.addToTree(root)
        selection = self.minimax(root, tree)
        state.execute(selection)
        return state
        
    def minimax(self, root, tree):
        root_state = root[1]
        actions = root_state.actions(self.char)
        for i in range(len(actions)):
            action = actions[i]
            clone = root_state.clone()
            new = clone.execute(action)
            self.id += 1
            node = Node(self.id, new, None, root[0])
            node = node.createNode()
            tree.addToTree(node)
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


class Tree:
    def __init__(self):
        self.tree = []

    def clearTree(self):
        self.tree =[]

    def addToTree(self, node):
        self.tree.append(node)



class Node:
    def __init__(self, id, state, value, parent_id):
        self.id = id
        self.parent_id = parent_id
        self.state = state
        self.value = value

    def createNode(self):
        data_node = [self.id, self.state, self.value, self.parent_id]
        return data_node

