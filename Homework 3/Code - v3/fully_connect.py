from base_class import *
import numpy as np
import pdb

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

    def backward(self, gradIn, eta):
        gradOut = super().backward(gradIn, eta)

        pi = self.getPrevIn()
        po = self.getPrevOut()

        dJdW = pi.T@gradIn
        dJdb = np.sum(gradIn,0)

        self.weights -= eta*dJdW/pi.shape[0]
        self.bias -= eta*dJdb/pi.shape[0]
        #pdb.set_trace()
        return gradOut

    def updateWeights(self, gradIn, eta = .0001):
        x = gradIn.shape[0]
        dJdb = np.sum(gradIn, axis = 0)
        dJdW = (self.getPrevIn().T @ gradIn)

        #pdb.set_trace()
        self.weights = self.weights - (eta * dJdW)/x
        self.bias = self.bias - (eta * dJdb)/x

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

    #implement update weights method, Use self, gradin, eta