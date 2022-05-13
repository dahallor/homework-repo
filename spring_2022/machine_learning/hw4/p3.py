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
    
    prepP3(IL)
    pca.getPCP3(IL.trainX)
    