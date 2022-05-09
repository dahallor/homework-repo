import numpy as np

class InputLayer:
    def __init__(self):
        self.mean = 0
        self.std = 0

    def getData(self):
        pass

    def shuffleData(self):
        pass

    def setMeanAndSTD(self, data):
        self.mean = np.mean(data, axis = 0)
        self.std = np.std(data, axis = 0)

    def zScore(self, data):
        z = np.array([])
        for i in range(len(data)):
            temp = np.subtract(data[i], self.mean)/self.std
            z = np.append(z, temp)

        z = z.reshape((len(data), len(data[0])))
        return z