import numpy as np
import math

class InputLayer:
    def __init__(self):
        pass

    def getCSVItems(self):
        data = np.genfromtxt('x06Simple.csv', dtype = int, delimiter = ",", skip_header = 1, )
        return data

    def shuffleData(self, data):
        np.random.shuffle(data)
        return data

    def splitData(self, data):
        training_size = int(np.ceil(len(data) * (2/3)))
        print(training_size)
        training_data = data[:training_size]
        validation_data = data[training_size:]
        return training_data, validation_data