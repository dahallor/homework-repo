from base_class import *
import statistics
import numpy

class InputLayer(Layer):
    def __init__(self, dataIn):
        super().__init__()
        '''
        temp_mean = numpy.array([])
        temp_std = numpy.array([])
        for i in range(len(dataIn[0])):
            t1 = statistics.mean(dataIn[:,i])
            t2 = statistics.stdev(dataIn[:,i])
    
            temp_mean = numpy.append(temp_mean, t1)
            if t2 == 0:
                temp_std = numpy.append(temp_std, 1)
            else:
                temp_std = numpy.append(temp_std, t2)
        self.meanX = temp_mean
        self.stdX = temp_std
        '''
        self.meanX = np.mean(dataIn, axis = 0, dtype = np.float64)
        self.stdX = np.std(dataIn, axis = 0, dtype = np.float64)
        


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
    