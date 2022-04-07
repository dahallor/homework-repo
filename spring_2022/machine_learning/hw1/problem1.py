from input import *
from weights import *
from eval import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    weights = Weights()
    eval = Evaluation()

    X = np.array([[-2], [-5], [-3], [0], [-8], [-2], [1], [5], [-1], [6]])
    Y = np.array([[1], [-4], [1], [3], [11], [5], [0], [-1], [-3], [1]])

    X = inputLayer.addDummyValueCrossValidation(X)
    w = weights.setWeights(X, Y)
    print(w)

    Yhat = eval.calcYhat(X, w)
    print(Yhat)

    RMSE = eval.RSME(Y, Yhat)
    SMAPE = eval.SMAPE(Y, Yhat)
    print(RMSE)
    print(float(SMAPE))