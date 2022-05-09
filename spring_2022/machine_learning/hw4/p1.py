import numpy as np
from data_input import *
from plot import *

if __name__ == '__main__':
    IL = InputLayer()
    plot = Plot()

    X = np.array([[-2, 1], [-5, -4], [-3, 1], [0, 3], [-8, 11], [-2, 5], [1, 0], [5, -1], [-1, -3], [6, 1]])
    Y = np.array([[1], [1], [1], [1], [1], [2], [2], [2], [2], [2]])

    IL.setMeanAndSTD(X)
    X = IL.zScore(X)

    '''
    X1 = X[:5]
    Y1 = Y[:5]
    X2 = X[5:]
    Y2 = Y[5:]

    print(X1, Y1, X2, Y2)
    '''
    X1_1 = np.array([])
    X1_2 = np.array([])
    X2_1 = np.array([])
    X2_2 = np.array([])
    Y1 = np.array([])
    Y2 = np.array([])
    for i in range(len(X)):
        if i < 5:
            X1_1 = np.append(X1_1, X[i][0])
            X1_2 = np.append(X1_2, X[i][1])
            Y1 = np.append(Y1, Y[i][0])
        else:
            X2_1 = np.append(X2_1, X[i][0])
            X2_2 = np.append(X2_2, X[i][1])
            Y2 = np.append(Y2, Y[i][0])
        print(i)
    #pdb.set_trace()
    plot.plotP1(X1_1, X1_2, Y1, X2_1, X2_2, Y2)

