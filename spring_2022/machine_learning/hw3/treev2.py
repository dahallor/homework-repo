import pdb
import numpy as np
import math
from node import *




class Tree:
    def __init__(self, data):
        self.featureHash = {}
        self.tree = []
        self.examples = []
        self.attributes = []
        self.entropy = []
        self.epsilon = .0000001
        self.total = len(data)


    def DTL(self, examples, attributes, default, k, val):

        total = len(examples)
        '''
        classification = [0, 0, 0, 0]
        pdb.set_trace()
        for i in range(len(examples)):
            match examples[i][-1]:
                case 0:
                    classification[0] += 1
                case 1:
                    classification[1] += 1
                case 2:
                    classification[2] += 1
                case 3:
                    classification[3] += 1
                case _:
                    raise Exception("Issue in DTL - Classifications")
        elif classification[0] == total:
            return 0
        elif classification[1] == total:
            return 1
        '''
        if len(examples) == 0:
            return default
        elif len(attributes) == 0:
            #return math.mode(examples)
            pass
        else:
            self.setEntropy(attributes, examples, k, val)
            feature = self.getLowestEntropy(attributes)
            pdb.set_trace()



    def convertFeaturesToBinary(self, IL, data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                feature_num = data[i][j]
                if feature_num < IL.mean[j]:
                    data[i][j] = 0
                else:
                    data[i][j] = 1


    def getExamples(self, examples):
        for i in range(len(examples)):
            pass

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
        tally = self.setCurrentTallies(attributes, examples)
        for i in range(len(attributes)):
            sum = 0
            var = attributes[i]
            for j in range(k):
                if type == "binary":
                    xn, xncn, xncm = self.getCurrentThing(tally, var, j)
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