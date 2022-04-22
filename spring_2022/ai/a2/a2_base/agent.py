import random
import util

class Node:
    def __init__(self):
        self.open = []
        self.closed = []
        self.queue = []
        self.tree = []

    def setTree(self):
        pass




class Agent(Node):
    def __init__(self):
        pass

    def BFS(self):
        pass

    def DFS (self):
        pass

    def a_star(self):
        pass

    def random_walk(self, state, n):
        for i in range(n):
            actions = state.actions()
            options = len(actions)
            selection = random.randint(0, options-1)
            selected_action = actions[selection]
            result = state.execute(selected_action)
            #print(state.pprint_string())
            util.pprint(result)

        