import pdb

def _dividePixelValue(X):
    for i in range(len(X)):
        for j in range(len(X[i])):
            X[i][j] = X[i][j]/255
    return X

def prepP2(IL):
    data = IL.getData()
    X, Y = IL.splitData(data)
    X = _dividePixelValue(X)
    IL.setMeanAndSTD(X)
    X = IL.zScore(X)
    #X = IL.reshape(X)
    return X, Y
