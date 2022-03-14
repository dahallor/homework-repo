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


if __name__ == '__main__':
    numpy.set_printoptions(threshold=sys.maxsize)

    #Section 2 - Visualizing Gradient
    '''
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
    inputL = InputLayer(X)
    X = inputL.forward(X)
    np.random.shuffle(X)
    train_size = round(len(X) * .67)
    valid_size = len(X) - train_size
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
        print("train " + str(epoch))
        num_epochs_train.append(epoch)

        H = FC.forward(X_train)
        Yhat, mean = square.eval(Y_train, H)
        delta = square.gradient(Y_train, mean)
        FC.backward(delta, eta)

        MAPE_train.append(square.MAPE(Y_train, Yhat))

        rsme = np.sqrt(Yhat[0])    
        RMSE_train.append(rsme)
        pdb.set_trace()
        epoch += 1
        try:
            change = MAPE_train[-2] - MAPE_train[-1]
        except Exception:
            pass    

    
    epoch = 0
    change = 0
    input()
    #Validation Loop Loop
    while epoch < 10000:
        if 0 < abs(change) < math.pow(10, -10):
            break
        print("valid " + str(epoch))
        num_epochs_valid.append(epoch)

        H = FC.forward(X_valid)
        Yhat, mean = square.eval(Y_valid, H)
        delta = square.gradient(Y_valid, mean)
        FC.backward(delta, eta)

        MAPE_valid.append(square.MAPE(Y_valid, Yhat))

        rsme = np.sqrt(Yhat[0])    
        RMSE_valid.append(rsme)
        pdb.set_trace()  
        epoch += 1
        try:
            change = MAPE_valid[-2] - MAPE_valid[-1]
        except Exception:
            pass  
        
    pdb.set_trace()
    


    '''
    #Section 5
    X = numpy.genfromtxt('./data/KidCreative.csv', delimiter = ',')
    X = np.delete(X, 0, axis = 0)
    X = np.delete(X, 0, axis = 1)
    inputL = InputLayer(X)
    X = inputL.forward(X)
    np.random.shuffle(X)
    train_size = round(len(X) * .67)
    valid_size = len(X) - train_size
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
    d_in = len(X_train[0])
    d_out = 1
    FC = FullyConnectedLayer(d_in, d_out)
    sig = SigmoidLayer()
    log = LogLoss()
    
    log_arr = []
    num_epoch_train = []
    num_epoch_valid = []

    epoch = 0
    eta = .0001

    #Training
    while epoch < 10000 or change > math.pow(10, -10):
        print(epoch)
        num_epoch_train.append(epoch)

        H = FC.forward(X_train)
        sigmoid = sig.forward(H)
        pdb.set_trace()
        Yhat = log.eval(Y_train, sigmoid)
        delta = log.gradient(Y_train, Yhat)
        delta2 = sig.gradient()
        FC.backward(delta2, eta)

        epoch += 1

        pass
    '''

        
        










    







