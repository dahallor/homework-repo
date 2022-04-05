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
    print(w)

    validYhat = eval.calcYhat(validX, w)
    RMSE = eval.RSME(validY, validYhat)
    MAPE = eval.MAPE(validY, validYhat)
    print(RMSE)
    print(MAPE)





    
