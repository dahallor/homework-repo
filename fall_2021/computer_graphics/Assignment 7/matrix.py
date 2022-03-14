import numpy
import math

def translation_matrix(P, Ln):
    dx = 0
    dy = 0
    dz = Ln

    translation = numpy.array([[1, 0, 0, dx], [0, 1, 0, dy], [0, 0, 1, dz], [0, 0, 0, 1]])

    return translation

def rotation_matrix(theta, value):
    degree = theta/360 * (2 * math.pi)
    cos =  math.cos(degree)
    sin = math.sin(degree)
    neg_sin = -1 * sin
    if value == "x":
        Rx = numpy.array([[1, 0, 0, 0], [0, cos, neg_sin, 0], [0, sin, cos, 0], [0, 0, 0, 1]])
        return Rx
    if value == "y":
        Ry = numpy.array([[cos, 0, sin, 0], [0, 1, 0, 0], [neg_sin, 0, cos, 0], [0, 0, 0, 1]])
        return Ry
    if value == "z":
        Rz = numpy.array([[cos, neg_sin, 0, 0], [sin, cos, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        return Rz

