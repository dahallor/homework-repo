import random
import util
import pdb
from rgb import *

class Node:
    def __init__(self):
        self.open = []
        self.closed = []
        self.queue = []

    def createNode(self, value, pointer):
        node = [value, pointer]
        return node

    def addToFront(self, node):
        self.queue.insert(0, node)

    def addToBack(self, node):
        self.queue.append(node)

    def deleteFromFront(self):
        self.queue.pop(0)

    def deleteFromBack(self):
        self.queue.pop(-1)





class Agent(Node):
    def __init__(self):
        super().__init__()

    def _search(self, state, parameter):
        value = state.__str__()
        node = self.createNode(value, None)
        self.open.append(node)

        while len(self.open) > 0:
            possible_actions = state.actions()
            if parameter == "BFS":
                clone = state.clone()
                for i in range(len(possible_actions)):
                    reset_state = State(str(clone))
                    selected_action = possible_actions[i]
                    '''
                    stored_x = selected_action.x
                    stored_y = selected_action.y
                    stored_x2 = selected_action.x2
                    stored_y2 = selected_action.y2
                    '''
                    result = reset_state.execute(selected_action).__str__()
                    if result not in self.closed:
                        node = self.createNode(result, selected_action)
                        self.open.append(node)
                    #Action(stored_x2, stored_y2, stored_x, stored_y)
                    

                    pdb.set_trace()



    def BFS(self, state):
        self._search(state, "BFS")

    def DFS (self, state):
        pass

    def astar(self, state, h):
        pass

    def random_walk(self, state, n):
        results = []
        for i in range(n):
            actions = state.actions()
            options = len(actions)
            selection = random.randint(0, options-1)
            selected_action = actions[selection]
            result = state.execute(selected_action)
            results.append(state.clone())
        util.pprint(results)

        