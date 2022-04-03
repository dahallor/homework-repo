from input import *
from weights import *
from obj import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    weights = Weights()

    data = inputLayer.getCSVItems()
    shuffled_data = inputLayer.shuffleData(data)
    trainX, trainY, validX, validY = inputLayer.splitData(shuffled_data)
    trainX = inputLayer.addDummyValue(trainX)
    # trainX, trainY, validX, validY = inputLayer.addDummyValue(trainX, trainY, validX, validY)

    w = weights.setWeights(trainX, trainY)
    print(w)

    
