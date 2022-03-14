import numpy as np
from matplotlib import pyplot as plt
from fully_connect import *
from act_func import *
from objective_func import *
from prop import *
import pdb
import random


epoch = 0



def ANN():
    X_train, X_test, Y_test, Y_train, IL = initalize()
    FC1, SIG, FC2, SM, CE = classes(X_train)
    layers = [IL, FC1, SIG, FC2, SM, CE]
    eta = .0001
    global epoch
    change = 0
    loss_v_epoch_train = []
    loss_v_epoch_test = []
    num_epoch = []
    s = 0
    r = 0


    while epoch < 10000:
        '''
        if 0 < change < .0000000001:
            break
        '''
        h_train, y_train, h_test, y_test, num_epoch = start_epoch(num_epoch, epoch, X_train, Y_train, X_test, Y_test)
        acc_train, mean_train = train(layers, h_train, y_train, eta, epoch)
        acc_test, mean_test = test(layers, h_test, y_test)
        loss_v_epoch_train.append(mean_train)
        loss_v_epoch_test.append(mean_test)
        #pdb.set_trace()
        if epoch % 100 == 0:
            print("epoch: {}, train loss: {:.4f} train acc %: {:.2f} test loss: {:.4f} test acc %: {:.2f}".format(epoch, mean_train, acc_train, mean_test, acc_test))
        try:
            change = abs(loss_v_epoch_train[-1] - loss_v_epoch_train[-2])/loss_v_epoch_train[-2]
            #pdb.set_trace()
        except Exception:
            pass
        
        epoch += 1

    plot(num_epoch, loss_v_epoch_train, loss_v_epoch_test, acc_train, acc_test)

def plot(epoch, mean_train, mean_test, train_acc, test_acc):
    plt.xlabel("Epoch")
    plt.ylabel("Mean Cross Entropy Loss")
    plt.plot(epoch, mean_train, label = 'Training', color = "black")
    plt.plot(epoch, mean_test, label = 'Testing', color = "blue")
    plt.legend()
    print("Training Accuracy: {}\nTesting Accuracy: {}".format(train_acc, test_acc))
    plt.show()

def start_epoch(num_epoch, epoch, X_train, Y_train, X_test, Y_test):
    num_epoch.append(epoch)

    train_sample = random.sample(range(len(X_train)), 10)
    test_sample = random.sample(range(len(X_test)), 10)

    h_train = np.zeros((len(train_sample), 784))
    y_train = np.zeros((len(train_sample), 10))
    h_test = np.zeros((len(test_sample), 784))
    y_test = np.zeros((len(test_sample), 10))


    for i in range(len(train_sample)):
        train_index = train_sample[i]
        h_train[i] = X_train[train_index]
        y_train[i] = Y_train[train_index]

    for i in range(len(test_sample)):
        test_index = test_sample[i]
        h_test[i] = X_test[test_index]
        y_test[i] = Y_test[test_index]

    #pdb.set_trace()
    return h_train, y_train, h_test, y_test, num_epoch



def initalize():

    print("Creating arrays, this will take a few minutes...")
    X_train = np.genfromtxt('./mnist/mnist_train_100.csv', delimiter = ',')
    print("X_train created")
    X_test = np.genfromtxt('./mnist/mnist_valid_10.csv', delimiter = ',')
    print("X_test created")

    Y_train = np.zeros((len(X_train), 10), dtype = 'float', order = 'C')
    Y_test = np.zeros((len(X_test), 10), dtype = 'float', order = 'C')
    for i in range(len(X_train)):
        if X_train[i][0] == 0:
            Y_train[i][0] = 1
        if X_train[i][0] == 1:
            Y_train[i][1] = 1
        if X_train[i][0] == 2:
            Y_train[i][2] = 1
        if X_train[i][0] == 3:
            Y_train[i][3] = 1
        if X_train[i][0] == 4:
            Y_train[i][4] = 1
        if X_train[i][0] == 5:
            Y_train[i][5] = 1
        if X_train[i][0] == 6:
            Y_train[i][6] = 1
        if X_train[i][0] == 7:
            Y_train[i][7] = 1
        if X_train[i][0] == 8:
            Y_train[i][8] = 1
        if X_train[i][0] == 9:
            Y_train[i][9] = 1
    print("Y_train created")
    for i in range(len(X_test)):
        if X_test[i][0] == 0:
            Y_test[i][0] = 1
        if X_test[i][0] == 1:
            Y_test[i][1] = 1
        if X_test[i][0] == 2:
            Y_test[i][2] = 1
        if X_test[i][0] == 3:
            Y_test[i][3] = 1
        if X_test[i][0] == 4:
            Y_test[i][4] = 1
        if X_test[i][0] == 5:
            Y_test[i][5] = 1
        if X_test[i][0] == 6:
            Y_test[i][6] = 1
        if X_test[i][0] == 7:
            Y_test[i][7] = 1
        if X_test[i][0] == 8:
            Y_test[i][8] = 1
        if X_test[i][0] == 9:
            Y_test[i][9] = 1
    print("Y_test created")

    IL = InputLayer(X_train)
    X_train = IL.forward(X_train)
    X_test = IL.forward(X_test)
    X_train = np.delete(X_train, 0, axis = 1)
    X_test = np.delete(X_test, 0, axis = 1)

    return X_train, X_test, Y_test, Y_train, IL
    


def classes(X):
    d_in = len(X[0])
    d_out1 = 784
    d_out2 = 10
    FC1 = FullyConnectedLayer(d_in, d_out1)
    SIG = SigmoidLayer()
    FC2 = FullyConnectedLayer(d_in, d_out2)
    SM = SoftmaxLayer()
    CE = CrossEntropy()
    return FC1, SIG, FC2, SM, CE