from input import *
from weights import *
from eval import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    weights = Weights()
    eval = Evaluation()

    S = 20

    for i in range(1, S+3, 1):
        data = inputLayer.getCSVItems()
        data = inputLayer.shuffleData(data, i)
        X, Y = inputLayer.splitDataCrossValidation(data)
        X = inputLayer.addDummyValueCrossValidation(X)
        trainX, trainY, validX, validY = inputLayer.S_folds(i, S, X, Y)

        
