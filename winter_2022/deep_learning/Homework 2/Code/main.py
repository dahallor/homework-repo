import numpy
from act_func import *
from objective_func import *
from fully_connect import FullyConnectedLayer
from input import *
import sys


if __name__ == '__main__':
    numpy.set_printoptions(threshold=sys.maxsize)

    #For act func gradient
    h = numpy.array([[1, 2, 3, 4]])

    act_lin = LinearLayer()
    act_relu = ReLuLayer()
    act_sig = SigmoidLayer()
    act_tanh = TanhLayer()
    act_soft = SoftmaxLayer()
    obj_squares = LeastSquares()
    obj_log = LogLoss()
    obj_CE = CrossEntropy()

    y = 0
    yhat = .2
    y_CE = numpy.array([1, 0, 0])
    yhat_CE = numpy.array([[.2, .2, .6]])


    #Uncomment this to run Section 4 of HW2
    '''
    featuresIn = len(h[0])
    featuresOut = 2
    fc = FullyConnectedLayer(int(featuresIn), int(featuresOut))
    Y = fc.forward(h)

    #To see output of FC using Input Layer
    print("Fully Connected:")
    print(Y)
    delta = fc.gradient()
    print("Fully Connected Gradient:")
    print(delta)
    

    print("Pick the number coresponding to the activation rate you wish to use")
    print("1) Linear\n2) ReLu Linear\n3) Sigmoid\n4) TanH\n5) Softmax")
    i = int(input())
    
    if i == 1:
        print("Linear")
        print(act_lin.forward(h))
        print("Activation Gradient:")
        delta = act_lin.gradient()
        print(delta)
    if i == 2:
        print("RELU")
        print(act_relu.forward(h))
        print("Activation Gradient:")
        delta = act_relu.gradient()
        print(delta)
    if i == 3:
        print("Sigmoid")    
        print(act_sig.forward(h))
        print("Activation Gradient:")
        delta = act_sig.gradient()
        print(delta)
    if i == 4:
        print("Tanh")
        print(act_tanh.forward(h))
        print("Activation Gradient:")
        delta = act_tanh.gradient()
        print(delta)
    if i == 5:
        print("Softmax")
        print(act_soft.forward(h))
        print("Activation Gradient:")
        delta = act_soft.gradient()
        print(delta)
    '''


    #For section 5 of HW2
    print("Least Squares Eval:")
    print(obj_squares.eval(y, yhat))
    print("Least Squares Gradient:")
    print(obj_squares.gradient(y, yhat))

    print("Log Loss Eval:")
    print(obj_log.eval(y, yhat))
    print("Log Loss Gradient:")
    print(obj_log.gradient(y, yhat))

    print("Cross Entropy Eval:")
    print(obj_CE.eval(y_CE, yhat_CE))
    print("Cross Entropy Gradient:")
    print(obj_CE.gradient(y_CE, yhat_CE))
