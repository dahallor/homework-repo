import numpy as np
import pdb

class LogLoss:
    def __init__(self):
        self.meanTrain = []
        self.mean1v2 = []
        self.mean1v3 = []
        self.mean2v3 = []
        self.meanValid = []

    def eval(self, y, yhat, input_type):
        epsilon = .0000001

        if input_type == "1v2" or input_type == "1v3" or input_type == "2v3":
            y, yhat = self.setTempYhat(y, yhat, input_type)

        J = np.zeros((len(y), 1), dtype = 'float')
        for i in range(len(J)):
            J[i][0] = -1 * ((y[i][0] * np.log((yhat[i][0] + epsilon))) + (1 - y[i][0]) * np.log((1 - yhat[i][0] + epsilon)))
        if input_type == "train":
            mean = np.mean(J)
            self.meanTrain.append(mean)
        if input_type == "valid":
            mean = np.mean(J)
            self.meanValid.append(mean)
        if input_type == "1v2":
            mean = np.mean(J)
            self.mean1v2.append(mean)
        if input_type == "1v3":
            mean = np.mean(J)
            self.mean1v3.append(mean)
        if input_type == "2v3":
            mean = np.mean(J)
            self.mean2v3.append(mean)

    def setTempYhat(self, y, yhat, input_type):
        tempYhat = np.array([])
        tempY = np.array([])
        for i in range(len(y)):
            match input_type:
                case "1v2":
                    if y[i] == 1 or y[i] == 2:
                        tempYhat = np.append(tempYhat, yhat[i])
                        tempY = np.append(tempY, y[i])
                case "1v3":
                    if y[i] == 1 or y[i] == 3:
                        tempYhat = np.append(tempYhat, yhat[i])
                        tempY = np.append(tempY, y[i])
                case "2v3":
                    if y[i] == 2 or y[i] == 3:
                        tempYhat = np.append(tempYhat, yhat[i])
                        tempY = np.append(tempY, y[i])
                case _:
                    raise Exception
        size = len(tempYhat)
        newYhat = np.reshape(tempYhat, (size, 1))
        newY = np.reshape(tempYhat, (size, 1))

        return newY, newYhat