import sys
import numpy as np
from prep import *
from data_input import *
from PCA import *
from plot import *
from KNN import *

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()
    plot = Plot()
    pca = PCA()
    
    prepP3(IL)
    knn_no_pca = KNN()
    knn_no_pca.findNearestNeighbors(IL)
    total = len(IL.validX)
    knn_no_pca.getAccuracy(total)

    