import numpy as np

class Weights:
    def __init__(self, data):
        x = len(data)
        self.W = np.zeros((len(data[0]), 1), dtype = float)
        self.b = np.random.uniform(low = -.0001, high = .0002)
        for i in range(len(data[0])):
            rand = np.random.uniform(low=-.0001, high=.0002)
            self.W[i][0] = rand

    def setWeights(self, X, Y):

        Xt = X.transpose()
        product = np.matmul(Xt, X)
        product2 = np.linalg.inv(product)
        product3 = np.matmul(product2, Xt)
        w = np.matmul(product3, Y)

        self.W = w

    def calcYhat(self, X):
        Yhat = np.matmul(X, self.W)
        return Yhat