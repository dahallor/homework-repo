from abc import ABC, abstractmethod


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

    def backward(self, gradIn):
        pass

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