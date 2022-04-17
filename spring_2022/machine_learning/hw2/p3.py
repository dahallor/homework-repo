import numpy as np
from run_regression import *
from plot import *
from input import *
from weights import *
from obj import *
from eval import *
import sys
import pdb
import math

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)

    IL = InputLayer()
    logLoss = LogLoss()
    plot = Plot()
    run = Run(0, [], .0001)
    evaluation = Eval()

    IL.alterIrisData()
    data = IL.getIrisItems()
    data = IL.shuffleData(data, 0)
    IL.splitDataSpam(data)
    weights = Weights(IL.trainX)
    #pdb.set_trace()


    IL.setMeanAndSTD(IL.trainX)
    IL.zScore("train")
    IL.zScore("valid")
    #pdb.set_trace()

    run.binaryLogisticalRegression(logLoss, evaluation, weights, IL)
    plot.plotMean(logLoss, run.epoch_list)