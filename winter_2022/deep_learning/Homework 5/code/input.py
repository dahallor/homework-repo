from base_class import *
import statistics
import numpy
import pdb

class InputLayer(Layer):
    def __init__(self, dataIn):
        super().__init__()
        temp_mean = numpy.array(numpy.mean(dataIn, axis = 0))
        temp_std = numpy.array(numpy.std(dataIn, axis = 0))

        for i in range(len(temp_std)):
            if temp_std[i] == 0:
                temp_std[i] = 1
        self.meanX = temp_mean
        self.stdX = temp_std



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
    