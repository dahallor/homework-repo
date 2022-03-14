import math
import sys


def set_point_arrays(length, j):
    i = 0
    k=0    
    for i in range(j):
        temp = userData[k]
        xPoint.append(temp)
        temp = userData[k+1]
        yPoint.append(temp)
        temp = userData[k+2]
        zPoint.append(temp)
        k += 3
        i+=1
    return j

def command_line():
    global n
    global r
    global inputfile
    num_elements = len(sys.argv[:])
    i = 0

    for i in range(num_elements):
        if sys.argv[i] == "-n":
            n = int(sys.argv[i+1])
        if sys.argv[i] == "-r":
            r = float(sys.argv[i+1])
        if sys.argv[i] == "-f":
            inputfile = str(sys.argv[i+1])
        i += 1
    return



def draw_curves(k, u):
    totalx = 0
    totaly = 0
    totalz = 0
    degree = k - 1

    for i in range(k):
        parameter = (1-u)
        coef = math.factorial(degree)/(math.factorial(i) * math.factorial((degree-i)))
        pointx = xPoint[i]
        pointy = yPoint[i]
        pointz = zPoint[i]

        totalx += coef * math.pow(parameter, degree - i) *math.pow(u, i) * pointx
        totaly += coef * math.pow(parameter, degree - i) * math.pow(u, i) * pointy
        totalz += coef * math.pow(parameter, degree - i) * math.pow(u, i) * pointz

    xCoord.append(totalx)
    yCoord.append(totaly)
    zCoord.append(totalz)






def read_file(userData):
    f = open(inputfile, "r")
    lines = f.readlines()
    for line in lines:
        temp = line.split(" ")
        userData.append(float(temp[0]))
        userData.append(float(temp[1]))
        stripped = temp[2]
        stripped = stripped.strip("\n")
        userData.append(float(stripped))
    return userData

def write_out(n):
    PREFIX = "#Inventor V2.0 ascii\n\n\nSeparator {LightModel {model BASE_COLOR} Material {diffuseColor 1.0 1.0 1.0}\nCoordinate3 {\tpoint [ \n"

    IndexedLineSet = []

    output = open("out.iv", "w")
    output.write(PREFIX)
    i = 0
    j = len(xCoord)
    for i in range(j):
        IndexedLineSet.append(i)
        output.write("{:.6f} {:.6f} {:.6f},\n".format(xCoord[i], yCoord[i], zCoord[i]))
        i += 1
    output.write("] }\n")
    IndexedLineSet.append(-1)
    output.write("\nIndexedLineSet {coordIndex [\n")
    i = 0
    j = len(IndexedLineSet)
    for i in range(j):
        output.write("{}, ".format(IndexedLineSet[i]))
    output.write("\n] } }") 
    i=0
    j = len(xPoint)
    for i in range(j):
        output.write("\nSeparator {{LightModel {{model PHONG}}Material {{\tdiffuseColor 1.0 1.0 1.0}}\nTransform {{translation\n {}  {}  {}  \n}}Sphere {{\tradius {} }}}}".format(xPoint[i], yPoint[i], zPoint[i], r))
        i += 1

    return

def print_to_terminal():
    f = open("out.iv", "r")
    print(f.read())


if __name__ == "__main__":

    n = 20
    r = .1
    inputfile = "ctps_in.txt"
    r = float(r)
    n = int(n)
    du = 1/n
    u = 0

    userData = []

    xPoint = []
    yPoint = []
    zPoint = []

    xCoord = []
    yCoord = []
    zCoord = []

    command_line()
    du = 1/n
    read_file(userData)
    length = len(userData)
    k = length//3
    set_point_arrays(length, k)
    for count in range(n+1):
        draw_curves(k, u)
        u += du
    write_out(n)
    print_to_terminal()
