import pdb
import numpy as np

class Tree:
    def __init__(self, data):
        self.featureHash = {}
        self.epsilon = .0000001
        self.total = len(data)

    def setHash(self, IL):
        for i in range(len(IL.trainX[0])):
            var = self.setVarName(i)
            self.featureHash[var] = {"below mean" : [0, 0], "above mean": [0, 0], "entropy" : 0}
        

    def fillHashData(self, IL, type):
        for i in range(len(IL.trainX)):
            for j in range(len(IL.trainX[i])):
                var = self.setVarName(j)
                answer = IL.trainY[i]
                feature_num = IL.trainX[i][j]
                #if feature_num < IL.median[j]:
                if feature_num < IL.mean[j]:
                    feature = "below mean"
                else:
                    feature = "above mean"
                #hash = self.featureHash[var]
                #print(var, answer, feature, hash)
                if type == "binary":
                    #pdb.set_trace()
                    self.setBinaryHash(var, answer, feature)

    def calcEntropy(self):
        for i in range(len(self.featureHash)):
            var = self.setVarName(i)
            b0 = self.featureHash[var]["below mean"][0]
            b1 = self.featureHash[var]["below mean"][1]
            a0 = self.featureHash[var]["above mean"][0]
            a1 = self.featureHash[var]["above mean"][1]
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
        #format is list[0]: Y = 0 list[1]: Y = 1
        #pdb.set_trace()
        match answer:
            case 0:
                arr = self.featureHash[var][feature]
                arr[0] += 1
            case 1:
                arr = self.featureHash[var][feature]
                arr[1] += 1




