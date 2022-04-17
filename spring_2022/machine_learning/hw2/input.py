import numpy as np
import pdb

class InputLayer:
    def __init__(self):
        self.mean = 0
        self.std = 0
        self.trainX = 0
        self.trainY = 0
        self.validX = 0
        self.validY = 0

    def getSpamItems(self):
        data = np.genfromtxt('spambase.data', delimiter = ",")
        return data

    def alterIrisData(self):
        f = open("iris.data", "r")
        g = open("irisAltered.csv", "w")
        lines = f.readlines()
        for line in lines:
            temp = line.split(",")
            value = temp[-1]
            value = value.strip("\n")
            print(value)
            match value:
                case "Iris-setosa":
                    temp[-1] = 1
                case "Iris-versicolor":
                    temp[-1] = 2
                case  "Iris-virginica":
                    temp[-1] = 3
                case _:
                    continue
            for i in range(len(temp)):
                if i == len(temp)-1:
                    temp[i] = int(temp[i])
                else:
                    temp[i] = float(temp[i])
            g.write("{:.1f},{:.1f},{:.1f},{:.1f},{}\n".format(temp[0], temp[1], temp[2], temp[3], temp[4]))

    def getIrisItems(self):
        data = np.genfromtxt('irisAltered.csv', delimiter = ",")
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

    def setMeanAndSTD(self, data):
        self.mean = np.mean(data, axis = 0)
        self.std = np.std(data, axis = 0)
        
    def zScore(self, inputType):
        z = np.array([])
        if inputType == "train":
            data = self.trainX
        if inputType == "valid":
            data = self.validX
        for i in range(len(data)):
            temp = np.subtract(data[i], self.mean)/self.std
            z = np.append(z, temp)

        z = z.reshape((len(data), len(data[0])))

        if inputType == "train":
            self.trainX = z
        if inputType == "valid":
            self.validX = z
        