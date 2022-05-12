import numpy as np
from data_input import *
from plot import *


def _PCA(IL, plot, X, Y):
    X_class1 = X[:5]
    X_class2 = X[5:]
    c1_X = np.array([])
    c1_Y = np.array([])
    c2_X = np.array([])
    c2_Y = np.array([])
    for i in range(len(X_class1)):
        c1_X = np.append(c1_X, X_class1[i][0])
        c1_Y = np.append(c1_Y, X_class1[i][1])
    for i in range(len(X_class2)):
        c2_X = np.append(c2_X, X_class2[i][0])
        c2_Y = np.append(c2_Y, X_class2[i][1])
    
    #Uncomment to reveal plot for part 1.a
    #plot.plotP1(c1_X, c1_Y, c2_X, c2_Y)

    #Covraince
    Xt = X.transpose()
    N = len(X)
    ddof_size = N-1
    #cov = (np.matmul(Xt, X))/(N-1)
    cov = np.cov(Xt)
    print()
    print(cov)
    print()


    #eigenvalues
    eigvalues, eigvectors = np.linalg.eig(cov)
    eigvector1 = eigvectors[:, :1]
    eigvector2 = eigvectors[:, 1:]

    #PCA
    PC1 = np.zeros((len(X), 1))
    PC2 = np.zeros((len(X), 1))
    for i in range(len(X)):
        obs = X[i]
        PC1[i] = np.matmul(obs, eigvector1)
        PC2[i] = np.matmul(obs, eigvector2)
    plot.plotP1_1D(PC1, PC2)

def _LDA(IL, plot, X, Y):
    IL.setMeanByClass(X)
    Sw = IL.std_c1 + IL.std_c2
    inv = np.linalg.inv(Sw)
    x = np.array([[0.000, 0.000]])
    for i in range(len(IL.mean_c1)):
        x[0][i] = IL.mean_c1[i] - IL.mean_c2[i]
    xt = np.array([[0.00000], [0.00000]])
    for i in range(len(x[0])):
        xt[i][0] = x[0][i]
    Sb = np.matmul(xt, x)
    '''
    pdb.set_trace()

    print()
    print(Sw)
    print()
    print(inv)
    print()
    print(Sb)
    '''
    matrix = np.matmul(inv, Sb)
    eigvalues, eigvectors = np.linalg.eig(matrix)
    eigvector1 = eigvectors[:, :1]
    eigvector2 = eigvectors[:, 1:]
    '''
    print(matrix)
    print()
    print(eigvalues)
    print()
    print(eigvector1)
    print()
    print(eigvector2)
    '''
    
    LDA = np.zeros((len(X), 1))
    for i in range(len(X)):
        obs = X[i]
        LDA[i] = np.matmul(obs, eigvector1)
    print(LDA)
    plot.plotP1_LDA(LDA)


if __name__ == '__main__':
    IL = InputLayer()
    plot = Plot()

    X = np.array([[-2, 1], [-5, -4], [-3, 1], [0, 3], [-8, 11], [-2, 5], [1, 0], [5, -1], [-1, -3], [6, 1]])
    Y = np.array([[1], [1], [1], [1], [1], [2], [2], [2], [2], [2]])

    IL.setMeanAndSTD(X)
    X = IL.zScore(X)

    #_PCA(IL, plot, X, Y)
    _LDA(IL, plot, X, Y)





