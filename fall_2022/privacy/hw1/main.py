import numpy as np
import sys
import pdb
from mech import Mechanism
from matplotlib import pyplot as plt

def parse_CSV():
    return np.genfromtxt(fname="CS590-HW1.csv", dtype=str, delimiter=",", skip_header=1)

def convert_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'y':
                array[i][j] = 1
            else:
                array[i][j] = 0
    array = array.astype('int32')
    return array

def get_physician_fee(array):
    #physician fee freeze at column index 3
    return array[:, 3]

def get_fee_sum(array):
    return sum(array)

def run_randomized_response(X, sumX):
    gamma = 0
    for i in range(3):
        sumY = 0
        for j in range(len(X)):
            Y = Mechanism.random_response(X[j][0], gamma)
            if Y == 1:
                sumY += 1
        print(f"gamma: {gamma} Total 1's in X: {sumX} Total 1's in Y:{sumY}")
        gamma += .25

def run_laplace(f):
    e = .1
    r = Mechanism.laplace(f, 1, e)
    print(f"epsilon: {e} Total 1's in f: {f} Amount of Laplace Noise: {r} Total of f+r: {int(f+r)}")
    e = 1
    r = Mechanism.laplace(f, 1, e)
    print(f"epsilon: {e} Total 1's in f: {f} Amount of Laplace Noise: {r} Total of f+r: {int(f+r)}")

def run_guassian(f):
    theta = .01
    e = .1
    r = Mechanism.guassian(f, 1, e, theta)
    print(f"epsilon: {e} Total 1's in f: {f} Amount of Guassian Noise: {r} Total of f+r: {int(f+r)}")
    e = 1
    r = Mechanism.guassian(f, 1, e, theta)
    print(f"epsilon: {e} Total 1's in f: {f} Amount of Guassian Noise: {r} Total of f+r: {int(f+r)}")

def compare_mechs(f):
    e = .1
    theta = .01
    laplace = []
    guassian = []
    y_axis_l = []
    y_axis_g = []
    for i in range(100):
        laplace.append(Mechanism.laplace(f, 1, e))
        guassian.append(Mechanism.guassian(f, 1, e, theta))
        y_axis_l.append(1)
        y_axis_g.append(2)
    plt.scatter(laplace, y_axis_l, c = "blue")
    plt.scatter(guassian, y_axis_g, c = "orange")
    plt.show()


if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    array = parse_CSV()
    array = convert_array(array)
    fee_col = get_physician_fee(array)
    sumX = get_fee_sum(fee_col)
    print(f"Total number of 1's in X: {sumX}\n")
    
    run_randomized_response(array, sumX)
    print()
    run_laplace(sumX)
    print()
    run_guassian(sumX)
    print()
    compare_mechs(sumX)


    