import numpy as np
import pdb

class InputLayer:
    def __init__(self):
        self.std = 0
        self.mean = 0

    def getCSVItems(self):
        data = np.genfromtxt('x06Simple.csv', dtype = int, delimiter = ",", skip_header = 1, )
        return data

    def shuffleData(self, data, num):
        np.random.seed(num)
        np.random.shuffle(data)
        return data

    def splitDataDirect(self, data):
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

    def splitDataCrossValidation(self, data):
        data = np.delete(data, 0, axis = 1)

        trans = data.transpose()
        Yt = trans[0]
        Y = np.array([Yt])
        Y = Y.transpose()
        X = np.delete(data, 0, axis = 1)
        return X, Y

    def addDummyValueDirect(self, trainX, validX):
        trainX = np.insert(trainX, 0, 1, axis = 1)
        validX = np.insert(validX, 0, 1, axis = 1)
        return trainX, validX

    def addDummyValueCrossValidation(self, X):
        X = np.insert(X, 0, 1, axis = 1)
        return X

    def S_folds(self, index, S, X, Y):
        foldsX = np.reshape(X, (-1, (len(X)//S), len(X[0])))
        foldsY = np.reshape(Y, (-1, (len(Y)//S), len(Y[0])))
        foldsXvalid = foldsX[index]
        foldsYvalid = foldsY[index]
        foldsXtrain = np.delete(foldsX, index-1, axis = 0)
        foldsYtrain = np.delete(foldsY, index-1, axis = 0)

        return foldsXtrain, foldsYtrain, foldsXvalid, foldsYvalid

    def N_folds(self, index, X, Y):
        validX = X[index]
        validY = Y[index]
        trainX = np.delete(X, index, axis = 0)
        trainY = np.delete(Y, index, axis = 0)

        return trainX, trainY, validX, validY
    
    def reassemble(self, trainX, trainY):
        heightX = len(trainX) * len(trainX[0])
        widthX = len(trainX[0][0])
        trainX = np.reshape(trainX, (heightX, widthX))

        heightY = len(trainY) * len(trainY[0])
        widthY= len(trainY[0][0])
        trainY = np.reshape(trainY, (heightY, widthY))
        
        return trainX, trainY
        

    def getDimensionality(self, S, X):
        foldsX = np.reshape(X, (-1, (len(X)//S), len(X[0])))
        size = len(foldsX)
        return size


    def setMeanAndSTD(self, data):
        self.mean = np.mean(data, axis = 0)
        self.std = np.std(data, axis = 0)
        
    def zScore(self, data):
        z = np.array([])
        for i in range(len(data)):
            #pdb.set_trace()
            temp = np.subtract(data[i], self.mean)/self.std
            z = np.append(z, temp)

        z = z.reshape((len(data), 4))

        return z
