import numpy as np
import math

class Weights:
    def __init__(self):
        pass

    def setWeights(self, X, Y):
        Xt = X.transpose()
        product = np.matmul(Xt, X)
        product2 = np.linalg.inv(product)
        problem3 = np.matmul(product2, Xt)
        w = np.matmul(problem3, Y)
        return w
        '''
        Xt = X.transpose()
        product = Xt@X
        product = product.astype(float)
        product2 = product ** -1
        product3 = product2@Xt 
        w = product3@Y
        return w
        '''