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
        root = [None, None]
        root[0] = state.clone()
        selection = self.minimax(root, True)
        state.execute(selection[0])
        return state
        
    def minimax(self, node, isMaxPlayer):
        state = node[0]
        result = self.terminal_test(state)
        #pdb.set_trace()
        if result != None:
            node[1] = result
            return node

        if isMaxPlayer == True:
            maxScore = -math.inf
            node = [state, maxScore]
            actions = state.actions(self.char)
            for i in range(len(actions)):
                clone = state.clone()
                exe = clone.execute(actions[i])
                node[0] = exe
                node[1] = maxScore
                #pdb.set_trace()
                node = self.minimax(node, False)
                score = node[1]
                if score > maxScore:
                    maxScore = score
                    node[0] = exe
                    node[1] = maxScore * self.values["penality"]
            #pdb.set_trace()
            return node


        if isMaxPlayer == False:
            minScore = math.inf
            node = [state, minScore]
            actions = state.actions(self.char)
            for i in range(len(actions)):
                print(i)
                clone = state.clone()
                exe = clone.execute(actions[i])
                node[0] = exe
                node[1] = minScore
                node = self.minimax(node, True)
                score = node[1]
                if score < minScore:
                    minScore = score
                    node[0] = exe
                    node[1] = minScore * self.values["penality"]
            return node

    def terminal_test(self, state):
        #pdb.set_trace()
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


