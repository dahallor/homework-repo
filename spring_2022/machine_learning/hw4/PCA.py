import numpy as np
import math
import pdb

def _getCov(X):
    print("Calculating Covariance...")
    Xt = X.transpose()
    N = len(X)
    cov = (np.matmul(Xt, X))/(N-1)
    return cov

def _getEig(cov):
    eigvalues, eigvectors = np.linalg.eig(cov)
    eigvalues = np.real(eigvalues)
    eigvectors = np.real(eigvectors)
    return eigvalues, eigvectors

def _getTopEig(eigvalues):
    vectors = np.argsort(eigvalues)
    max_vector = vectors[-1]
    return max_vector

def _getTopTwoEigs(eigvalues):
    vectors = np.argsort(eigvalues)
    max_vectors = []
    max_vectors.append(vectors[-1])
    max_vectors.append(vectors[-2])
    return max_vectors

def _getTop100Eigs(eigvalues):
    vectors = np.argsort(eigvalues)
    indecies = len(vectors)-100
    max_vectors = vectors[indecies:]
    max_vectors = np.flip(max_vectors)
    return max_vectors

def _getAllEigs(eigvalues):
    vectors = np.argsort(eigvalues)
    max_vectors = np.flip(vectors)
    return max_vectors


class PCA:
    def getPC(self, X):
        cov = _getCov(X)
        self.eigvalues, eigvectors = _getEig(cov)
        max_values = _getTopTwoEigs(self.eigvalues)
        self.vec1 = max_values[0]
        self.vec2 = max_values[1]
        self.eigvector1 = eigvectors[:, self.vec1:self.vec1+1]
        self.eigvector2 = eigvectors[:, self.vec2:self.vec2+1]

    def getPCTopValue(self, X):
        cov = _getCov(X)
        self.eigvalues, eigvectors = _getEig(cov)
        max_value = _getTopEig(self.eigvalues)
        self.eigvector1 = eigvectors[:, max_value:max_value+1]

    def getPCP3_100(self, X):
        cov = _getCov(X)
        self.eigvalues, self.eigvectors = _getEig(cov)
        max_values = _getTop100Eigs(self.eigvalues)
        return max_values

    def getPCP3_All(self, X):
        cov = _getCov(X)
        self.eigvalues, self.eigvectors = _getEig(cov)
        max_values = _getAllEigs(self.eigvalues)
        return max_values

    def getPC_P3_Valid_All(self, X):
        cov = _getCov(X)
        self.eigvaluesValid, self.eigvectorsValid = _getEig(cov)
        max_values = _getAllEigs(self.eigvaluesValid)
        return max_values
    
    def calcPC(self, plot, X):
        self.PC1 = np.zeros((len(X), 1))
        self.PC2 = np.zeros((len(X), 1))
        print("Calculating Principle Components...")
        for i in range(len(X)):
            obs = X[i]
            self.PC1[i] = np.matmul(obs, self.eigvector1)
            self.PC2[i] = np.matmul(obs, self.eigvector2)
        plot.plotPCA(self.PC1, self.PC2)

    def calcPC_TopValue(self, X):
        self.PC = np.zeros((len(X), 1))
        print("Calculating Principle Components...")
        for i in range(len(X)):
            obs = X[i]
            self.PC[i] = np.matmul(obs, self.eigvector1)
        pdb.set_trace()


    def whiten(self, plot):
        values = np.real(self.eigvalues)
        eig1 = values[self.vec1]
        eig2 = values[self.vec2]

        self.eigvector1 = self.eigvector1/(np.sqrt(eig1))
        self.eigvector2 = self.eigvector2/(np.sqrt(eig2))

        plot.plotPCA_Whiten(self.eigvector1, self.eigvector2)



