import math
from base_class import *
import numpy as np

class LeastSquares(Objective):
    def __init__(self):
        super().__init__()

    def eval(self, y, yhat):

        temp1 = (y - yhat).T @ (y - yhat)/y.shape[0] 
        temp2 = np.sum(temp1, axis=1)
        loss = np.mean(temp2)

        return loss

    def gradient(self, Y, Yhat):
        delta = -2 * (Y - Yhat)
        return delta



class LogLoss(Objective):
    def __init__(self):
        super().__init__()

    def eval(self, y, yhat):
        epsilon = .0000001
        temp = -1 * ((y * np.log(yhat + epsilon)) + (1 - y) * np.log(1 - yhat + epsilon))
        temp2 = np.sum(temp, axis=1)
        loss = np.mean(temp2)
        return loss

    def gradient(self, y, yhat):
        epsilon = .0000001
        delta = -1 * ((y - yhat) / (yhat * (1 - yhat) + epsilon))
        return delta

class CrossEntropy(Objective):
    def __init__(self):
        super().__init__()

    def eval(self, y, yhat):
        
        temp = -1 * y * np.log(yhat)
        temp2 = np.sum(temp, axis = 1)
        loss = np.mean(temp2)
    
        return loss

    def gradient(self, y, yhat):
        epsilon = .0000001
        delta = y/(yhat + epsilon)
        delta *= -1

        return delta



   