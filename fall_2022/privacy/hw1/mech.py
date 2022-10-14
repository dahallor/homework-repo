import random
import numpy as np

class Mechanism:
    def random_response(self, X, gamma):
        random_num = random.random()
        truth_threshold = .5 + gamma
        if random_num >= truth_threshold:
            Y = X
        else:
            Y = 1-X

    #f = true value
    #delta = sensativity
    #epsilon = privacy parameter
    # r = random draw from laplace
    def laplace(self, f, delta, epsilon):
        mu = 0
        b = delta/epsilon
        r = np.random.laplace(mu, b, 1)
        return f + r

    
    def guassian(self):
        pass