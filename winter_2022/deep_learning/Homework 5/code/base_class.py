from abc import ABC, abstractmethod
import math
import numpy as np
import pdb

class Layer(ABC):
    def __init__(self):
        self.__prevIn = []
        self.__prevOut = []
    
    def setPrevIn(self, dataIn):
        self.__prevIn = dataIn

    def setPrevOut(self, out):
        self.__prevOut = out

    def getPrevIn(self):
        return self.__prevIn

    def getPrevOut(self):
        return self.__prevOut

    def backward(self, gradIn, eta, epoch):
        sg = self.gradient()
        try:
            grad = np.zeros((gradIn.shape[0],sg.shape[2]))
            for i in range(gradIn.shape[0]):
                for j in range(sg.shape[1]):
                    grad[i][j] = gradIn[i]@sg[i][j]
        except Exception:
            grad = np.zeros((gradIn.shape[0],sg.shape[1]))
            grad = gradIn@sg
        #pdb.set_trace()
        return grad

    @abstractmethod
    def forward(self, dataIn):
        pass

    @abstractmethod
    def gradient(self):
        pass

class Objective(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def eval(self, y, yhat):
        pass

    @abstractmethod
    def gradient(self, y, yhat):
        pass