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
        root = Node(1, state.clone(), None, None)
        tree = Tree()
        tree.addToTree(root.data)
        player_sym = self.char
        if player_sym == "X":
            opponent_sym = "O"
        else:
            opponent_sym = "X"
        selection = self.minimax(root, tree, player_sym, opponent_sym, True)
        pdb.set_trace()
        state.execute(selection.data[1])
        return state
        
    def minimax(self, node, tree, player_sym, opponent_sym, isMaxPlayer):
        result = self.terminal_test(node)
        #pdb.set_trace()
        if result != None:
            node.data[2] = result
            return node

        if isMaxPlayer == True:
            maxScore = -math.inf
            state = node.data[1]
            actions = state.actions(player_sym)
            parent_id = node.data[0]
            id = parent_id + 1
            branch = []
            for i in range(len(actions)):
                clone = state.clone()
                exe = clone.execute(actions[i])
                node = Node(id, exe, None, parent_id)
                tree.addToTree(node.data)
                branch.append(node)
                id += 1
            #pdb.set_trace()
            for i in range(len(branch)):
                current_node = branch[i]
                node = self.minimax(current_node, tree, player_sym, opponent_sym, False)
                score = node.data[2]
                try:
                    if score > maxScore:
                        maxScore = score
                        node.data[1] = exe
                        node.data[2] = maxScore * self.values["penality"]
                except TypeError:
                    pass
            return node

        if isMaxPlayer == False:
            minScore = math.inf
            state = node.data[1]
            actions = state.actions(opponent_sym)
            parent_id = node.data[0]
            id = parent_id + 1
            branch = []
            for i in range(len(actions)):
                clone = state.clone()
                exe = clone.execute(actions[i])
                node = Node(id, exe, None, parent_id)
                tree.addToTree(node.data)
                branch.append(node)
                id += 1
            #pdb.set_trace()
            for i in range(len(branch)):
                current_node = branch[i]
                node = self.minimax(current_node, tree, player_sym, opponent_sym, True)
                score = node.data[2]
                try:
                    if score < minScore:
                        maxScore = score
                        node.data[1] = exe
                        node.data[2] = maxScore * self.values["penality"]
                except TypeError:
                    pass
            return node




    def terminal_test(self, node):
        #pdb.set_trace()
        state = node.data[1]
        #pdb.set_trace()
        if state.game_over() == True:
            #pdb.set_trace()
            winner = state.winner
            if winner == self.char:
                node.data[2] = self.values["win"]
                return node
            elif (self.char == "X" and winner == "O") or (self.char == "O" and winner == "X"):
                node.data[2] = self.values["lose"]
                return node
            else:
                node.data[2] = self.values["tie"]
                return node
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
        self.data = [self.id, self.state, self.value, self.parent_id]
