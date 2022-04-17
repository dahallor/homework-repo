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
        self.prec_PR = []
        self.recall_PR = []
        self.thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    def calcProbability(self, X, weights):
        Yhat = np.zeros((len(X), 1), dtype = 'float')
        for i in range(len(X)):
            exponent = -1 * (np.matmul(X[i], weights.W) + weights.b)
            Yhat[i] = 1/(1 + np.exp(exponent))

        return Yhat

    def setPosAndNeg(self, Y, Yhat, thresh):
        newYhat = []
        for i in range(len(Yhat)):
            temp = []
            if Yhat[i][0] >= thresh:
                value = 1
            else:
                value = 0
            temp.append(value)
            newYhat.append(temp)
        self.ratio.update( (k,0) for k in self.ratio )
        
        for i in range(len(Y)):
            if int(Y[i][0]) == 1 and int(newYhat[i][0]) == 1:
                self.ratio["T+"] += 1
            if int(Y[i][0]) == 1 and int(newYhat[i][0]) == 0:
                self.ratio["F-"] += 1
            if int(Y[i][0]) == 0 and int(newYhat[i][0]) == 1:
                self.ratio["F+"] += 1
            if int(Y[i][0]) == 0 and int(newYhat[i][0]) == 0:
                self.ratio["T-"] += 1
        #pdb.set_trace()


    def setAccuracy(self):
        sum = self.ratio["T+"] + self.ratio["T-"]
        N = sum + self.ratio["F+"] + self.ratio["F-"]
        self.accuracy = (1/N) * sum


    def setPrecision(self):
        TP = self.ratio["T+"]
        FP = self.ratio["F+"]
        try:
            self.precision = TP/(TP+FP)
        except Exception:
            self.precision = 1

    def setRecall(self):
        TP = self.ratio["T+"]
        FN = self.ratio["F-"]  
        try:
            self.recall = TP/(TP+FN)
        except Exception:
            self.recall = 0 

    def setF_Measure(self):
        self.f = (2 * self.precision * self.recall)/(self.precision + self.recall)   

    def setPR(self):
        self.prec_PR.append(self.precision)
        self.recall_PR.append(self.recall)

    

