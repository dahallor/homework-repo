import numpy as np
from input import *
from weights import *
from obj import *
from eval import *
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
    evaluation = Eval()
    inputLayer.setMeanAndSTD(trainX)
    trainX = inputLayer.zScore(trainX)
    validX = inputLayer.zScore(validX)


    epoch = 0
    epoch_list = []
    eta = .0001
    while epoch <= 1000000:
        if epoch % 100 == 0:
            print("Epoch: {}".format(epoch))
            #pdb.set_trace()
        if epoch > 3:
            change = abs(logLoss.meanTrain[epoch-1] - logLoss.meanTrain[epoch-2])
            if change < math.pow(2, -32):
                break

        trainYhat = evaluation.calcYhat(trainX, weights)
        validYhat = evaluation.calcYhat(validX, weights)

        logLoss.eval(trainY, trainYhat, "train")
        logLoss.eval(validY, validYhat, "valid")

        weights.set_dJdW(trainX, trainY, trainYhat)
        weights.set_dJdb(trainY, trainYhat)

        weights.updateWeightsAndBias(eta)

        epoch_list.append(epoch)
        epoch += 1






    
