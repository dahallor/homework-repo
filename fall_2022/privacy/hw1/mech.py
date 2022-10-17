import random
import numpy as np
import pdb

class Mechanism:
    def random_response(X, gamma):
        random_num = random.random()
        truth_threshold = .5 + gamma
        if random_num >= truth_threshold:
            Y = X
        else:
            Y = 1-X
        return Y

    #f = true value
    #delta = sensativity
    #epsilon = privacy parameter
    # r = random draw from laplace
    def laplace(f, delta, epsilon):
        mu = 0
        b = delta/epsilon
        r = np.random.laplace(mu, b, 1)
        return r[0]

    
    def guassian(f, delta, epsilon, theta):
        mu = 0
        x = 1/theta
        sigma = np.sqrt(np.log(x) * (delta/epsilon))
        r = np.random.normal(mu, sigma, 1)
        return r[0]