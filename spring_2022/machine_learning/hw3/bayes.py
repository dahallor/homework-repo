import numpy as np
import math
import pdb


#Helpers
def _runBayes0(normals, P0, observation):
    probability_0 = P0
    for i in range(len(observation)):
        x = observation[i]
        mean = normals.mean_not_spam[i]
        std = normals.std_not_spam[i]
        exponent = -1 * ((math.pow((x-mean), 2))/(2 * math.pow(std, 2)))
        denom = std * np.sqrt(2 * math.pi)
        Px = 1/denom * np.exp(exponent)
        probability_0 *= Px
    return probability_0
    

def _runBayes1(normals, P1, observation):
    probability_1 = P1
    for i in range(len(observation)):
        x = observation[i]
        mean = normals.mean_spam[i]
        std = normals.std_spam[i]
        exponent = -1 * ((math.pow((x-mean), 2))/(2 * math.pow(std, 2)))
        denom = std * np.sqrt(2 * math.pi)
        Px = 1/denom * np.exp(exponent)
        probability_1 *= Px
    return probability_1

def _runBayes1Cart(normals, P1, observation):
    probability_1 = P1
    for i in range(len(observation)):
        x = observation[i]
        mean = normals.mean1[i]
        std = normals.std1[i]
        exponent = -1 * ((math.pow((x-mean), 2))/(2 * math.pow(std, 2)))
        denom = std * np.sqrt(2 * math.pi)
        Px = 1/denom * np.exp(exponent)
        probability_1 *= Px
    return probability_1

def _runBayes2(normals, P2, observation):
    probability_2 = P2
    for i in range(len(observation)):
        x = observation[i]
        mean = normals.mean2[i]
        std = normals.std2[i]
        exponent = -1 * ((math.pow((x-mean), 2))/(2 * math.pow(std, 2)))
        denom = std * np.sqrt(2 * math.pi)
        Px = 1/denom * np.exp(exponent)
        probability_2 *= Px
    return probability_2

def _runBayes3(normals, P3, observation):
    probability_3 = P3
    for i in range(len(observation)):
        x = observation[i]
        mean = normals.mean3[i]
        std = normals.std3[i]
        exponent = -1 * ((math.pow((x-mean), 2))/(2 * math.pow(std, 2)))
        denom = std * np.sqrt(2 * math.pi)
        Px = 1/denom * np.exp(exponent)
        probability_3 *= Px
    return probability_3



class Bayes:
    def runNaiveBayesP2(self, normals, stats, IL):
        P0, P1 = self.getClassProbP2(IL.validY)
        for i in range(len(IL.validX)):
            observation = IL.validX[i]
            probability_0 = _runBayes0(normals, P0, observation)
            probability_1 = _runBayes1(normals, P1, observation)
            if max(probability_0, probability_1) == probability_0:
                yhat = 0
            if max(probability_0, probability_1) == probability_1:
                yhat = 1
            y = IL.validY[i]
            stats.addGuess(y, yhat)
            

    def getClassProbP2(self, validY):
        P0 = 0
        P1 = 0
        total = len(validY)
        for i in range(len(validY)):
            match validY[i]:
                case 0:
                    P0 += 1
                case 1:
                    P1 += 1
                case _:
                    raise Exception("Error when calculating class probability")
        P0 = P0/total
        P1 = P1/total
        return P0, P1

    def runNaiveBayesP4(self, normals, stats, IL):
        P1, P2, P3 = self.getClassProbP4(IL.validY)
        for i in range(len(IL.validX)):
            observation = IL.validX[i]
            probability_1 = _runBayes1Cart(normals, P1, observation)
            probability_2 = _runBayes2(normals, P2, observation)
            probability_3 = _runBayes3(normals, P3, observation)
            if max(probability_1, probability_2, probability_3) == probability_1:
                yhat = 1
            if max(probability_1, probability_2, probability_3) == probability_2:
                yhat = 2
            if max(probability_1, probability_2, probability_3) == probability_3:
                yhat = 3
            y = IL.validY[i]
            stats.addGuessMulticlass(y, yhat)
            

    def getClassProbP4(self, validY):
        P1 = 0
        P2 = 0
        P3 = 0
        total = len(validY)
        for i in range(len(validY)):
            match validY[i]:
                case 1:
                    P1 += 1
                case 2:
                    P2 += 1
                case 3:
                    P3 += 1
                case _:
                    raise Exception("Error when calculating class probability")
        P1 = P1/total
        P2 = P2/total
        P3 = P3/total
        return P1, P2, P3









