import numpy as np
import pdb
    
    
def train(layers, h, y, eta, epoch):
        #forward
        for i in range(len(layers)-1):
            h = layers[i].forward(h)
            #pdb.set_trace()

        #pdb.set_trace()
        mean_loss = layers[-1].eval(y, h)

        train_accuracy_rate = accuracy(y, h)
        #backward
        grad = layers[-1].gradient(y,h)
        for i in range(len(layers)-2,0,-1):
            newgrad = layers[i].backward(grad, eta, epoch)
            #pdb.set_trace()
            grad = newgrad

        return train_accuracy_rate, mean_loss
        

    

def test(layers, h, y):
    #Testing
    #forward
    for i in range(len(layers)-1):
        #pdb.set_trace()
        h = layers[i].forward(h)

    mean_loss = layers[-1].eval(y, h)
    test_accuracy_rate = accuracy(y, h)

    return test_accuracy_rate, mean_loss


def accuracy(y, yhat):
    '''
    num_correct = 0
    n = len(yhat)

    for i in range(len(y)):

        y_max = np.max(y[i])
        y_index = np.where(y[i] == y_max)
        yhat_max = np.max(yhat[i])
        yhat_index = np.where(yhat[i] == yhat_max)
        if y_index == yhat_index:
            num_correct += 1
        #pdb.set_trace()


    pdb.set_trace()
    accuracy_rate = (num_correct/n)*100
    #pdb.set_trace()
    return accuracy_rate
    '''
    return (np.sum(np.argmax(yhat, axis=1) == np.argmax(y, axis=1)) / len(y) * 100)