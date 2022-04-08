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

    def setLocalWeights(self, X, Y, D):
        #FIXME: revert inverted matrix when diagnal matrix stops sucking
        Xt = X.transpose()
        product1 = np.matmul(Xt, D)
        product2 = np.matmul(product1, X)
        #product3 = np.linalg.inv(product2)
        product3 = product2
        product4 = np.matmul(product3, Xt)
        product5 = np.matmul(product4, D)
        w = np.matmul(product5, Y)
        return w
