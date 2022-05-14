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
    knn = KNN()
    
    prepP3(IL)
    max_values = pca.getPCP3_All(IL.trainX)
    knn.plottingPoints(pca, max_values, IL.trainX)

    max_values_valid = pca.getPC_P3_Valid_All(IL.validX)
    knn.plottingPoints(pca, max_values_valid, IL.validX)
    