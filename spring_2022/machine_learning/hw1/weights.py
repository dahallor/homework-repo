import numpy as np
import math

class Weights:
    def __init__(self):
        pass


    def setWeights(self, X, Y):

        Xt = X.transpose()
        product = np.matmul(Xt, X)
        product2 = np.linalg.inv(product)
        product3 = np.matmul(product2, Xt)
        w = np.matmul(product3, Y)

        return w

