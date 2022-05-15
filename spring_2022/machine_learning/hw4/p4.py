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

    #Target Image
    image = np.array([X[-1]])
    image = image.reshape(87, 65)
    plot.displayImage(image, "Target Image")

    #Top PC Value as Image
    pca.getPCTopValue(X)
    pca.calcPC_TopValue(X)
    image = pca.eigvector1.reshape(87, 65)
    plot.displayImage(image, "Largest Eigenvector")

    #Reconstructed Image w/ 1 PC
    X_hat = pca.uncompressTopValue()
    image = np.array([X_hat[-1]])
    image = image.reshape(87, 65)
    plot.displayImage(image, "Single PC Reconstruction")

    #Reconstructed Image w/ 95% alpha
    max_values = pca.getPCP3_All(X)
    count = pca.selectTopEigValues()
    max_values = max_values[:count+1]
    pca.calcPC_Threshold(X, max_values)
    X_hat = pca.uncompressThreshold(X, max_values)
    image = np.array([X_hat[-1]])
    image = image.reshape(87, 65)
    plot.displayImage(image, ".95 Alpha Reconstruction")