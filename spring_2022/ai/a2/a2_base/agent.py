import random
import util
import pdb
import sys
from rgb import *

class Node:
    def __init__(self):
        self.currentPath = []
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



class Agent:

    def _search(self, state, parameter, node, aux):
        #Initialize values
        currentNode,  possible_actions, clone = aux.initalizeSearch(node, state)
        aux.addToCurrentPath(node, currentNode[1])

        #Search Algorithm

        tally = 0
        while len(node.open) > 0:
            currentNode = aux.initalizeLoop(node)
            for i in range(len(possible_actions)):
                result_string, tally, result = aux.evalCurrentNode(tally, clone, possible_actions, i)
                repeat = aux.checkForRepeats(result_string, node)
                aux.selectSearchMethod(self, repeat, node, parameter, result, currentNode)
                aux.checkIfGoal(result_string, tally)

                State(result_string)
                
            
            #clone = State(string)
            possible_actions = clone.actions()






    def BFS(self, result, currentNode, node):
        node.parent_id = currentNode[0]
        currentNode = node.createNode(node.id, result, node.parent_id)
        node.addToBack(currentNode)
        '''
        string = node.getFromOpenFront().__str__()
        
        return string
        '''



    def DFS(self, result, currentNode, node):
        node.parent_id = currentNode[0]
        currentNode = node.createNode(node.id, result, node.parent_id)
        node.addToFront(currentNode)
        '''
        string = node.getFromOpenFront().__str__()

        return string
        '''


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

class AuxMethods:
    def evalCurrentNode(self, tally, clone, possible_actions, i):
        tally += 1
        reset_state = State(str(clone))
        #pdb.set_trace()
        selected_action = possible_actions[i]
        result = reset_state.execute(selected_action)
        result_string = result.__str__()

        return result_string, tally, result

    def initalizeSearch(self, node, state):
        currentNode = node.createNode(node.id, state.clone(), None)
        node.open.append(currentNode)
        possible_actions = state.actions()
        clone = state.clone()
        return currentNode,  possible_actions, clone

    def initalizeLoop(self, node):
        currentNode = node.open[0]
        #node.currentPathNodes.append(currentNode)
        node.deleteFromFront()
        return currentNode

    def checkForRepeats(self, result_string, node):
        repeat = False
        for j in range(len(node.closed)):
            if result_string == node.closed[j][1]:
                repeat = True
                break
        return repeat
    
    def selectSearchMethod(self, agent, repeat, node, parameter, result, currentNode):
        if repeat == False:
            node.id += 1
            if parameter == "BFS":
                agent.BFS(result, currentNode, node)
            if parameter == "DFS":
                agent.DFS(result, currentNode, node)
            
            node.printStatesFromCurrentPath()
            pdb.set_trace()
            self.addToCurrentPath(node, result)
            self.printCurrentPath(node)

    def checkIfGoal(self, string, tally):
        check = State(string)
        #pdb.set_trace()
        if check.is_goal() == True:
            print(tally)
            sys.exit()

    def addToCurrentPath(self, node, result):
        #pdb.set_trace()
        node.currentPath.append(result)

    def removeFromCurrentPath(self):
        pass

    def printCurrentPath(self, node):
        util.pprint(node.currentPath)
