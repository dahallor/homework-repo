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
        J = np.zeros((len(y), 1), dtype = 'float')
        for i in range(len(J)):
            J[i][0] = -1 * ((y[i][0] * np.log((yhat[i][0] + epsilon))) + (1 - y[i][0]) * np.log((1 - yhat[i][0] + epsilon)))
        if input_type == "train":
            mean = np.mean(J)
            self.meanTrain.append(mean)
        if input_type == "valid":
            mean = np.mean(J)
            self.meanValid.append(mean)

    def evalMulticlass(self, y, yhat, input_type):
        epsilon = .0000001
        J = np.zeros((len(y), 1), dtype = 'float')
        for i in range(len(J)):
            J[i][0] = -1 * ((y[i][0] * np.log((yhat[i][0] + epsilon))) + (1 - y[i][0]) * np.log((1 - yhat[i][0] + epsilon)))
        if input_type == "1v2":
            mean = np.mean(J)
            self.mean1v2.append(mean)
        if input_type == "1v3":
            mean = np.mean(J)
            self.mean1v3.append(mean)
        if input_type == "2v3":
            mean = np.mean(J)
            self.mean2v3.append(mean)