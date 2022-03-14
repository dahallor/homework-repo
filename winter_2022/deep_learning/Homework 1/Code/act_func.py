from tempfile import tempdir
from base_class import *
from input import *
import numpy

class LinearLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        Y = (dataIn)
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        pass

class ReLuLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        Y = dataIn
        for i in range(len(Y)):
            for j in range(len(Y[i])):
                if Y[i][j] < 0:
                    Y[i][j] = 0
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        pass
    
class SigmoidLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        Y = 1/(1+numpy.exp(-dataIn))
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        pass

class SoftmaxLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        a = len(dataIn)
        b = len(dataIn[0])
        Y = numpy.zeros((a, b), dtype=float, order = 'C')
        for i in range(a):
            sum = 0
            for j in range(b):
                sum += numpy.exp(dataIn[i][j])
            for j in range(b):
                Y[i][j] = numpy.exp(dataIn[i][j])/sum
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        pass
    
class TanhLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        Y = (numpy.exp(dataIn) - numpy.exp(-dataIn))/(numpy.exp(dataIn) + numpy.exp(-dataIn))
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        pass
    