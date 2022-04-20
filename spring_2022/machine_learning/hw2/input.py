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
        self.trainX1v2 = np.array([])
        self.trainY1v2 = np.array([])
        self.trainX1v3 = np.array([])
        self.trainY1v3 = np.array([])
        self.trainX2v3 = np.array([])
        self.trainY2v3 = np.array([])
        self.validX1v2 = np.array([])
        self.validY1v2 = np.array([])
        self.validX1v3 = np.array([])
        self.validY1v3 = np.array([])
        self.validX2v3 = np.array([])
        self.validY2v3 = np.array([])

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

    def setMulticlassData(self, set):
        for i in range(len(self.trainX)):
            match set:
                case "1v2":
                    #pdb.set_trace()
                    if self.trainY[i] == 1:
                        self.trainX1v2 = np.append(self.trainX1v2, self.trainX[i])
                        self.trainY1v2 = np.append(self.trainY1v2, 1)
                    if self.trainY[i] == 2:
                        self.trainX1v2 = np.append(self.trainX1v2, self.trainX[i])
                        self.trainY1v2 = np.append(self.trainY1v2, 0)
                    if i == len(self.trainX) - 1:
                        size = len(self.trainY1v2)
                        self.trainX1v2 = np.reshape(self.trainX1v2, (size, len(self.trainX[0])))
                        self.trainY1v2 = np.reshape(self.trainY1v2, (size, 1))
                case "1v3":
                    if self.trainY[i] == 1:
                        self.trainX1v3 = np.append(self.trainX1v3, self.trainX[i])
                        self.trainY1v3 = np.append(self.trainY1v3, 1)
                    if self.trainY[i] == 3:
                        self.trainX1v3 = np.append(self.trainX1v3, self.trainX[i])
                        self.trainY1v3 = np.append(self.trainY1v3, 0)
                    if i == len(self.trainX) - 1:
                        size = len(self.trainY1v3)
                        self.trainX1v3 = np.reshape(self.trainX1v3, (size, len(self.trainX[0])))
                        self.trainY1v3 = np.reshape(self.trainY1v3, (size, 1))
                case "2v3":
                    if self.trainY[i] == 2:
                        self.trainX2v3 = np.append(self.trainX2v3, self.trainX[i])
                        self.trainY2v3 = np.append(self.trainY2v3, 1)
                    if self.trainY[i] == 3:
                        self.trainX2v3 = np.append(self.trainX2v3, self.trainX[i])
                        self.trainY2v3 = np.append(self.trainY2v3, 0)
                    if i == len(self.trainX) - 1:
                        size = len(self.trainY2v3)
                        self.trainX2v3 = np.reshape(self.trainX2v3, (size, len(self.trainX[0])))
                        self.trainY2v3 = np.reshape(self.trainY2v3, (size, 1))
                case _:
                    raise Exception

        for i in range(len(self.validX)):
            match set:
                case "1v2":
                    if self.validY[i] == 1:
                        self.validX1v2 = np.append(self.validX1v2, self.validX[i])
                        self.validY1v2 = np.append(self.validY1v2, 1)
                    if self.validY[i] == 2:
                        self.validX1v2 = np.append(self.validX1v2, self.validX[i])
                        self.validY1v2 = np.append(self.validY1v2, 0)
                    if i == len(self.validX) - 1:
                        size = len(self.validY1v2)
                        self.validX1v2 = np.reshape(self.validX1v2, (size, len(self.validX[0])))
                        self.validY1v2 = np.reshape(self.validY1v2, (size, 1))
                case "1v3":
                    if self.validY[i] == 1:
                        self.validX1v3 = np.append(self.validX1v3, self.validX[i])
                        self.validY1v3 = np.append(self.validY1v3, 1)
                    if self.validY[i] == 3:
                        self.validX1v3 = np.append(self.validX1v3, self.validX[i])
                        self.validY1v3 = np.append(self.validY1v3, 0)
                    if i == len(self.validX) - 1:
                        size = len(self.validY1v3)
                        self.validX1v3 = np.reshape(self.validX1v3, (size, len(self.validX[0])))
                        self.validY1v3 = np.reshape(self.validY1v3, (size, 1))
                case "2v3":
                    if self.validY[i] == 2:
                        self.validX2v3 = np.append(self.validX2v3, self.validX[i])
                        self.validY2v3 = np.append(self.validY2v3, 1)
                    if self.validY[i] == 3:
                        self.validX2v3 = np.append(self.validX2v3, self.validX[i])
                        self.validY2v3 = np.append(self.validY2v3, 0)
                    if i == len(self.validX) - 1:
                        size = len(self.validY2v3)
                        self.validX2v3 = np.reshape(self.validX2v3, (size, len(self.validX[0])))
                        self.validY2v3 = np.reshape(self.validY2v3, (size, 1))
                case _:
                    raise Exception


    def setMeanAndSTD(self, data):
        self.mean = np.mean(data, axis = 0)
        self.std = np.std(data, axis = 0)
        
    def zScore(self, inputType):
        z = np.array([])
        match inputType:
            case "train":
                data = self.trainX
            case "valid":
                data = self.validX
            case "train1v2":
                data = self.trainX1v2
            case "train1v3":
                data = self.trainX1v3
            case "train2v3":
                data = self.trainX2v3
            case "valid1v2":
                data = self.validX1v2
            case "valid1v3":
                data = self.validX1v3
            case "valid2v3":
                data = self.validX2v3
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
            case "train1v2":
                self.trainX1v2 = z
            case "train1v3":
                self.trainX1v3 = z
            case "train2v3":
                self.trainX2v3 = z
            case "valid1v2":
                self.validX1v2 = z
            case "valid1v3":
                self.validX1v3 = z
            case "valid2v3":
                self.validX2v3 = z
            case _:
                raise Exception
        