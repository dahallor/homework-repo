from matrix import *
from polygons import *
import numpy
import math
import pdb
import copy

def computation(P0, P1, P2, P3, theta1, theta2, theta3):
    #first level
    Tz0 = translation_matrix(P0, P0.start2[2])
    Rz1 = rotation_matrix(theta1, "z")
    M1 = Tz0.dot(Rz1)

    P1_prime = []
    for i in range(8):
        temp1 = copy.deepcopy(numpy.array([[P1.coordinates[i][0]], [P1.coordinates[i][1]], [P1.coordinates[i][2]], [1]]))
        temp2 = M1.dot(temp1)
        temp3 = []
        temp3.append(temp2[0])
        temp3.append(temp2[1])
        temp3.append(temp2[2])
        P1_prime.append(temp3)
 
    #second level
    Tz1 = translation_matrix(P1, P1.start2[2])
    Ry2 = rotation_matrix(theta2, "y")
    temp = Tz1.dot(Ry2)
    M2 = M1.dot(temp)
 
    P2_prime = []
    for i in range(8):
        temp1 = copy.deepcopy(numpy.array([[P2.coordinates[i][0]], [P2.coordinates[i][1]], [P2.coordinates[i][2]], [1]]))
        temp2 = M2.dot(temp1)
        temp3 = []
        temp3.append(temp2[0])
        temp3.append(temp2[1])
        temp3.append(temp2[2])
        P2_prime.append(temp3)

    #third level
    Tz2 = translation_matrix(P2, P2.start2[2])
    Ry3 = rotation_matrix(theta3, "y")
    temp = Tz2.dot(Ry3)
    M3 = M2.dot(temp)

 
    P3_prime = []
    for i in range(8):
        temp1 = copy.deepcopy(numpy.array([[P3.coordinates[i][0]], [P3.coordinates[i][1]], [P3.coordinates[i][2]], [1]]))
        temp2 = M3.dot(temp1)
        temp3 = []
        temp3.append(temp2[0])
        temp3.append(temp2[1])
        temp3.append(temp2[2])
        P3_prime.append(temp3)
  
    #final level
    Tz3 = translation_matrix(P3, P3.start2[2])
    M4 = M3.dot(Tz3)
    #extract final vector
    origin = numpy.array([0, 0, 0, 1])
    end_point = M4.dot(origin)
    

    return P1_prime, P2_prime, P3_prime, end_point

    
