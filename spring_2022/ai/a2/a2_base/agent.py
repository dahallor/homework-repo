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

    def createAStarNode(self, id, value, h, pointer):
        node = [id, value, h, pointer]
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




#--------------------------------------------------------------------------------------------------------------







class Agent:


#--------------------------------------Search-------------------------------------------------------------------
    def _search(self, state, parameter, node, aux):
        currentNode,  possible_actions, clone, tally = aux.initalizeSearch(node, state)
        aux.printCurrentPath(node, currentNode)

        while len(node.open) > 0 :
            currentNode = aux.initalizeLoop(node)
            if tally > 1:
                clone = State(currentNode[1].__str__())
                possible_actions = clone.actions()
            for i in range(len(possible_actions)):
                result_string, tally, result = aux.evalCurrentNode(tally, clone, possible_actions, i)
                repeat = aux.checkForRepeats(result_string, node)
                childNode = aux.selectSearchMethod(self, repeat, node, parameter, result, currentNode)
                aux.checkIfGoal(result_string, tally)
            if parameter == "DFS" and repeat == False:
                aux.printCurrentPath(node, childNode)
            if parameter == "A*" and repeat == False:
                aux.reorderOpen(node)


    def BFS(self, result, currentNode, node):
        node.parent_id = currentNode[0]
        childNode = node.createNode(node.id, result, node.parent_id)
        node.addToBack(childNode)
        return childNode

    def DFS(self, result, currentNode, node):
        node.parent_id = currentNode[0]
        childNode = node.createNode(node.id, result, node.parent_id)
        node.addToFront(childNode)
        return childNode

    def astar(self, result, currentNode, h, node):
        node.parent_id = currentNode[0]
        childNode = node.createAStarNode(node.id, result, h, node.parent_id)
        node.addToBack(childNode)
        return childNode
        

#-------------------------------random walk-------------------------------------------------------------------------

    def random_walk(self, state, n, node, aux):
        currentNode = node.createNode(node.id, state.clone(), None)
        node.currentPathNodes.append(currentNode)
        for i in range(n-1):
            node.id += 1
            node.parent_id += 1
            actions = state.actions()
            options = len(actions)
            selection = random.randint(0, options-1)
            selected_action = actions[selection]
            result = state.execute(selected_action)
            currentNode = node.createNode(node.id, state.clone(), node.parent_id)
            node.currentPathNodes.append(currentNode)
            #pdb.set_trace()
        node.printStatesFromCurrentPath()





#-------------------------------------------------------------------------------------------------------------------






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
        tally = 0
        return currentNode,  possible_actions, clone, tally

    def initalizeLoop(self, node):
        currentNode = node.open[0]
        node.deleteFromFront()
        return currentNode

    def checkForRepeats(self, result_string, node):
        repeat = False
        for j in range(len(node.closed)):
            if result_string == node.closed[j][1]:
                repeat = True
                break
        print(repeat)
        #pdb.set_trace()
        return repeat
    
    def selectSearchMethod(self, agent, repeat, node, parameter, result, currentNode):
        if repeat == False:
            node.id += 1
            if parameter == "BFS":
                childNode = agent.BFS(result, currentNode, node)
                self.printCurrentPath(node, childNode)

            if parameter == "DFS":
                childNode = agent.DFS(result, currentNode, node)

            if parameter == "A*":
                h = self.heuristic(node, result)
                #pdb.set_trace()
                childNode = agent.astar(result, currentNode, h, node)
                #pdb.set_trace()
                self.printCurrentPath(node, childNode)
           
            
            return childNode

    def checkIfGoal(self, string, tally):
        check = State(string)
        #pdb.set_trace()
        if check.is_goal() == True:
            print(tally)
            pdb.set_trace()
            sys.exit()


    def printCurrentPath(self, node, childNode):
        node.currentPath = []
        parent = childNode[-1]
        node.currentPath.insert(0, childNode[1])
        #pdb.set_trace()
        while parent != None:
            #pdb.set_trace()
            for i in range(len(node.closed)):
                if parent == node.closed[i][0]:
                    parentNode = node.closed[i]
                    parent = parentNode[-1]
                    node.currentPath.insert(0, parentNode[1])
            #pdb.set_trace()
        util.pprint(node.currentPath)

    def heuristic(self, node, result):
        #Heuristic calculation is how many same color spaces are touching. The lower the better
        result = result.__str__()
        split = [char for char in result]
        matrix = []
        temp = []
        for i in range(len(split)):
            if split[i] == "|":
                matrix.append(temp)
                temp = []
                continue
            temp.append(split[i])
            if i == len(split)-1:
                matrix.append(temp)

        h = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                #pdb.set_trace()
                letter = matrix[i][j]

                try:
                    if matrix[i][j-1] == letter:
                        h += 1
                except Exception:
                    pass

                try:
                    if matrix[i][j+1] == letter:
                        h += 1
                except Exception:
                    pass

                try:
                    if matrix[i-1][j] == letter:
                        h += 1
                except Exception:
                    pass

                try:
                    if matrix[i+1][j] == letter:
                        h += 1
                except Exception:
                    pass
        return h

    def reorderOpen(self, node):
        temp = []
        for i in range(len(node.open)):
            currentNode = node.open[i]
            h = currentNode[2]
            if len(temp) == 0:
                temp.append(currentNode)
            for j in range(len(temp)):
                if h < temp[j][2]:
                    temp.insert(j, currentNode)
                    break
                if j == len(temp) - 1:
                    temp.append(currentNode)
        node.open = temp
        #node.open.append(temp)
        #pdb.set_trace()

    def findNext(self, node):
        lowestH = 9999999999
        lowestNode = None
        for i in range(len(node.open)):
            currentNode = node.open[i]
            h = currentNode[2]
            if h < lowestH:
                lowestH = h
                lowestNode = currentNode
        return lowestNode
        
