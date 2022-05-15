import numpy as np
import statistics as stat
import math
import pdb


class KNN:
    def __init__(self, k = 1):
        self.k = k
        self.numCorrect = 0
        self.lowest_value = []
        self.index = []

    def findNearestNeighbors(self, IL, validX, trainX):
        print("Finding Nearest Neighbors...")
        for i in range(len(validX)):
            if i % 100 == 0:
                print("Observation {} out of {}".format(i, len(validX)))
            self._setArray()
            validX_vector = validX[i]
            yhat = int(IL.validY[i][0])
            distances = self._distance(trainX, validX_vector, i)
            for j in range(self.k):
                for k in range(len(distances)):
                    if distances[k] < self.lowest_value[j] and k not in self.index:
                        self.lowest_value.insert(j, distances[k])
                        self.lowest_value.pop(j+1)
                        self.index.insert(j, k)
                        self.index.pop(j+1)
            self._getMaxValues(IL, yhat)

    def getAccuracy(self, total):
        acc = (self.numCorrect/total) * 100
        print("{:.6f}%".format(acc))
        print()
            


    def _distance(self, trainX, validX_vector, i):
        distances = []
        for j in range(len(trainX)):
            sum = 0
            trainX_vector = trainX[j]
            for k in range(len(validX_vector)):
                dif = validX_vector[k] - trainX_vector[k]
                sum += math.pow(dif, 2)
            dist = math.sqrt(sum)
            distances.append(dist)
        return distances

    def _setArray(self):
        self.lowest_value = []
        self.index = []
        for i in range(self.k):
            self.lowest_value.append(999999999)
            self.index.append(9999999999)

    def _getMaxValues(self, IL, yhat):
        classes = []
        for a in range(len(self.index)):
            value = self.index[a]
            classes.append(int(IL.trainY[value][0]))
        mode = stat.mode(classes)
        if mode == yhat:
            self.numCorrect += 1
    
            


    

 