import numpy
from act_func import *
from fully_connect import FullyConnectedLayer
from input import *
import sys


if __name__ == '__main__':

    numpy.set_printoptions(threshold=sys.maxsize)
    #x = numpy.genfromtxt('../mcpd_augmented.csv', delimiter = ',')
    #To sample test matrix
    x = numpy.array([[1, 7777777, 3.8998989898, 4], [5, 6, 7, 90909090909090909]])

    input_layer = InputLayer(x)
    act_lin = LinearLayer()
    act_relu = ReLuLayer()
    act_sig = SigmoidLayer()
    act_tanh = TanhLayer()
    act_soft = SoftmaxLayer()

    
    z = input_layer.forward(x)
    #To get output of just input layer
    print("Input Layer:")
    print(z)

    featuresIn = len(z[0])
    featuresOut = 2

    fc = FullyConnectedLayer(int(featuresIn), int(featuresOut))
    Y = fc.forward(z)
    #To get output from just FC Layer
    #print(fc.forward(x))

    #To see output of FC using Input Layer
    #print("Fully Connected:")
    #print(Y)

    final = act_sig.forward(Y)
    #To see print output of final layer
    #print("Sigmoid:")
    #print(final)
    final = str(final)

    f = open('./results.txt', 'w')
    f.write(final)
    f.close()
'''
    print("Pick the number coresponding to the activation rate you wish to use")
    print("1) Linear\n2) ReLu Linear\n3) Sigmoid\n4) TanH\n5) Softmax")
    i = int(input())
    
    if i == 1:
        print("Linear")
        print(act_lin.forward(x))
    if i == 2:
        print("RELU")
        y = act_relu.forward(x)
        print(y)
    if i == 3:
        print("Sigmoid")    
        print(act_sig.forward(x))
    if i == 4:
        print("Tanh")
        print(act_tanh.forward(x))
    if i == 5:
        print("Softmax")
        print(act_soft.forward(x))
'''