from input import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    data = inputLayer.getCSVItems()
    shuffled_data = inputLayer.shuffleData(data)
    trainX, trainY, validX, validY = inputLayer.splitData(shuffled_data)

