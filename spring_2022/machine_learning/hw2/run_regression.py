import math
from eval import *

class Run:
    def __init__(self, epoch, epoch_list, eta):
        self.epoch = epoch
        self.epoch_list = epoch_list
        self.eta = eta

    def binaryLogisticalRegression(self, logLoss, evaluation, weights, IL):
        while self.epoch <= 1000000:
            #Check Conditionals
            if self.epoch % 100 == 0:
                print("Epoch: {}\n".format(self.epoch))
                
            if self.epoch > 3:
                change = abs(logLoss.meanTrain[self.epoch-1] - logLoss.meanTrain[self.epoch-2])
                if change < math.pow(2, -32):
                    break

            #Get Yhat        
            trainYhat = evaluation.calcProbability(IL.trainX, weights)
            validYhat = evaluation.calcProbability(IL.validX, weights)

            #Objective Function Evaluation
            logLoss.eval(IL.trainY, trainYhat, "train")
            logLoss.eval(IL.validY, validYhat, "valid")

            #Set Weight and Bias derivatives
            weights.set_dJdW(IL.trainX, IL.trainY, trainYhat)
            weights.set_dJdb(IL.trainY, trainYhat)

            #Update Weights with derivatives
            weights.updateWeightsAndBias(self.eta)

            #Incremenet values
            self.epoch_list.append(self.epoch)
            self.epoch += 1

        #Statistics Evaluations
        evaluation.setPosAndNeg(IL.trainY, trainYhat, .5)
        evaluation.setAccuracy()
        evaluation.setPrecision()
        evaluation.setRecall()
        evaluation.setF_Measure()
        print("Accuracy: {}\nPrecision: {}\nRecall: {}\nF-Measure: {}\n".format(evaluation.accuracy, evaluation.precision, evaluation.recall, evaluation.f))

        for i in range(11):
            evaluation.setPosAndNeg(IL.trainY, trainYhat, (i/10))
            evaluation.setPrecision()
            evaluation.setRecall()
            evaluation.setPR()
        print(evaluation.prec_PR, evaluation.recall_PR)
            

