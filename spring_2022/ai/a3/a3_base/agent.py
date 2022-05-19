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
        self.player_sym = self.char
        self.penalties = 0
        if self.player_sym == "X":
            self.opponent_sym = "O"
        else:
            self.opponent_sym = "X"

        

    def choose_action(self, state):
        possible_actions = state.actions(self.player_sym)
        selection = self.findBestMove(state)
        #pdb.set_trace()
        state.execute(possible_actions[selection])
        self.penalties = 0
        return state

    def findBestMove(self, state):
        maxScore = -math.inf
        root = Node(self.player_sym, state, None)
        root.expand(self, self.opponent_sym)
        for child in range(len(root.children)):
            #print(root.children[child].state.__str__())
            score = self.minimax(root.children[child], False)
            #pdb.set_trace()
            if score > maxScore:
                maxScore = score
                selection = child
        return selection

        
    def minimax(self, node, isMaxPlayer):
        result = self.terminal_test(node, self.player_sym)
        if result != None:
            return result.value
        
        if isMaxPlayer == True:
            maxScore = -math.inf
            new_node = Node(self.player_sym, node.state, None)
            new_node.expand(self, self.opponent_sym)
            #pdb.set_trace()
            for child in range(len(new_node.children)):
                score = self.minimax(new_node.children[child], False)
                maxScore = max(score, maxScore)
            return maxScore
            

        if isMaxPlayer == False:
            minScore = math.inf
            new_node = Node(self.opponent_sym, node.state, None)
            new_node.expand(self, self.player_sym)
            for child in range(len(new_node.children)):
                score = self.minimax(new_node.children[child], True)
                minScore = min(score, minScore)
            return minScore



    def terminal_test(self, node, sym):
        if node.state.game_over() != False:
            if node.state.winner() == sym:
                node.value = self.values["win"]
            elif node.state.winner() != sym:
                node.value = self.values["lose"]
            else:
                node.value = self.values["tie"]
            p = math.pow(self.values["penality"], self.penalties)
            node.value *= p
            return node
        else:
            return None


class Node:
    def __init__(self, char, state, value, parent = None, actions = None):
        self.state = state
        self.value = value
        self.parent = parent
        self.children = []
        self.actions = self.state.actions(char)

    def expand(self, minimax, char):
        minimax.penalties += 1
        for action in self.actions:
            clone = self.state.clone()
            childNode = Node(char, clone.execute(action), None, self)
            self.children.append(childNode)

