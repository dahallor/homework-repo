import random
import util
import pdb
import sys
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

    def printStatesFromCurrentPath(self):
        self.currentPathStatesOnly = []
        #pdb.set_trace()
        for i in range(len(self.currentPathNodes)):
            self.currentPathStatesOnly.append(self.currentPathNodes[i][1])
        util.pprint(self.currentPathStatesOnly)

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
        node = self.createNode(self.id, state.clone(), None)
        self.open.append(node)
        #self.currentPathNodes.append(node)
        possible_actions = state.actions()
        clone = state.clone()

        #Search Algorithm

        tally = 0
        while len(self.open) > 0:
            '''
            if i > 2:
                pdb.set_trace()
                self.currentPathNodes.pop(-1)
                '''
            currentNode = self.open[0]
            self.currentPathNodes.append(currentNode)
            self.deleteFromFront()
            for i in range(len(possible_actions)):
                result_string, tally, result = self.evalCurrentNode(self, tally, clone, possible_actions, i)
                #pdb.set_trace()
                repeat = False
                num_paths = 0
                for j in range(len(self.closed)):
                    if result_string == self.closed[j][1]:
                        repeat = True
                        break
                if repeat == False:
                    num_paths += 1
                    self.id += 1
                    if parameter == "BFS":
                        string = self.BFS(result, currentNode)
                    if parameter == "DFS":
                        string = self.DFS(result, currentNode)
                    
                    self.printStatesFromCurrentPath()
                    #pdb.set_trace()
                    #self.currentPathNodes.pop(-1)
                check = State(string)
                pdb.set_trace()
                if check.is_goal() == True:
                    print(tally)

                    sys.exit()
                #if num_paths == 0:
                    #self.currentPathNodes.pop(-1)
                State(string)
                
            
            clone = State(string)
            possible_actions = clone.actions()






    def BFS(self, result, currentNode):
        self.parent_id = currentNode[0]
        node = self.createNode(self.id, result, self.parent_id)
        self.currentPathNodes.append(node)
        self.addToBack(node)
        string = self.getFromOpenFront().__str__()
        
        return string



    def DFS(self, result, currentNode):
        self.parent_id = currentNode[0]
        node = self.createNode(self.id, result, self.parent_id)
        self.currentPathNodes.append(node)
        self.addToFront(node)
        string = self.getFromOpenFront().__str__()

        return string


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
        self.printStatesFromCurrentPath()


    def evalCurrentNode(self, tally, clone, possible_actions, i):
        tally += 1
        reset_state = State(str(clone))
        #pdb.set_trace()
        selected_action = possible_actions[i]
        result = reset_state.execute(selected_action)
        result_string = result.__str__()

        return result_string, tally, result


        