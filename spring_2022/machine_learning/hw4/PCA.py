import numpy as np
import pdb

def _getCov(X):
    cov = np.cov(X)
    return cov

def _getEig(cov):
    eigvalues, eigvectors = np.linalg.eig(cov)
    return eigvalues, eigvectors

def _getTopTwoEigs(eigvalues):
    vectors = np.argsort(eigvalues)
    max_vectors = vectors[:2]
    return max_vectors
    


class PCA:
    def __init__(self):
        pass

    def getPC(self, X):
        cov = _getCov(X)
        eigvalues, eigvectors = _getEig(cov)
        max_vectors = _getTopTwoEigs(eigvalues)
        pdb.set_trace()