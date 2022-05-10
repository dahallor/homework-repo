import pdb

def prepP2(IL):
    data = IL.getData()
    X, Y = IL.splitData(data)
    IL.setMeanAndSTD(X)
    X = IL.zScore(X)
    pdb.set_trace()
    X = IL.reshape(X)
    pdb.set_trace()
