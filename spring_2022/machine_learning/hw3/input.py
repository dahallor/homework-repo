import numpy as np

class InputLayer:
    def __init__(self):
        self.mean = 0
        self.std = 0
        self.var = 0
        self.median = 0

        self.trainX = 0
        self.trainY = 0
        self.validX = 0
        self.validY = 0

        self.train = np.array([[]])

        self.trainX0 = np.array([])
        self.trainX1 = np.array([])
    
        self.trainY0 = np.array([])
        self.trainY1 = np.array([])

        self.debugX = np.array([])
        self.debugY = np.array([])

    def getSpamItems(self):
            data = np.genfromtxt('spambase.data', delimiter = ",")
            return data
    
    def getCartData(self):
            data = np.genfromtxt('CTG.csv', delimiter = ",")
            data = np.delete(data, 0, axis = 0)
            data = np.delete(data, 0, axis = 0)
            data = np.delete(data, -2, axis = 1)
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

        self.trainX = X[:training_size]
        self.trainY = Y[:training_size]
        self.validX = X[training_size:]
        self.validY = Y[training_size:]

        self.debugX = np.arange(70)
        self.debugX.reshape(7,10)
        self.debugY = np.array([[1], [0], [0], [1], [0], [0], [1], [0], [1], [1]])

    def setStatsInfo(self, data):
        self.mean = np.mean(data, axis = 0)
        self.std = np.std(data, axis = 0)
        self.var = np.var(data, axis = 0)
        
    def zScore(self, inputType):
        z = np.array([])
        match inputType:
            case "train":
                data = self.trainX
            case "valid":
                data = self.validX
            case "debug":
                data = self.debugX
            case _:
                raise Exception


        for i in range(len(data)):
            temp = np.subtract(data[i], self.mean)/self.std
            z = np.append(z, temp)

        z = z.reshape((len(data), len(data[0])))

        match inputType:
            case "train":
                self.trainX = z
            case "valid":
                self.validX = z
            case "debug":
                self.debugX = z
            case _:
                raise Exception

    def setZscoredMedian(self):
        self.median = np.median(self.trainX, axis = 0)



