import numpy as np

class InputLayer:
    def __init__(self):
        self.mean = 0
        self.std = 0

    def getData(self):
        data = np.genfromtxt("lfw20.csv", delimiter = ",")
        return data

    def splitData(self, data):
        trans = data.transpose()
        Yt = trans[0]
        Y = np.array([Yt])
        Y = Y.transpose()
        X = np.delete(data, 0, axis = 1)
        return X, Y

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

    def reshape(self, temp):
        X = np.array([])
        for i in range(len(temp)):
            image = temp[i]
            X = np.append(X, image.reshape(87, 65))
        return X

        return X.reshape(87, 65)

    