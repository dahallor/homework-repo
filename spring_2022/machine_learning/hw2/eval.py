import numpy as np

class Eval():
    def __init__(self):
        pass

    def calcYhat(self, X, weights):
        Yhat = np.zeros((len(X), 1), dtype = 'float')
        for i in range(len(X)):
            exponent = -1 * (np.matmul(X[i], weights.W) + weights.b)
            Yhat[i] = 1/(1 + np.exp(exponent))

        return Yhat

