import math
from base_class import *
import numpy as np

class LeastSquares(Objective):
    def __init__(self):
        super().__init__()

    def eval(self, y, yhat):
        J = math.pow((y-yhat),2)
        return J

    def gradient(self, y, yhat):
        delta = -2 * (y - yhat)
        return delta

class LogLoss(Objective):
    def __init__(self):
        super().__init__()

    def eval(self, y, yhat):
        epsilon = .0000001
        J = -1 * ((y * np.log(yhat + epsilon)) + (1 - y) * np.log(1 - yhat + epsilon))
        return J

    def gradient(self, y, yhat):
        epsilon = .0000001
        delta = -1 * ((y - yhat) / (yhat * (1 - yhat) + epsilon))
        return delta

class CrossEntropy(Objective):
    def __init__(self):
        super().__init__()

    def eval(self, y, yhat):
        e = .0000001
        yt = np.transpose(yhat)
        log = np.log(yt + e)

        J = y.dot(log)
        J *= -1
    
        return J

    def gradient(self, y, yhat):
        epsilon = .0000001
        delta = y/(yhat + epsilon)
        delta *= -1
        return delta