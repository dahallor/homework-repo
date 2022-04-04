import numpy as np

class InputLayer:
    def __init__(self):
        pass

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
        foldsXvalid = foldsX[index-1]
        foldsYvalid = foldsY[index-1]
        foldsXtrain = np.delete(foldsX, index-1, axis = 0)
        foldsYtrain = np.delete(foldsY, index-1, axis = 0)

        return foldsXtrain, foldsYtrain, foldsXvalid, foldsYvalid

        '''
        print(foldsXvalid)
        print("------------------------------------------------------------")
        print(foldsX)
        print("------------------------------------------------------------")
        print(foldsXtrain)
        input()
        '''
        
