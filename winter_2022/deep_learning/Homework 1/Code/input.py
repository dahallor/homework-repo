from base_class import *
import numpy

class InputLayer(Layer):
    def __init__(self, dataIn):
        t1 = numpy.mean(dataIn, axis=0, dtype = "float")
        t2 = numpy.std(dataIn, axis = 0, dtype = "float")
        self.meanX = t1
        self.stdX = t2

    def forward(self, dataIn):
        self.setPrevIn(dataIn)
        row = len(dataIn)
        col = len(dataIn[0])
        z_data = numpy.zeros((row, col), dtype = float, order = 'C')
        for i in range(len(dataIn)):
            for j in range(len(dataIn[i])):
                mu = self.meanX[j]
                sigma = self.stdX[j]
                x = dataIn[i][j]
                z = (x-mu)/sigma
                z_data[i][j] = z
        self.setPrevOut(z_data)
        return z_data
            


    def gradient(self):
        pass
    