import numpy as np
import pdb

class Weights:
    def __init__(self, data):
        self.W = np.zeros((len(data[0]), 1), dtype = float)
        self.b = np.random.uniform(low = -.0001, high = .0002)
        self.dJdW = 0
        self.dJdb = 0
        for i in range(len(data[0])):
            rand = np.random.uniform(low=-.0001, high=.0002)
            self.W[i][0] = rand

    def updateWeightsAndBias(self, eta):
        self.W = self.W - eta * self.dJdW
        self.b = self.b - eta * self.dJdb

    def set_dJdW(self, X, Y, Yhat):
        Xt = X.transpose()
        N = len(X)
        dif = Yhat - Y
        w = np.matmul(Xt, dif)
        self.dJdW = (1/N) * w

    def set_dJdb(self, Y, Yhat):
        sum = 0
        N = len(Y)
        for i in range(N):
            sum += Yhat[i][0] - Y[i][0]
        self.dJdb = (1/N) * sum

    


