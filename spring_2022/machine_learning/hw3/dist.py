import numpy as np
import math
import pdb

class Normals:
    def __init__(self):
        self.mean_not_spam = 0
        self.std_not_spam = 0
        self.mean_spam = 0
        self.std_spam = 0

    def setStatsp2(self, trainX0, trainX1):
        self.mean_not_spam = np.mean(trainX0, axis=0)
        self.std_not_spam = np.std(trainX0, axis=0)
        self.mean_spam = np.mean(trainX1, axis=0)
        self.std_spam = np.std(trainX1, axis=0)

