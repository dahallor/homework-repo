from base_class import *
import numpy as np

class FullyConnectedLayer(Layer):
    def __init__(self, sizeIn, sizeOut):
        super().__init__()
        np.random.seed(0)
        W = np.zeros((sizeIn, sizeOut), dtype = float, order = 'C')
        rand = np.random.uniform(low=-.0001, high=.0002, size = sizeIn*sizeOut)
        b = np.random.uniform(low = -.0001, high = .0002, size = sizeOut)
        self.setBias(b)
        count = 0
        for i in range(sizeOut):
            for j in range(sizeIn):
                W[j][i] = rand[count]
                count += 1
        self.sizeIn = sizeIn
        self.sizeOut = sizeOut
        self.setWeights(W)

    def getWeights(self):
        return self.weights

    def setWeights(self, weights):
        self.weights = weights

    def getBias(self):
        return self.bias

    def setBias(self, bias):
        self.bias = bias

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        W = self.getWeights()
        b = self.getBias()
        h = dataIn.dot(W)
        Y = h + b
        self.setPrevOut(Y)
        return Y


    def gradient(self):
        W = self.getWeights()
        delta = np.transpose(W)
        return delta