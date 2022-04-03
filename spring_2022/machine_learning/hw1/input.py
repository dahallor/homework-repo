import numpy as np

class InputLayer:
    def __init__(self):
        pass

    def getCSVItems(self):
        data = np.genfromtxt('x06Simple.csv', dtype = int, delimiter = ",", skip_header = 1, )
        return data

    def shuffleData(self, data):
        np.random.shuffle(data)
        return data

    def splitData(self, data):
        data = np.delete(data, 0, axis = 1)

        trans = data.transpose()
        Yt = trans[0]
        Y = np.array([Yt])
        Y = Y.transpose()
        X = np.delete(data, 0, axis = 1)

        training_size = int(np.ceil(len(data) * (2/3)))

        trainX = X[:training_size]
        trainY = Y[:training_size]
        validX = X[training_size:]
        validY = Y[training_size:]

        return trainX, trainY, validX, validY

    def addDummyValue(self, trainX):
        trainX = np.insert(trainX, 0, 1, axis = 1)
        return trainX
        '''
        trainY = np.insert(trainY, 0, 1, axis = 1)
        validX = np.insert(validX, 0, 1, axis = 1)
        validY = np.insert(validY, 0, 1, axis = 1)
        return trainX, trainY, validX, validY
        '''