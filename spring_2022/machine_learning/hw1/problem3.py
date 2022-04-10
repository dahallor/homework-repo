from input import *
from weights import *
from eval import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    weights = Weights()
    eval = Evaluation()

    S = 20
    S4 = np.array([])
    S11 = np.array([])
    S22 = np.array([])
    SN = np.array([])

    RMSEs = np.array([])

    #For S Folds
    for i in range(1, S+1, 1):
        errors = []
        data = inputLayer.getCSVItems()
        data = inputLayer.shuffleData(data, i)
        X, Y = inputLayer.splitDataCrossValidation(data)
        X = inputLayer.addDummyValueCrossValidation(X)
        N = inputLayer.getDimensionality(S, X)
        for j in range(N):
            trainX, trainY, validX, validY = inputLayer.S_folds(j, S, X, Y)
            trainX, trainY = inputLayer.reassemble(trainX, trainY)
            
            w = weights.setWeights(trainX, trainY)

            
            validYhat = eval.calcYhat(validX, w)
            errors = eval.SE(validY, validYhat, errors)
            
            match j:
                case 3:
                    root = eval.RMSEfromSE(errors)
                    S4 = np.append(S4, root)
                case 10:
                    root = eval.RMSEfromSE(errors)
                    S11 = np.append(S11, root)
                case 21:
                    root = eval.RMSEfromSE(errors)
                    S22 = np.append(S11, root)
                case _:
                    continue

        '''
        root = eval.RMSEfromSE(errors)
        RMSEs = np.append(RMSEs, root)
        #pdb.set_trace()
        '''
    print("S = 4")
    print("Mean = {}".format(np.mean(S4)))
    print("STD = {}".format(np.std(S4)))

    print("S = 11")
    print("Mean = {}".format(np.mean(S11)))
    print("STD = {}".format(np.std(S11)))

    print("S = 22")
    print("Mean = {}".format(np.mean(S22)))
    print("STD = {}".format(np.std(S22)))
    
    #For N Folds/leave one out
    for i in range(1, S+1, 1):
        errors = []
        data = inputLayer.getCSVItems()
        data = inputLayer.shuffleData(data, i)
        X, Y = inputLayer.splitDataCrossValidation(data)
        X = inputLayer.addDummyValueCrossValidation(X)
        for j in range(len(X)):
            trainX, trainY, validX, validY = inputLayer.N_folds(j, X, Y)
            
            w = weights.setWeights(trainX, trainY)
            
            validYhat = eval.calcYhat(validX, w)
            errors = eval.SE(validY, validYhat, errors)

        root = eval.RMSEfromSE(errors)
        SN = np.append(SN, root)

    
    print("S = N")
    print("Mean = {}".format(np.mean(SN)))
    print("STD = {}".format(np.std(SN)))


        
