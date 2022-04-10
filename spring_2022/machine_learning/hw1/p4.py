from input import *
from weights import *
from eval import *
import pdb
import math
import numpy as np

if __name__ == '__main__':
    inputLayer = InputLayer()
    weights = Weights()
    eval = Evaluation()

    data = inputLayer.getCSVItems()
    inputLayer.setMeanAndSTD(data)
    data = inputLayer.zScore(data)
    shuffled_data = inputLayer.shuffleData(data, 0)
    trainX, trainY, validX, validY = inputLayer.splitDataDirect(shuffled_data)
    trainX, validX = inputLayer.addDummyValueDirect(trainX, validX)


    k = 1
    RMSEs = np.array([])
    MAPEs = np.array([])
    for i in range(len(validX)):
        sum = 0
        beta = np.array([])
        errors = []
        for j in range(len(trainX)):
            sum = abs(validX[i][0] - trainX[j][0]) + abs(validX[i][1] - trainX[j][1]) + abs(validX[i][2] - trainX[j][2])
            d = math.pow(sum, 2)/math.pow(k, 2)
            d *= -1
            beta_point = np.exp(d)
            beta = np.append(beta, beta_point)
        beta = np.diag(beta)
        w = weights.setLocalWeights(trainX, trainY, beta)

        Yhat = eval.calcYhat(validX, w)
        errors = eval.SE(validY, Yhat, errors)
        error = eval.RMSEfromSE(errors)
        MAPE = eval.MAPE(validY, Yhat)
        RMSEs = np.append(RMSEs, error)
        MAPEs = np.append(MAPEs, MAPE)

    for i in range(len(validX)):
        print(i + 1)
        print("Sample: {}".format(validX[i]))
        print("RMSE: {}".format(RMSEs[i]))
        print("MAPE: {}".format(MAPEs[i]))

        

