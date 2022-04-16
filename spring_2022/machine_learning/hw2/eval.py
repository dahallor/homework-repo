import numpy as np
import pdb

class Eval():
    def __init__(self):
        self.ratio = {
            "T+" : 0,
            "T-" : 0,
            "F+" : 0,
            "F-" : 0
        }
        self.accuracy = 0
        self.precision = 0
        self.recall = 0
        self.f = 0

    def calcYhat(self, X, weights):
        Yhat = np.zeros((len(X), 1), dtype = 'float')
        for i in range(len(X)):
            exponent = -1 * (np.matmul(X[i], weights.W) + weights.b)
            Yhat[i] = 1/(1 + np.exp(exponent))

        return Yhat

    def setPosAndNeg(self, Y, Yhat):
        newYhat = []
        for i in range(len(Yhat)):
            temp = []
            if Yhat[i][0] >= .5:
                value = 1
            else:
                value = 0
            temp.append(value)
            newYhat.append(temp)

        for i in range(len(Y)):
            if int(Y[i][0]) == int(newYhat[i][0]) and int(Y[i][0]) == 1:
                self.ratio["T+"] += 1
            if int(Y[i][0]) == int(newYhat[i][0]) and int(Y[i][0]) == 0:
                self.ratio["T-"] += 1
            if int(Y[i][0]) != int(newYhat[i][0]) and int(Y[i][0]) == 1:
                self.ratio["F-"] += 1
            if int(Y[i][0]) != int(newYhat[i][0]) and int(Y[i][0]) == 0:
                self.ratio["F+"] += 1

    def setAccuracy(self, N):
        sum = self.ratio["T+"] + self.ratio["T-"]
        self.accuracy = (1/N) * sum


    def setPrecision(self):
        TP = self.ratio["T+"]
        FP = self.ratio["F+"]

        self.precision = TP/(TP+FP)

    def setRecall(self):
        TP = self.ratio["T+"]
        FN = self.ratio["F-"]  

        self.recall = TP/(TP+FN) 

    def setF_Measure(self):
        self.f = (2 * self.precision * self.recall)/(self.precision + self.recall)         

    

