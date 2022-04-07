import numpy as np
import math

class Evaluation():
    def __init__(self):
        pass

    def calcYhat(self, X, w):
        Yhat = X.dot(w)
        return Yhat

    def SE(self, Y, Yhat, errors):
        for i in range(len(Y)):
            J = Y[i] - Yhat[i]
            errors = np.append(errors, J)

        return errors
    
    def RSME(self, Y, Yhat):
        N = Y.shape[0]
        sum = 0

        for i in range(len(Y)):
            temp = Yhat[i][0] - Y[i][0]
            temp2 = math.pow(temp, 2)
            sum += temp2

        MSE = (1/N) * sum
        RMSE = np.sqrt(MSE)

        return RMSE

    def RMSEfromSE(self, SEs):
        sum = np.sum(SEs)
        mean = (1/len(SEs)) * sum
        root = np.sqrt(mean)
        return root

    def MAPE(self, Y, Yhat):
        N = Y.shape[0]
        sum = 0

        for i in range(len(Y)):
            temp = (Y[i][0] - Yhat[i][0])/Y[i][0]
            temp2 = abs(temp)
            sum += temp2
        
        MAPE = (1/N) * sum
        return MAPE

    def SMAPE(self, Y, Yhat):
        N = Y.shape[0]
        sum = 0

        for i in range(len(Y)):
            top = abs(Yhat[i] - Y[i])
            bottom = (abs(Y[i]) - abs(Yhat[i]))/2
            value = top/bottom
            sum += value

        SMAPE = (1/N) * sum
        return SMAPE