from abc import ABC, abstractmethod
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

    def backward(self, gradIn, eta):
        sg = self.gradient()

        grad = np.zeros((gradIn.shape[0], sg.shape[2]))
        pdb.set_trace()
        grad = gradIn * sg
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