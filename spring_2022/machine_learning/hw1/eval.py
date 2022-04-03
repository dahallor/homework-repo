import numpy as np

class Evaluation():
    def __init__(self):
        pass

    def calcYhat(self, X, w):
        Yhat = X.dot(w)
        return Yhat

    def RSME(self, Y, Yhat):
        N = Y.shape[0]
        dif = Yhat - Y
        #print(Yhat, Y, N)
        print(dif)
        difT = dif.transpose()
        all = difT * dif
        print(all)
        RMSE = np.sqrt((1/N) * (dif.transpose() * dif))

        return RMSE

    def MAPE(self, Y, Yhat):
        pass