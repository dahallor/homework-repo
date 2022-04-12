import numpy as np
from input import *
from weights import *
from obj import *
import sys
import pdb
import math

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    inputLayer = InputLayer()
    logLoss = LogLoss()

    data = inputLayer.getSpamItems()
    data = inputLayer.shuffleData(data, 0)

    trainX, trainY, validX, validY = inputLayer.splitDataSpam(data)
    weights = Weights(trainX)
    inputLayer.setMeanAndSTD(trainX)
    trainX = inputLayer.zScore(trainX)
    validX = inputLayer.zScore(validX)


    epoch = 0
    epoch_list = []
    eta = .0001
    while epoch <= 1000000:
        pdb.set_trace()
        try:
            change = abs(logLoss.meanTrain[epoch-1] - logLoss.meanTrain[epoch-2])
            if change < math.pow(2, -32):
                break
        except Exception:
            pass

        trainYhat = weights.calcYhat(trainX)
        validYhat = weights.calcYhat(validX)

        J1 = logLoss.eval(trainY, trainYhat, "train")
        J2 = logLoss.eval(validY, validYhat, "valid")

        epoch_list.append(epoch)
        epoch += 1





    
