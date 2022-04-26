import random
import util
import pdb
from rgb import *

class Node:
    def __init__(self):
        self.currentPathNodes = []
        self.currentPathStatesOnly = []
        self.open = []
        self.closed = []
        self.id = 1
        self.parent_id = 0

    def createNode(self, id, value, pointer):
        node = [id, value, pointer]
        return node

    def addToFront(self, node):
        self.open.insert(0, node)

    def addToBack(self, node):
        self.open.append(node)

    def deleteFromFront(self):
        node = self.open[0]
        self.open.pop(0)
        self.closed.insert(0, node)

    def deleteFromBack(self):
        node = self.open[-1]
        self.open.pop(-1)
        self.closed.append(node)

    def getFromOpenFront(self):
        node = self.open[0]
        state = node[1]
        return state

    def getFromOpenBack(self):
        node = self.open[-1]
        state = node[1]
        return state






class Agent(Node):
    def __init__(self):
        super().__init__()

    def _search(self, state, parameter):
        #Initialize values
        value = state.__str__()
        node = self.createNode(self.id, value, None)
        self.open.append(node)
        possible_actions = state.actions()
        clone = state.clone()

        #Search Algorithm

        i = 0
        while len(self.open) > 0:
            i += 1
            if parameter == "BFS":
                self.BFS(possible_actions, clone)
                string = self.getFromOpenFront()
                self.parent_id = self.open[0][0]
            if parameter == "DFS":
                self.DFS(possible_actions, clone)
                string = self.getFromOpenBack()
                self.parent_id = self.open[-1][0]

            
            
            clone = State(string)
            possible_actions = clone.actions()
            if i % 1000 == 0:
                print(i)




    def BFS(self, possible_actions, clone):
        self.deleteFromFront()
        for i in range(len(possible_actions)):
            reset_state = State(str(clone))
            selected_action = possible_actions[i]
            result = reset_state.execute(selected_action).__str__()
            repeat = False
            for j in range(len(self.closed)):
                if result == self.closed[j][1]:
                    repeat = True
                    break
            for j in range(len(self.open)):
                if result == self.open[j][1]:
                    repeat = True
                    break
            if repeat == False:
                self.id += 1
                node = self.createNode(self.id, result, self.parent_id)
                self.addToBack(node)


    def DFS (self, possible_actions, clone):
        self.deleteFromBack()
        for i in range(len(possible_actions)):
            reset_state = State(str(clone))
            selected_action = possible_actions[i]
            result = reset_state.execute(selected_action).__str__()
            repeat = False
            for j in range(len(self.closed)):
                if result == self.closed[j][1]:
                    repeat = True
                    break
            for j in range(len(self.open)):
                if result == self.open[j][1]:
                    repeat = True
                    break
            if repeat == False:
                self.id += 1
                node = self.createNode(self.id, result, self.parent_id)
                self.addToBack(node)
        pdb.set_trace()

    def astar(self, state, h):
        pass

    def random_walk(self, state, n):
        node = self.createNode(self.id, state.clone(), None)
        self.currentPathNodes.append(node)
        #pdb.set_trace()
        for i in range(n-1):
            self.id += 1
            self.parent_id += 1
            actions = state.actions()
            options = len(actions)
            selection = random.randint(0, options-1)
            selected_action = actions[selection]
            result = state.execute(selected_action)
            node = self.createNode(self.id, state.clone(), self.parent_id)
            self.currentPathNodes.append(node)
            #pdb.set_trace()
            #results.append(state.clone())
        #pdb.set_trace()
        for i in range(len(self.currentPathNodes)):
            self.currentPathStatesOnly.append(self.currentPathNodes[i][1])
            print(i)
        util.pprint(self.currentPathStatesOnly)

        