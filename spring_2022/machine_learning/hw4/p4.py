import sys
import numpy as np
from prep import *
from data_input import *
from PCA import *
from plot import *

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()
    plot = Plot()
    pca = PCA()

    X, Y = prepP2(IL) 

    pca.getPCTopValue(X)
    pca.calcPC_TopValue(plot, X)



    image = np.array([X[-1]])
    image = image.reshape(87, 65)