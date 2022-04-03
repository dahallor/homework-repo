from input import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    data = inputLayer.getCSVItems()
    shuffled_data = inputLayer.shuffleData(data)
    print(shuffled_data)
    trainingX, validX = inputLayer.splitData(shuffled_data)
    print(trainingX, validX)