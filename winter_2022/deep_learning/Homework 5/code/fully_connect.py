from base_class import *
import numpy as np
import pdb
from ADAM import *



class FullyConnectedLayer(Layer):
    def __init__(self, sizeIn, sizeOut):
        super().__init__()
        np.random.seed(0)
        W = np.zeros((sizeIn, sizeOut), dtype = float, order = 'C')
        rand = np.random.uniform(low=-.0001, high=.0002, size = sizeIn*sizeOut)
        b = np.random.uniform(low = -.0001, high = .0002, size = sizeOut)
        self.setBias(b)
        count = 0
        self.s = np.zeros((sizeIn, sizeOut))
        self.r = np.zeros((sizeIn, sizeOut))

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

    def backward(self, gradIn, eta, epoch):
        gradOut = super().backward(gradIn, eta, epoch)
        self.updateWeights(gradIn, eta, epoch)
        return gradOut

    def updateWeights(self, gradIn, eta, epoch):
        pi = self.getPrevIn()
        po = self.getPrevOut()

        dJdW = pi.T@gradIn
        dJdb = np.sum(gradIn,0)
        #epoch = getEpoch()
        #print("FC")
        #pdb.set_trace()
        rho1 = .9
        rho2 = .999
        delta = .00000001
        
        self.s = (rho1 * self.s) + (1-rho1) * dJdW
        self.r = (rho2 * self.r) + (1-rho2) * (dJdW * dJdW)



        #pdb.set_trace()
        self.weights -= eta * ((self.s / (1 - rho1)) / (np.sqrt(self.r / (1 - rho2)) + delta))
        self.bias -= eta*dJdb/pi.shape[0]
        

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        W = self.getWeights()
        b = self.getBias()
        #pdb.set_trace()
        h = dataIn.dot(W)
        Y = h + b
        self.setPrevOut(Y)
        return Y


    def gradient(self):
        W = self.getWeights()
        delta = np.transpose(W)
        return delta

    #implement update weights method, Use self, gradin, eta