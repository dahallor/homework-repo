import pdb

def _dividePixelValue(X):
    for i in range(len(X)):
        for j in range(len(X[i])):
            X[i][j] = X[i][j]/255
    return X

def prepP2(IL):
    print("Retreiving Data...")
    data = IL.getData()
    X, Y = IL.splitData(data)
    X = _dividePixelValue(X)
    IL.setMeanAndSTD(X)
    print("Z Scoring...")
    X = IL.zScore(X)
    return X, Y

def prepP3(IL):
    print("Retreiving Data...")
    data = IL.getData()
    data = IL.shuffleData(data, 0)
    IL.splitDataP3(data)
    IL.trainX = _dividePixelValue(IL.trainX)
    IL.validX = _dividePixelValue(IL.validX)
    IL.setMeanAndSTD(IL.trainX)
    print("Z Scoring...")
    IL.trainX = IL.zScore(IL.trainX)
    IL.validX = IL.zScore(IL.validX)
