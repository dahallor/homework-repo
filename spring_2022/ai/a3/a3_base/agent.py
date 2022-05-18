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
        self.id = 1
        root = Node(self.id, state.clone(), [None, -math.inf], None)
        self.id += 1
        tree = Tree()
        tree.addToTree(root.data)
        player_sym = self.char
        if player_sym == "X":
            opponent_sym = "O"
        else:
            opponent_sym = "X"
        '''
        id = 2
        branch = []
        actions = state.actions()
        for i in range(len(actions)):
            clone = state.clone()
            exe = clone.execute(actions[i])
            node = Node(id, exe, -math.inf, 1)
            tree.addToTree(node.data)
            branch.append(node)
            id += 1
        for i in range(len(branch)):
            node = branch[i]
            selection = self.minimax(node, tree, player_sym, opponent_sym, True)
            node = branch[i]
            '''
        #pdb.set_trace()
        selection = self.minimax(root, tree, player_sym, opponent_sym, False)
        pdb.set_trace()
        state.execute(selection.data[1])
        return state
        
    def minimax(self, node, tree, player_sym, opponent_sym, isMaxPlayer):
        result = self.terminal_test(node)
        #print(result)
        #pdb.set_trace()
        if result != None:
            #pdb.set_trace()
            return result

        if isMaxPlayer == True:
            maxScore = -math.inf
            scoreList = [None, maxScore]
            state = node.data[1]
            actions = state.actions(player_sym)
            parent_id = node.data[0]
            branch = []
            for i in range(len(actions)):
                clone = state.clone()
                exe = clone.execute(actions[i])
                node = Node(self.id, exe, scoreList, parent_id)
                tree.addToTree(node.data)
                branch.append(node)
                self.id += 1
            #pdb.set_trace()
            for i in range(len(branch)):
                current_node = branch[i]
                #pdb.set_trace()
                node = self.minimax(current_node, tree, player_sym, opponent_sym, False)
                #node = self.minimax(current_node, tree, player_sym, opponent_sym, True)
                #pdb.set_trace()
                branch[i] = node
            #pdb.set_trace()
            for i in range(len(branch)):
                node = branch[i]
                #pdb.set_trace()
                print(node.data)
                score = node.data[2][1]
                if score > maxScore:
                    maxScore = score
                    num = node.data[2][0]
            for i in range(len(branch)):
                node = branch[i]
                #pdb.set_trace()
                if node.data[2][1] == maxScore:
                    return_node = node
                    num = return_node.data[0]
                    new_score = maxScore * self.values["penality"]
                    return_node.data[2] = [num, new_score]
                    #pdb.set_trace()
                    return return_node

        if isMaxPlayer == False:
            minScore = math.inf
            scoreList = [None, minScore]
            state = node.data[1]
            actions = state.actions(opponent_sym)
            parent_id = node.data[0]
            branch = []
            for i in range(len(actions)):
                clone = state.clone()
                exe = clone.execute(actions[i])
                node = Node(self.id, exe, scoreList, parent_id)
                tree.addToTree(node.data)
                branch.append(node)
                self.id += 1
            #pdb.set_trace()
            for i in range(len(branch)):
                current_node = branch[i]
                #pdb.set_trace()
                node = self.minimax(current_node, tree, player_sym, opponent_sym, True)
                #pdb.set_trace()
                branch[i] = node
            for i in range(len(branch)):
                node = branch[i]
                scoreList = node.data[2]
                print(scoreList)
                score = scoreList[1]
                if score < minScore:
                    minScore = score
            for i in range(len(branch)):
                node = branch[i]
                #pdb.set_trace()
                if node.data[2][1] == minScore:
                    return_node = node
                    num = return_node.data[0]
                    new_score = minScore * self.values["penality"]
                    return_node.data[2] = [num, new_score]
                    return return_node




    def terminal_test(self, node):
        #pdb.set_trace()
        state = node.data[1]
        #pdb.set_trace()
        if state.game_over() != False:
            #pdb.set_trace()
            winner = state.winner()
            if winner == self.char:
                node.data[2] = [node.data[0], self.values["win"]]
                #pdb.set_trace()
                return node
            elif (self.char == "X" and winner == "O") or (self.char == "O" and winner == "X"):
                node.data[2] = [node.data[0], self.values["lose"]]
                #pdb.set_trace()
                return node
            else:
                node.data[2] = [node.data[0], self.values["tie"]]
                #pdb.set_trace()
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
