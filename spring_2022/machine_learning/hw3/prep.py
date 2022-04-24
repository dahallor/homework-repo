import numpy as np

def prep_data_p2(IL):
    data = IL.getSpamItems()
    data = IL.shuffleData(data, 0)
    IL.splitDataSpam(data)
    IL.setStatsInfo(IL.trainX)
    IL.zScore("train")
    IL.zScore("valid")
    seperateTypes(IL)


def seperateTypes(IL):
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
    
    