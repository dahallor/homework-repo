import pdb
import numpy as np
import math




class Tree:
    def __init__(self, data):
        self.featureHash = {}
        self.tree = []
        self.examples = []
        self.attributes = []
        self.entropy = []
        self.epsilon = .0000001
        self.total = len(data)

    def setAttribute(self, IL):
        for i in range(len(IL.trainX[0])):
            var = self.setVarName(i)
            self.featureHash[var] = {0 : [0, 0], 1: [0, 0], "entropy" : 0}
            self.attributes.append(var)

    def setInitialExamples(self, IL):
        rows = len(IL.trainX)
        cols = len(IL.trainX[0]) + 1
        self.train = np.zeros((rows, cols), dtype = int)
        for i in range(len(IL.trainX)):
            answer = int(IL.trainY[i][0])
            for j in range(len(IL.trainX[i])):
                feature_num = IL.trainX[i][j]
                if feature_num < IL.mean[j]:
                    IL.trainX[i][j] = 0
                else:
                    IL.trainX[i][j] = 1
            temp = np.array([])
            temp = np.append(IL.trainX[i], IL.trainY[i][0])
            #pdb.set_trace()
            for j in range(len(self.train[i])):
                self.train[i][j] = temp[j]
            self.examples.append(self.train[i])


    def getExamples(self, examples):
        pass

    def DTL(self, examples, attributes, default, classification):

        total = len(examples)
        #classification = [0, 0]
        for i in range(len(examples)):
            if examples[i][-1] == 0:
                classification[0] += 1
            if examples[i][-1] == 1:
                classification[1] += 1
        if len(examples) == 0:
            return default
        elif classification[0] == total:
            return 0
        elif classification[1] == total:
            return 1
        elif len(attributes) == 0:
            return math.mode(examples)
        else:
            pass



    def getEntropy(self, attributes, examples, k):
        sum = 0
        self.featureHash = {}
        for i in range(len(attributes)):
            var = attributes[i]
            self.featureHash[var] = np.zeros((1, k), dtype = int)
        for i in range(len(examples)):
            for j in range(len(examples[i])-1):
                var = attributes[j]
                if examples[i][-1] == 0:
                    self.featureHash[var][0][0] += 1
                if examples[i][-1] == 1:
                    self.featureHash[var][0][1] += 1


                
        

        

        






    def fillHashData(self, IL, type):
        for i in range(len(IL.trainX)):
            answer = int(IL.trainY[i][0])
            for j in range(len(IL.trainX[i])):
                var = self.setVarName(j)
                feature_num = IL.trainX[i][j]
                if feature_num < IL.mean[j]:
                    #IL.trainX[i][j] = "below avg"
                    feature = 0
                else:
                    #IL.trainX[i][j] = "above avg"
                    feature = 1
                if type == "binary":
                    self.setBinaryHash(var, answer, feature)

    def calcEntropy(self, k):
        for i in range(len(self.featureHash)):
            var = self.setVarName(i)
            b0 = self.featureHash[var]["below avg"][0]
            b1 = self.featureHash[var]["below avg"][1]
            a0 = self.featureHash[var]["above avg"][0]
            a1 = self.featureHash[var]["above avg"][1]
            below_count = b0 + b1
            above_count = a0 + a1

            if b0 == 0:
                prob_b0 = 0
            else:
                prob_b0 = -1 * (b0/self.total * np.log((b0/self.total)))
            if b1 == 0:
                prob_b1 = 0
            else:
                prob_b1 = -1 * (b1/self.total * np.log((b1/self.total)))
            if a0 == 0:
                prob_a0 = 0
            else:
                prob_a0 = -1 * (a0/self.total * np.log((a0/self.total)))
            if a1 == 0:
                prob_a1 = 0
            else:
                prob_a1 = -1 * (a1/self.total * np.log((a1/self.total)))
            entropy = (below_count/self.total) * (prob_b0 + prob_b1) + (above_count/self.total) * (prob_a0 + prob_a1)
            self.featureHash[var]["entropy"] = entropy


    def getRoot(self):
        lowest = 1
        name = ""
        for i in range(len(self.featureHash)):
            var = self.setVarName(i)
            if self.featureHash[var]["entropy"] < lowest:
                lowest = self.featureHash[var]["entropy"]
                name = var
        return name, lowest


    def setVarName(self, num):
        var = "x" + str(num + 1)
        return var
            


    def setBinaryHash(self, var, answer, feature):
        match answer:
            case 0:
                arr = self.featureHash[var][feature]
                arr[0] += 1
            case 1:
                arr = self.featureHash[var][feature]
                arr[1] += 1



class Node:
    def __init__(self, data, left = None, right = None):
        self.left = left
        self.right = right
        self.node = data

    

    
