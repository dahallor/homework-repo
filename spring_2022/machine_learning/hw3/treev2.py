import pdb
import numpy as np
import math
from node import *




class Tree:
    def __init__(self, data):
        self.tree = []
        self.examples = []
        self.attributes = []
        self.tally = {}
        self.entropy = []
        self.epsilon = .0000001
        self.total = len(data)

    def printTree(self):
        for i in range(len(self.tree)):
            #pdb.set_trace()
            print(self.tree[i].__str__())
            print()

    def DTL(self, examples, attributes, default, k, val):
        total = len(examples)
        if len(examples) == 0:
            return default
        elif len(attributes) == 0:
            class_val = self.getMode()
            return class_val
        else:
            self.setEntropy(attributes, examples, k, val)
            feature = self.getLowestEntropy(attributes)
            
            temp = self.tally[feature]
            data = [feature, temp]
            #tree = Tree(examples)
            '''
            
            
            node = Node(data, examples_left, examples_right)
            '''
            attributes.remove(feature)
            
            for i in range(2):
                if i == 0:
                    default = self.getMode()
                    examples_left = self.getExamples(examples, feature, "left")
                    data = self.DTL(examples_left, attributes, default, k, val)
                if i == 1:
                    default = self.getMode()
                    examples_right = self.getExamples(examples, feature, "right")
                    data = self.DTL(examples_right, attributes, default, k, val)
                try:
                    node = Node(data, examples_left, examples_right)
                except Exception:
                    try:
                        node = Node(data, examples_left)
                    except Exception:
                        try:
                            node = Node(data, examples_right)
                        except Exception:
                            try:
                                node = Node(data)
                            except Exception:
                                raise Exception("No nodes selected")
                                

                self.tree.append(node)
            return self.tree

    def getMode(self):
        key = ""
        for i in self.tally:
            key = i
        #pdb.set_trace()
        try:
            x0c0 = self.tally[key]["x0, c0"]
            x0c1 = self.tally[key]["x0, c1"]
        except Exception:
            pass
        try:
            x1c0 = self.tally[key]["x1, c0"]
            x1c1 = self.tally[key]["x1, c1"]
        except Exception:
            pass
        try:
            x1c1 = self.tally[key]["x1, c1"]
            x1c2 = self.tally[key]["x1, c2"]
            x1c3 = self.tally[key]["x1, c3"]
        except Exception:
            pass              
        try:
            x2c1 = self.tally[key]["x2, c1"]
            x2c2 = self.tally[key]["x2, c2"]
            x2c3 = self.tally[key]["x2, c3"]
        except Exception:
            pass   
        try:
            x3c1 = self.tally[key]["x3, c1"]
            x3c2 = self.tally[key]["x3, c2"]
            x3c3 = self.tally[key]["x3, c3"]
        except Exception:
            pass   

        try:
            value = max(x0c0, x0c1, x1c0, x1c1)
            if value == x0c0 or value == x1c0:
                return 0
            if value == x0c1 or value == x1c1:
                return 1
        except:
            value = max(x1c1, x1c2, x1c3, x2c1, x2c2, x2c3, x3c1, x3c2, x3c3)
            if value == x1c1 or value == x2c1 or value == x3c1:
                return 1
            if value == x1c2 or value == x2c2 or value == x3c2:
                return 2
            if value == x1c3 or value == x2c3 or value == x3c3:
                return 3


    def checkClassification(self, examples):
        class0 = 0
        class1= 0
        class2 = 0
        class3 = 0
        size = len(examples)
        for i in range(size):
            match examples[i][0]["class"]:
                case 0:
                    class0 += 1
                case 1:
                    class1 += 1
                case 2:
                    class2 += 1
                case 3:
                    class3 += 1
                case _:
                    raise Exception("Error in checkClassification")
        if class0 == size:
            return 0
        elif class1 == size:
            return 1
        elif class2 == size:
            return 2
        elif class3 == size:
            return 3
        else:
            return None


    def convertFeaturesToBinary(self, IL, data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                feature_num = data[i][j]
                if feature_num < IL.mean[j]:
                    data[i][j] = 0
                else:
                    data[i][j] = 1


    def getExamples(self, examples, feature, branch):
        new_examples = []
        for i in range(len(examples)):
            if branch == "left":
                if examples[i][0][feature] == 0:
                    new_examples.append(examples[i])
            if branch == "right":
                if examples[i][0][feature] == 1:
                    new_examples.append(examples[i])
        return new_examples

        

    def setInitialExamples(self, IL):
        for i in range(len(IL.trainX)):
            temp = []
            example = {}
            example["class"] = int(IL.trainY[i][0])
            for j in range(len(IL.trainX[i])):
                var = self.setVarName(j)
                example[var] = int(IL.trainX[i][j])
            temp.append(example)
            self.examples.append(temp)
            
                




    def setEntropy(self, attributes, examples, k, type):
        sum = 0
        self.entropy = {}
        self.tally = self.setCurrentTallies(attributes, examples)
        for i in range(len(attributes)):
            sum = 0
            var = attributes[i]
            for j in range(k):
                if type == "binary":
                    xn, xncn, xncm = self.getCurrentThing(self.tally, var, j)
                cn_fraction = xncn/(xn+self.epsilon)
                cm_fraction = xncm/(xn+self.epsilon)
                weight = (xn/self.total)
                part1 = -1 * (cn_fraction * math.log((cn_fraction+self.epsilon), k))
                part2 = -1 * (cm_fraction * math.log((cm_fraction+self.epsilon), k))
                sum += weight * (part1 + part2)
            self.entropy[var] = sum   
        

    def getLowestEntropy(self, attributes):
        lowestEntropy = 99999999
        feature = ""
        for i in range(len(attributes)):
            x = attributes[i]
            ent = self.entropy[x]
            if ent < lowestEntropy:
                lowestEntropy = ent
                feature = x
        return feature


    def getCurrentThing(self, tally, var, num):
        x0c0 = tally[var]["x0, c0"]
        x0c1 = tally[var]["x0, c1"]
        x1c0 = tally[var]["x1, c0"]
        x1c1 = tally[var]["x1, c1"]
        try:
            x2c0 = tally[var]["x2, c0"]
            x2c1 = tally[var]["x2, c1"]
            x3c0 = tally[var]["x3, c0"]
            x3c1 = tally[var]["x3, c1"]
        except:
            pass
        x0 = x0c0 + x0c1
        x1 = x1c0 + x1c1
        try:
            x2 = x2c0 + x2c1
            x3 = x3c0 + x3c1
        except:
            pass
        match num:
            case 0:
                return x0, x0c0, x0c1
            case 1:
                return x1, x1c0, x1c1
            case 2:
                return x2, x2c0, x2c1
            case 3:
                return x3, x3c0, x3c1
            case _:
                raise Exception("Get thingy error")

    def setCurrentTallies(self, attributes, examples):
        tally = {}
        for i in range(len(attributes)):
            var = attributes[i]
            tally[var] = {"x0, c0" : 0, "x0, c1" : 0, "x1, c0" : 0, "x1, c1" : 0}
        for i in range(len(examples)):
            for j in range(len(attributes)):
                var = attributes[j]
                x = examples[i][0]
                #pdb.set_trace()
                x = x[var]
                if examples[i][0]["class"] == 0 and x == 0:
                    tally[var]["x0, c0"] += 1
                if examples[i][0]["class"] == 1 and x == 0:
                    tally[var]["x0, c1"] += 1
                if examples[i][0]["class"] == 0 and x == 1:
                    tally[var]["x1, c0"] += 1
                if examples[i][0]["class"] == 1 and x == 1:
                    tally[var]["x1, c1"] += 1
        return tally


    def setVarName(self, num):
        var = "x" + str(num + 1)
        return var

    def setAttributes(self, data):
        for i in range(len(data[0])):
            var = self.setVarName(i)
            self.attributes.append(var)