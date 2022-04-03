from input import *
from weights import *
from eval import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    weights = Weights()
    eval = Evaluation()


    data = inputLayer.getCSVItems()
    shuffled_data = inputLayer.shuffleData(data)
    trainX, trainY, validX, validY = inputLayer.splitData(shuffled_data)
    trainX, validX = inputLayer.addDummyValue(trainX, validX)
    # trainX, trainY, validX, validY = inputLayer.addDummyValue(trainX, trainY, validX, validY)

    w = weights.setWeights(trainX, trainY)

    validYhat = eval.calcYhat(validX, w)
    RMSE = eval.RSME(validY, validYhat)
    #print(RMSE)




    
