from matplotlib import pyplot as plt
import math
import numpy as np
from objective_func import *

def ADAM(eta, gradIn, epoch):
    print("ADAM")
    rho1 = .9
    rho2 = .999
    delta = .00000001
    r = 0
    s = 0

    J = gradIn
    s = rho1 * s + (1-rho1) * J
    r = rho2 * r + (1-rho2) * (J * J)
    pdb.set_trace()
    combined = (s/(1- math.pow(rho1, epoch)))/(math.sqrt(r/(1-math.pow(rho2, epoch))) + delta)
    return combined

