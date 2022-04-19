import numpy as np
import pdb

class Weights:
    def __init__(self, data):
        self.W = np.zeros((len(data[0]), 1), dtype = float)
        self.W_1v2 = np.zeros((len(data[0]), 1), dtype = float)
        self.W_1v3 = np.zeros((len(data[0]), 1), dtype = float)
        self.W_2v3 = np.zeros((len(data[0]), 1), dtype = float)
        self.b = np.random.uniform(low = -.0001, high = .0002)
        self.b_1v2 = np.random.uniform(low = -.0001, high = .0002)
        self.b_1v3 = np.random.uniform(low = -.0001, high = .0002)
        self.b_2v3 = np.random.uniform(low = -.0001, high = .0002)
        self.dJdW = 0
        self.dJdb = 0
        for i in range(len(data[0])):
            rand = np.random.uniform(low=-.0001, high=.0002)
            self.W[i][0] = rand

            rand = np.random.uniform(low=-.0001, high=.0002)
            self.W_1v2[i][0] = rand

            rand = np.random.uniform(low=-.0001, high=.0002)
            self.W_1v3[i][0] = rand

            rand = np.random.uniform(low=-.0001, high=.0002)
            self.W_2v3[i][0] = rand

    def updateWeightsAndBias(self, eta):
        self.W = self.W - eta * self.dJdW
        self.b = self.b - eta * self.dJdb

    def updateWAndBMulticlass(self, eta, type):
        match type:
            case "1v2":
                self.W_1v2 = self.W_1v2 - eta * self.dJdW
                self.b_1v2 = self.b_1v2 - eta * self.dJdb       
            case "1v3":
                self.W_1v3 = self.W_1v3 - eta * self.dJdW
                self.b_1v3 = self.b_1v3 - eta * self.dJdb
            case "2v3":
                self.W_2v3 = self.W_2v3 - eta * self.dJdW
                self.b_2v3 = self.b_2v3 - eta * self.dJdb
            case _:
                raise Exception

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
        

    


