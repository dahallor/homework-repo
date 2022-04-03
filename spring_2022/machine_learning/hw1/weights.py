import numpy as np
import math

class Weights:
    def __init__(self):
        pass

    def setWeights(self, X, Y):
        Xt = X.transpose()
        product = Xt.dot(X)
        product = product.astype(float)
        product2 = product ** -1
        product3 = product2.dot(Xt) 
        w = product3.dot(Y)
        return w