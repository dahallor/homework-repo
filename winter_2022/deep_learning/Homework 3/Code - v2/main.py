from itertools import accumulate
import numpy
from act_func import *
from objective_func import *
from fully_connect import FullyConnectedLayer
from input import *
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import sys
import pdb

def visualize_eval(X, W):
    x1 = X[0][0]
    x2 = X[1][0]
    w1 = W[0][0]
    w2 = W[1][0]
    J = math.pow((x1 * w1 - 5 * x2 *w2 -2), 2)
    return J

def visualize_gradient(X, W):
    x1 = X[0][0]
    x2 = X[1][0]
    w1 = W[0][0]
    w2 = W[1][0]
    delta_w1 = 2 * (x1 * w1 - 5 * x2 * w2 - 2) * x1
    delta_w2 = -10 * x2 * (x1 * w1 - 5 * x2 * w2 -2)
    return delta_w1, delta_w2

def initalize_kid(X):
    X = np.delete(X, 0, axis = 0)
    X = np.delete(X, 0, axis = 1)
    inputL = InputLayer(X)
    X = inputL.forward(X)
    np.random.shuffle(X)
    train_size = round(len(X) * .67)

    X_train = X[0:train_size]
    X_valid = X[train_size:]


    Y_train = np.zeros((len(X_train), 1), dtype = 'float', order = 'C')
    Y_valid = np.zeros((len(X_valid), 1), dtype = 'float', order = 'C')
    for i in range(len(Y_train)):
        Y_train[i] = X_train[i][0]
    for i in range(len(Y_valid)):
        Y_valid[i] = X_valid[i][0]

    X_train = np.delete(X_train, 0, axis = 1)
    X_valid = np.delete(X_valid, 0, axis = 1)

    return X_train, X_valid, Y_train, Y_valid


def initalize_med(X):
    inputL = InputLayer(X)
    X = inputL.forward(X)
    np.random.shuffle(X)
    train_size = round(len(X) * .67)
    X_train = X[0:train_size]
    X_valid = X[train_size:]


    Y_train = np.zeros((len(X_train), 1), dtype = 'float', order = 'C')
    Y_valid = np.zeros((len(X_valid), 1), dtype = 'float', order = 'C')
    for i in range(len(Y_train)):
        Y_train[i] = X_train[i][-1]
    for i in range(len(Y_valid)):
        Y_valid[i] = X_valid[i][-1]

    X_train = np.delete(X_train, -1, axis = 1)
    X_valid = np.delete(X_valid, -1, axis = 1)

    return X_train, X_valid, Y_train, Y_valid

def RMSE(Y, YHAT, n):
    DIF = Y - YHAT
    sq = np.zeros((len(Y), 1), dtype = 'float', order = 'C')
    for i in range(len(DIF)):
        sq[i] = math.pow(DIF[i][0], 2)
    sum = np.sum(sq)
    mse = sum/n
    rmse = np.sqrt(mse)

    return rmse

def MAPE(Y, YHAT, n):
    APE = abs((Y - YHAT)/Y)
    sum = np.sum(APE)
    MAPE = sum/n
    return MAPE

if __name__ == '__main__':
    numpy.set_printoptions(threshold=sys.maxsize)

    #Section 2 - Visualizing Gradient

    X = np.zeros((2, 1), dtype = float, order = 'C')
    W = np.zeros((2, 1), dtype = float, order = 'C')
    X[0][0] = 1
    X[1][0] = 1
    W[0][0] = 0
    W[1][0] = 0
    J = np.zeros(100, dtype = float, order = 'C')
    w1 = np.zeros(100, dtype = float, order = 'C')
    w2 = np.zeros(100, dtype = float, order = 'C')
    eta = .01

    for i in range(100):

        temp = visualize_eval(X, W)
        d1, d2 = visualize_gradient(X, W)
        print(d1, d2)
        J[i] = temp

        W[0][0] = W[0][0] + eta * (-1 * d1)
        W[1][0] = W[1][0] + eta * (-1 * d2)
        w1[i] = W[0][0]
        w2[i] = W[1][0]


    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.plot(w1, w2, J, 'red')

    plt.show()
    
    '''
    #Section 4 - Linear Regression
    X = numpy.genfromtxt('./data/mcpd_augmented.csv', delimiter = ',')
    
    d_in = len(X[0])-1
    d_out = 1
    FC = FullyConnectedLayer(d_in, d_out)
    square = LeastSquares()

    RMSE_train = []
    RMSE_valid = []
    MAPE_train = []
    MAPE_valid = []
    num_epochs_train = []
    num_epochs_valid = []

    epoch = 0
    eta = .0001
    change = 0

    #Training Loop
    while epoch < 10000:
        if 0 < abs(change) < math.pow(10, -10):
            break
        X_train, X_valid, Y_train, Y_valid = initalize_med(X)
        print("train " + str(epoch))
        accumulator = np.zeros(((len(X_train)), len(X_train[0]), len(Y_train[0])), dtype = "float", order = 'C')
        YHAT = np.zeros((len(Y_train), len(Y_train[0])), dtype = "float", order = 'C')
        for i in range(len(Y_train)):
            y = Y_train[i]
            x = X_train[i]
            h = FC.forward(x)
            yhat = square.eval(y, h)
            YHAT[i][0] = yhat
            delta = square.gradient(y, h)
            for j in range(len(X_train[i])):
                accumulator[i][j][0] = delta
            mean = np.mean(accumulator, axis = 0)
            FC.updateWeights(mean, eta)

        n = len(Y_train)

        rmse = RMSE(Y_train, YHAT, n)
        mape = MAPE(Y_train, YHAT, n)
        RMSE_train.append(rmse)
        MAPE_train.append(mape)
        num_epochs_train.append(epoch)
            
        epoch += 1
        try:
            change = abs(MAPE_train[-2] - MAPE_train[-1])
        except Exception:
            pass    

    fig = plt.figure()
    plt.xlabel("Epoch")
    plt.ylabel("Error")
    plt.plot(num_epochs_train, MAPE_train, c='blue', label = "MAPE")
    plt.plot(num_epochs_train, RMSE_train, c='orange', label = "RMSE")
    plt.legend()
    plt.show()

    epoch = 0
    change = 0
    input()
    
    #Validation Loop Loop
    while epoch < 10000:
        if 0 < abs(change) < math.pow(10, -10):
            break
        X_train, X_valid, Y_train, Y_valid = initalize_med(X)
        print("valid " + str(epoch))
        accumulator = np.zeros(((len(X_valid)), len(X_valid[0]), len(Y_valid[0])), dtype = "float", order = 'C')
        YHAT = np.zeros((len(Y_valid), len(Y_valid[0])), dtype = "float", order = 'C')
        for i in range(len(Y_valid)):
            y = Y_valid[i]
            x = X_valid[i]
            h = FC.forward(x)
            yhat = square.eval(y, h)
            YHAT[i][0] = yhat
            delta = square.gradient(y, h)
            for j in range(len(X_valid[i])):
                accumulator[i][j][0] = delta
            mean = np.mean(accumulator, axis = 0)
            FC.updateWeights(mean, eta)

        n = len(Y_valid)

        rmse = RMSE(Y_valid, YHAT, n)
        mape = MAPE(Y_valid, YHAT, n)
        RMSE_valid.append(rmse)
        MAPE_valid.append(mape)
        num_epochs_valid.append(epoch)
            
        epoch += 1
        try:
            change = abs(MAPE_valid[-2] - MAPE_valid[-1])
        except Exception:
            pass    

    fig = plt.figure()
    plt.xlabel("Epoch")
    plt.ylabel("Error")
    plt.plot(num_epochs_valid, MAPE_valid, c='blue', label = "MAPE")
    plt.plot(num_epochs_valid, RMSE_valid, c='orange', label = "RMSE")
    plt.legend()
    plt.show()

    


    
    #Section 5
    X = numpy.genfromtxt('./data/KidCreative.csv', delimiter = ',')
    X_train, X_valid, Y_train, Y_valid = initalize_kid(X)
    d_in = len(X[0])-2
    d_out = 1
    FC = FullyConnectedLayer(d_in, d_out)
    sig = SigmoidLayer()
    log = LogLoss()
    
    log_arr = []
    accuracy = []
    num_epoch_train = []
    num_epoch_valid = []
    real_y = Y_train
    for i in range(len(real_y)):
        if abs(real_y[i][0]) < .5:
            real_y[i][0] = 0
        else:
            real_y[i][0] = 1


    epoch = 0
    eta = .0001
    change = 0

    #Training
    while epoch < 50:
        if 0 < abs(change) < math.pow(10, -10):
            break
        print("train " + str(epoch))
        accumulator = np.zeros(((len(X_train)), len(X_train[0]), len(Y_train[0])), dtype = "float", order = 'C')
        #YHAT = np.zeros((len(Y_train), len(Y_train[0])), dtype = "float", order = 'C')

        H = FC.forward(X_train)
        sigmoid = sig.forward(H)
        YHAT = log.eval(Y_train, sigmoid)
        delta = log.gradient(Y_train, YHAT)
        delta2 = sig.backward(delta, eta)
        mean = np.mean(accumulator, axis = 0)
        FC.updateWeights(mean, eta)


        real_yhat = YHAT
        for i in range(len(real_y)):
            if abs(real_yhat[i][0]) < .5:
                real_yhat[i][0] = 0
            else:
                real_yhat[i][0] = 1
        epoch += 1
        try:
            change = abs(log_arr[-2] - log_arr[-1])
        except Exception:
            pass  

    real_y = Y_valid
    for i in range(len(real_y)):
        if abs(real_y[i][0]) < .5:
            real_y[i][0] = 0
        else:
            real_y[i][0] = 1
    #Validating
    while epoch < 50:
        if 0 < abs(change) < math.pow(10, -10):
            break
        print("valid " + str(epoch))
        accumulator = np.zeros(((len(X_valid)), len(X_valid[0]), len(Y_valid[0])), dtype = "float", order = 'C')
        #YHAT = np.zeros((len(Y_train), len(Y_train[0])), dtype = "float", order = 'C')

        H = FC.forward(X_valid)
        sigmoid = sig.forward(H)
        YHAT = log.eval(Y_valid, sigmoid)
        delta = log.gradient(Y_valid, YHAT)
        delta2 = sig.backward(delta, eta)
        mean = np.mean(accumulator, axis = 0)
        FC.updateWeights(mean, eta)


        real_yhat = YHAT
        for i in range(len(real_y)):
            if abs(real_yhat[i][0]) < .5:
                real_yhat[i][0] = 0
            else:
                real_yhat[i][0] = 1
        epoch += 1
        try:
            change = abs(log_arr[-2] - log_arr[-1])
        except Exception:
            pass 
        '''




        
        










    







