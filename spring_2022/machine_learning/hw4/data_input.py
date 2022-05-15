import numpy as np
import pdb

class InputLayer:
    def __init__(self):
        self.mean = 0
        self.std = 0

        self.mean_c1 = 0
        self.mean_c2 = 0
        self.std_c1 = 0
        self.std_c2 = 0

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

    def splitDataP3(self, data):
        trans = data.transpose()
        Yt = trans[0]
        Y = np.array([Yt])
        Y = Y.transpose()
        X = np.delete(data, 0, axis = 1)

        training_size = int(np.ceil(len(data) * (2/3)))

        self.trainX = X[:training_size]
        self.trainY = Y[:training_size]
        self.validX = X[training_size:]
        self.validY = Y[training_size:]

    def shuffleData(self, data, num):
        np.random.seed(num)
        np.random.shuffle(data)
        return data

    def setMeanAndSTD(self, data):
        self.mean = np.mean(data, axis = 0)
        self.std = np.std(data, axis = 0, ddof = 1)

    def setMeanByClass(self, X):
        X_class1 = X[:5]
        X_class2 = X[5:]

        self.mean_c1 = np.mean(X_class1, axis=0)
        self.mean_c2 = np.mean(X_class2, axis=0)
        print("Means")
        print(self.mean_c1)
        print(self.mean_c2)
        print()

        x = X_class1 - self.mean_c1
        xt = x.transpose()
        self.std_c1 = np.matmul(xt, x)

        x = X_class2 - self.mean_c2
        xt = x.transpose()
        self.std_c2 = np.matmul(xt, x)
        
        print("Sigmas")
        print(self.std_c1)
        print(self.std_c2)
        print()




    def zScore(self, data):
        z = np.array([])
        for i in range(len(data)):
            temp = np.subtract(data[i], self.mean)/self.std
            z = np.append(z, temp)

        z = z.reshape((len(data), len(data[0])))
        return z



    