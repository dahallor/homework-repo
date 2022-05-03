import numpy as np
import math
import pdb

class Normals:
    def __init__(self):
        self.mean_not_spam = 0
        self.std_not_spam = 0
        self.mean_spam = 0
        self.std_spam = 0

        self.mean1 = 0
        self.std1 = 0
        self.mean2 = 0
        self.std2 = 0
        self.mean3 = 0
        self.std3 = 0

    def setNormalModelsp2(self, trainX0, trainX1):
        self.mean_not_spam = np.mean(trainX0, axis=0)
        self.std_not_spam = np.std(trainX0, axis=0)
        self.mean_spam = np.mean(trainX1, axis=0)
        self.std_spam = np.std(trainX1, axis=0)

    def setNormalModelsP4(self, trainX1, trainX2, trainX3):
        self.mean1 = np.mean(trainX1, axis=0)
        self.std1 = np.std(trainX1, axis=0)
        self.mean2 = np.mean(trainX2, axis=0)
        self.std2 = np.std(trainX2, axis=0)
        self.mean3 = np.mean(trainX3, axis=0)
        self.std3 = np.std(trainX3, axis=0)


    

