import numpy as np
import pdb

def prep_data_p2(IL):
    data = IL.getSpamItems()
    data = IL.shuffleData(data, 0)
    IL.splitDataSpam(data)
    IL.setStatsInfo(IL.trainX)
    IL.zScore("train")
    IL.zScore("valid")
    seperateTypesp2(IL)

def prep_data_p3(IL):
    data = IL.getSpamItems()
    data = IL.shuffleData(data, 0)
    IL.splitDataSpam(data)
    IL.setStatsInfo(IL.trainX)
    IL.zScore("train")
    IL.zScore("valid")
    IL.setZscoredMedian()

def prep_data_p4(IL):
    data = IL.getCartData()
    data = IL.shuffleData(data, 0)
    IL.splitDataSpam(data)
    IL.setStatsInfo(IL.trainX)
    IL.zScore("train")
    IL.zScore("valid")
    seperateTypesP4(IL)

def seperateTypesp2(IL):
    for i in range(len(IL.trainX)):
        match IL.trainY[i][0]:
            case 0:
                IL.trainX0 = np.append(IL.trainX0, IL.trainX[i])
                IL.trainY0 = np.append(IL.trainY0, IL.trainY[i])
            case 1:
                IL.trainX1 = np.append(IL.trainX1, IL.trainX[i])
                IL.trainY1 = np.append(IL.trainY1, IL.trainY[i])
            case _:
                raise Exception("Issue with seperation by spam type")
    IL.trainX0 = IL.trainX0.reshape(-1, len(IL.trainX[0]))
    IL.trainY0 = IL.trainY0.reshape(-1, 1)
    IL.trainX1 = IL.trainX1.reshape(-1, len(IL.trainX[0]))
    IL.trainY1 = IL.trainY1.reshape(-1, 1)
    
    
def seperateTypesP4(IL):
    for i in range(len(IL.trainX)):
        match IL.trainY[i][0]:
            case 1:
                IL.trainX1 = np.append(IL.trainX1, IL.trainX[i])
                IL.trainY1 = np.append(IL.trainY1, IL.trainY[i])
            case 2:
                IL.trainX2 = np.append(IL.trainX2, IL.trainX[i])
                IL.trainY2 = np.append(IL.trainY2, IL.trainY[i])
            case 3:
                IL.trainX3 = np.append(IL.trainX3, IL.trainX[i])
                IL.trainY3 = np.append(IL.trainY3, IL.trainY[i])
            case _:
                raise Exception("Error when seperating Class Types")
    IL.trainX1 = IL.trainX1.reshape(-1, len(IL.trainX[0]))
    IL.trainY1 = IL.trainY1.reshape(-1, 1)
    IL.trainX2 = IL.trainX2.reshape(-1, len(IL.trainX[0]))
    IL.trainY2 = IL.trainY2.reshape(-1, 1)
    IL.trainX3 = IL.trainX3.reshape(-1, len(IL.trainX[0]))
    IL.trainY3 = IL.trainY3.reshape(-1, 1)