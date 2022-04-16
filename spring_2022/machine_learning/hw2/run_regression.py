import math
from eval import *

class Run:
    def __init__(self, epoch, epoch_list, eta):
        self.epoch = epoch
        self.epoch_list = epoch_list
        self.eta = eta

    def binaryLogisticalRegression(self, logLoss, evaluation, weights, IL):
        while self.epoch <= 500:
            #Check Conditionals
            if self.epoch % 100 == 0:
                print("Epoch: {}\nAccuracy: {}\nPrecision: {}\nRecall: {}\nF-Measure: {}\n".format(self.epoch, evaluation.accuracy, evaluation.precision, evaluation.recall, evaluation.f))
                
            if self.epoch > 3:
                change = abs(logLoss.meanTrain[self.epoch-1] - logLoss.meanTrain[self.epoch-2])
                if change < math.pow(2, -32):
                    break

            #Get Yhat        
            trainYhat = evaluation.calcYhat(IL.trainX, weights)
            validYhat = evaluation.calcYhat(IL.validX, weights)

            #Objective Function Evaluation
            logLoss.eval(IL.trainY, trainYhat, "train")
            logLoss.eval(IL.validY, validYhat, "valid")

            #Statistics Evaluations
            evaluation.setPosAndNeg(IL.trainY, trainYhat)
            evaluation.setAccuracy()
            evaluation.setPrecision()
            evaluation.setRecall()
            evaluation.setF_Measure()

            #Set Weight and Bias derivatives
            weights.set_dJdW(IL.trainX, IL.trainY, trainYhat)
            weights.set_dJdb(IL.trainY, trainYhat)

            #Update Weights with derivatives
            weights.updateWeightsAndBias(self.eta)

            #Incremenet values
            self.epoch_list.append(self.epoch)
            self.epoch += 1

