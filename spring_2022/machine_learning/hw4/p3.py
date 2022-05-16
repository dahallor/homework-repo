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
    knn_no_pca = KNN()
    knn_pca = KNN()
    knn_whiten = KNN()
    
    prepP3(IL)
    total = len(IL.validX)

    #No PCA
    knn_no_pca.findNearestNeighbors(IL, IL.validX, IL.trainX)
    knn_no_pca.getAccuracy(total)
    
    #PCA
    max_values = pca.getPCP3_100(IL.trainX)
    trainPC = pca.calcPC_Threshold(IL.trainX, max_values)
    validPC = pca.calcPC_Threshold(IL.validX, max_values)
    knn_pca.findNearestNeighbors(IL, validPC, trainPC)
    knn_pca.getAccuracy(total)

    #PCA Whitened
    max_values = pca.getPCP3_100(IL.trainX)
    trainPC = pca.calcPC_Whitened(IL.trainX, max_values)
    validPC = pca.calcPC_Whitened(IL.validX, max_values)
    knn_whiten.findNearestNeighbors(IL, validPC, trainPC)
    knn_whiten.getAccuracy(total)
    

    