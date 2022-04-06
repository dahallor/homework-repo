from input import *
from weights import *
from eval import *

if __name__ == '__main__':
    inputLayer = InputLayer()
    weights = Weights()
    eval = Evaluation()

    S = 20

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

            '''
            validYhat = eval.calcYhat(validX, w)
            errors = eval.SE(validY, validYhat, errors)
            print(errors)
            #print("trainX: {}\nvalidX: {}\ntrainY: {}\n validY: {}\n".format(trainX, validX, trainY, validY))
            #print("trainY: {}\n validY: {}\n".format(trainY, validY))
            '''



    #For N Folds/leave one out


        
