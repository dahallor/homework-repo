import pdb
import numpy as np




class Tree:
    def __init__(self, data):
        self.featureHash = {}
        self.obsList = []
        self.entropy = []
        self.epsilon = .0000001
        self.total = len(data)

    def setHash(self, IL):
        for i in range(len(IL.trainX[0])):
            var = self.setVarName(i)
            self.featureHash[var] = {"below avg" : [0, 0], "above avg": [0, 0], "entropy" : 0}
        

    def fillHashData(self, IL, type):
        for i in range(len(IL.trainX)):
            observation = {}
            answer = int(IL.trainY[i][0])
            observation["class"] = answer
            for j in range(len(IL.trainX[i])):
                var = self.setVarName(j)
                feature_num = IL.trainX[i][j]
                if feature_num < IL.mean[j]:
                    #IL.trainX[i][j] = "below avg"
                    feature = "below avg"
                else:
                    #IL.trainX[i][j] = "above avg"
                    feature = "above avg"
                observation[var] = feature
                if type == "binary":
                    self.setBinaryHash(var, answer, feature)
            self.obsList.append(observation)

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



class Node(Tree):
    def __init__(self):
        super().__init__()
        self.id = 1
        node = {}

    

    
