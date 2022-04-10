from input import *
from weights import *
from eval import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    weights = Weights()
    eval = Evaluation()

    #Problem 2
    data = inputLayer.getCSVItems()
    shuffled_data = inputLayer.shuffleData(data, 0)
    trainX, trainY, validX, validY = inputLayer.splitDataDirect(shuffled_data)
    trainX, validX = inputLayer.addDummyValueDirect(trainX, validX)

    w = weights.setWeights(trainX, trainY)

    trainYhat = eval.calcYhat(trainX, w)
    validYhat = eval.calcYhat(validX, w)

    RMSEtrain = eval.RSME(trainY, trainYhat)
    MAPEtrain = eval.MAPE(trainY, trainYhat)
    RMSEvalid = eval.RSME(validY, validYhat)
    MAPEvalid = eval.MAPE(validY, validYhat)

    print("Training Set:")
    print("RMSE: {}".format(RMSEtrain))
    print("MAPE: {}".format(MAPEtrain))
    print()
    print("Validation Set:")
    print("RMSE: {}".format(RMSEvalid))
    print("MAPE: {}".format(MAPEvalid))







    
