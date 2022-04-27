import numpy as np
import math
import pdb

class Normals:
    def setNormals(self, IL):
        #trainX0
        prob = []
        for i in range(len(IL.trainX0)):
            temp = []
            for j in range(len(IL.trainX0[i])):
                x = IL.trainX0[i][j]
                mu = IL.mean[j]
                var = IL.var[j]
                std = IL.std[j]

                exponent = -1 * ((math.pow((x - mu), 2))/(2 * var))
                e = np.exp(exponent)
                p = 1/(std * np.sqrt((2 * math.pi))) * e
                temp.append(p)
                
            prob.append(temp)
            pdb.set_trace()
