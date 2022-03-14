from tempfile import tempdir
from base_class import *
from input import *
import numpy
import math
import pdb

class LinearLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        Y = (dataIn)
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        Y = self.getPrevOut()
        k = len(Y[0])
        delta = numpy.zeros((k, k), dtype = float, order = 'C')

        for i in range(k):
            for j in range(k):
                if i == j:
                    delta[i][j] = 1
        return delta


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
        Y = self.getPrevIn()
        k = len(Y[0])
        delta = numpy.zeros((k, k), dtype = float, order = 'C')
        for a in range(len(Y)):
            for i in range(k):
                for j in range(k):
                    if i == j and Y[a][i] > 0:
                        delta[i][j] = 1
        return delta
    
class SigmoidLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        Y = 1/(1+numpy.exp(-dataIn))
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        epsilon = .0000001
        Y = self.getPrevOut()
        #print(Y)
        k = len(Y[0]) 
        n = len(Y)
        delta = numpy.zeros((n, k, k), dtype = float, order = 'C')

        #print(delta)


        for a in range(n):
            delta[a] = np.diag(Y[a])

        #pdb.set_trace()
        return delta

class SoftmaxLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        a = len(dataIn)
        b = len(dataIn[0])
        Y = numpy.zeros((a, b), dtype=float, order = 'C')
        #pdb.set_trace()
        for i in range(a):
            sum = 0
            for j in range(b):
                sum += numpy.exp(dataIn[i][j])
            for j in range(b):
                Y[i][j] = numpy.exp(dataIn[i][j])/sum
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        Y = self.getPrevOut()
        k = len(Y[0])
        n = len(Y)
        delta = numpy.zeros((n, k, k), dtype = float, order = 'C')
        for a in range(n):
            for i in range(k):
                for j in range(k):
                    pdb.set_trace
                    if i == j:
                        delta[a][i][j] = Y[a][j] * (1 - Y[a][j])
                    else:
                        delta[a][i][j] = -1 * (Y[a][i] * Y[a][j])
        return delta
    
class TanhLayer(Layer):
    def __init__(self):
        super().__init__()

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        Y = (numpy.exp(dataIn) - numpy.exp(-dataIn))/(numpy.exp(dataIn) + numpy.exp(-dataIn))
        self.setPrevOut(Y)
        return Y

    def gradient(self):
        epsilon = .0000001
        Y = self.getPrevOut()
        k = len(Y[0])
        delta = numpy.zeros((k, k), dtype = float, order = 'C')
        for a in range(len(Y)):
            for i in range(k):
                for j in range(k):
                    if i == j:
                        delta[i][j] = (1 - math.pow(Y[a][j], 2)) + epsilon
        return delta

 
    