import math
from eval import *

class Run:
    def __init__(self, epoch, epoch_list, eta):
        self.epoch = epoch
        self.epoch_list = epoch_list
        self.eta = eta

    def binaryLogisticalRegression(self, logLoss, evaluation, weights, IL):
        while self.epoch <= 50000:
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
        print("Training:\nAccuracy: {}\nPrecision: {}\nRecall: {}\nF-Measure: {}\n".format(evaluation.accuracy, evaluation.precision, evaluation.recall, evaluation.f))
        
        evaluation.setPosAndNeg(IL.validY, validYhat, .5)
        evaluation.setAccuracy()
        evaluation.setPrecision()
        evaluation.setRecall()
        evaluation.setF_Measure()
        print("Validation:\nAccuracy: {}\nPrecision: {}\nRecall: {}\nF-Measure: {}\n".format(evaluation.accuracy, evaluation.precision, evaluation.recall, evaluation.f))

        for i in range(11):
            evaluation.setPosAndNeg(IL.trainY, trainYhat, (i/10))
            evaluation.setPrecision()
            evaluation.setRecall()
            evaluation.setPR("train")

        for i in range(11):
            evaluation.setPosAndNeg(IL.validY, validYhat, (i/10))
            evaluation.setPrecision()
            evaluation.setRecall()
            evaluation.setPR("valid")
            

    def multiclassLogisticalRegression(self, logLoss, evaluation, weights, IL):
        while self.epoch <= 1000:
            #Check Conditionals
            if self.epoch % 100 == 0:
                print("Epoch: {}\n".format(self.epoch))
                
            if self.epoch > 3:
                change1 = abs(logLoss.mean1v2[self.epoch-1] - logLoss.mean1v2[self.epoch-2])
                change2 = abs(logLoss.mean1v3[self.epoch-1] - logLoss.mean1v3[self.epoch-2])
                change3 = abs(logLoss.mean2v3[self.epoch-1] - logLoss.mean2v3[self.epoch-2])
                if change1 < math.pow(2, -32) or change2 < math.pow(2, -32) or change3 < math.pow(2, -32):
                    break

            #Get Yhat        
            trainYhat_1v2 = evaluation.calcMulticlass(IL.trainX, weights, "1v2")
            weights.set_dJdW(IL.trainX, IL.trainY, trainYhat_1v2)
            weights.set_dJdb(IL.trainY, trainYhat_1v2)
            weights.updateWAndBMulticlass(self.eta, "1v2")
            logLoss.evalMulticlass(IL.trainY, trainYhat_1v2, "1v2")

            trainYhat_1v3 = evaluation.calcMulticlass(IL.trainX, weights, "1v3")
            weights.set_dJdW(IL.trainX, IL.trainY, trainYhat_1v3)
            weights.set_dJdb(IL.trainY, trainYhat_1v3)
            weights.updateWAndBMulticlass(self.eta, "1v3")
            logLoss.evalMulticlass(IL.trainY, trainYhat_1v3, "1v3")

            trainYhat_2v3 = evaluation.calcMulticlass(IL.trainX, weights, "2v3")
            weights.set_dJdW(IL.trainX, IL.trainY, trainYhat_2v3)
            weights.set_dJdb(IL.trainY, trainYhat_2v3)
            weights.updateWAndBMulticlass(self.eta, "2v3")
            logLoss.evalMulticlass(IL.trainY, trainYhat_2v3, "2v3")

            validYhat = evaluation.calcMulticlass(IL.validX, weights, "valid")
            #pdb.set_trace()

            #Objective Function Evaluation
            logLoss.eval(IL.validY, validYhat, "valid")

            #Incremenet values
            self.epoch_list.append(self.epoch)
            self.epoch += 1
        print(validYhat)
        pdb.set_trace()

