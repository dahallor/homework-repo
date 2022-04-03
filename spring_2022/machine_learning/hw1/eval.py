import numpy as np
import math

class Evaluation():
    def __init__(self):
        pass

    def calcYhat(self, X, w):
        Yhat = X.dot(w)
        return Yhat

    def RSME(self, Y, Yhat):
        N = Y.shape[0]
        sum = 0

        for i in range(len(Y)):
            temp = Yhat[i][0] - Y[i][0]
            temp2 = math.pow(temp, 2)
            sum += temp2

        MSE = (1/N) * sum
        RMSE = np.sqrt(MSE)

        '''
        dif = Yhat - Y
        #print(Yhat, Y, N)
        print(dif)
        difT = dif.transpose()
        all = difT * dif
        print(all)
        RMSE = np.sqrt((1/N) * (dif.transpose() * dif))

        '''

        return RMSE

    def MAPE(self, Y, Yhat):
        N = Y.shape[0]
        sum = 0

        for i in range(len(Y)):
            temp = (Y[i][0] - Yhat[i][0])/Y[i][0]
            temp2 = abs(temp)
            sum += temp2
        
        MAPE = (1/N) * sum
        return MAPE