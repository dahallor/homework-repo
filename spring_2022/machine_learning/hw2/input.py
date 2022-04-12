import numpy as np

class InputLayer:
    def __init__(self):
        self.mean = 0
        self.std = 0

    def getSpamItems(self):
        data = np.genfromtxt('spambase.data', delimiter = ",")
        return data

    def getIrisItems(self):
        data = np.genfromtxt('iris.data', delimiter = ",")
        return data

    def shuffleData(self, data, num):
        np.random.seed(num)
        np.random.shuffle(data)
        return data

    def splitDataSpam(self, data):
        trans = data.transpose()
        Yt = trans[-1]
        Y = np.array([Yt])
        Y = Y.transpose()
        X = np.delete(data, -1, axis = 1)

        training_size = int(np.ceil(len(data) * (2/3)))

        trainX = X[:training_size]
        trainY = Y[:training_size]
        validX = X[training_size:]
        validY = Y[training_size:]

        return trainX, trainY, validX, validY

    def setMeanAndSTD(self, data):
        self.mean = np.mean(data, axis = 0)
        self.std = np.std(data, axis = 0)
        
    def zScore(self, data):
        z = np.array([])
        for i in range(len(data)):
            #pdb.set_trace()
            temp = np.subtract(data[i], self.mean)/self.std
            z = np.append(z, temp)

        z = z.reshape((len(data), len(data[0])))

        return z