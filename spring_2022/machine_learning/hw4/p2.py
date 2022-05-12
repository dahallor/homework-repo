import sys
import numpy as np
from prep import *
from data_input import *
from PCA import *

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()
    pca = PCA()

    X, Y = prepP2(IL) 
    pca.getPC(X)