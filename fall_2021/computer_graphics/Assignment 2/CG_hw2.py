import math
import sys



def set_point_arrays(length, j):
    i = 0
    k = 0
    #enters input into x, y, and z arrays
    for i in range(j):
        if i < 2:
            temp = userData[k]
            x_tangent_point.append(temp)
            temp = userData[k+1]
            y_tangent_point.append(temp)
            temp = userData[k+2]
            z_tangent_point.append(temp)
            k += 3
            i += 1
        else:
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
    global t
    num_elements = len(sys.argv[:])
    i = 0

    for i in range(num_elements):
        if sys.argv[i] == "-n":
            n = int(sys.argv[i+1])
        if sys.argv[i] == "-r":
            r = float(sys.argv[i+1])
        if sys.argv[i] == "-f":
            inputfile = str(sys.argv[i+1])
        if sys.argv[i] == "-t":
            t = float(sys.argv[i+1])
        i += 1
    return

def draw_hermite(xq0, yq0, zq0, xq1, yq1, zq1, xt0, yt0, zt0, xt1, yt1, zt1, t, u):

    x = (2 * math.pow(u, 3) - 3 * math.pow(u, 2) + 1) * xq0 + (-2 * math.pow(u, 3) + 3 * math.pow(u, 2)) * xq1 + (math.pow(u, 3) - 2 * math.pow(u, 2) + u) * xt0 + (math.pow(u, 3) - math.pow(u, 2)) * xt1

    y = (2 * math.pow(u, 3) - 3 * math.pow(u, 2) + 1) * yq0 + (-2 * math.pow(u, 3) + 3 * math.pow(u, 2)) * yq1 + (math.pow(u, 3) - 2 * math.pow(u, 2) + u) * yt0 + (math.pow(u, 3) - math.pow(u, 2)) * yt1

    z = (2 * math.pow(u, 3) - 3 * math.pow(u, 2) + 1) * zq0 + (-2 * math.pow(u, 3) + 3 * math.pow(u, 2)) * zq1 + (math.pow(u, 3) - 2 * math.pow(u, 2) + u) * zt0 + (math.pow(u, 3) - math.pow(u, 2)) * zt1

    xCoord.append(x)
    yCoord.append(y)
    zCoord.append(z)
    
    
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
        if i == j-1:
           
                output.write("{:.6f} {:.6f} {:.6f}\n] {}".format(xCoord[i], yCoord[i], zCoord[i], "}"))

                
        i += 1

    
    
    output.write("\nIndexedLineSet {coordIndex [\n")
    i = 0
    
    j = len(IndexedLineSet)
    for i in range(j):
        output.write("{}, ".format(IndexedLineSet[i]))
        if i % 63 == 0 and i >= 63:
            output.write("-1, {}, ".format(IndexedLineSet[i]))
    
    IndexedLineSet.append(-1)
    sizeof = len(IndexedLineSet)
    output.write("{}".format(IndexedLineSet[sizeof-1]))
    output.write("\n] } }")



    i=0
    j = len(xPoint)
    for i in range(j):
        output.write("\nSeparator {{LightModel {{model PHONG}}Material {{\tdiffuseColor 1.0 1.0 1.0}}\nTransform {{translation\n {}  {}  {}  \n}}Sphere {{\tradius {} }}}}".format(xPoint[i], yPoint[i], zPoint[i], r))
    
   

    return

def get_t0(x0, y0, z0, x2, y2, z2, t):
    xt0 = (1-t) * .5 * (x2 - x0)
    yt0 = (1-t) * .5 * (y2 - y0)
    zt0 = (1-t) * .5 * (z2 - z0)

    return xt0, yt0, zt0 

def get_t1(x1, y1, z1, x3, y3, z3, t):
    xt1 = (1-t) * .5 * (x3 - x1)
    yt1 = (1-t) * .5 * (y3 - y1)
    zt1 = (1-t) * .5 * (z3 - z1)

    return xt1, yt1, zt1

def T0_prime(xt0, yt0, zt0, t):
    xt0 = (1-t) * xt0
    yt0 = (1-t) * yt0
    zt0 = (1-t) * zt0

    return xt0, yt0, zt0
 
def Tn_prime(xt1, yt1, zt1, t):
    xt1 = (1-t) * xt1
    yt1 = (1-t) * yt1
    zt1 = (1-t) * zt1
    return xt1, yt1, zt1

def print_to_terminal():
    #for testing before writing out to file
    i = 0
    j = len(xCoord)
    for i in range (j):
        print("{:.6f} {:.6f} {:.6f}".format(xCoord[i], yCoord[i], zCoord[i]))
        i += 1

if __name__ == "__main__":

    n = 11
    r = .1
    t = 0
    inputfile = "ctps_in.txt"
    r = float(r)
    n = int(n)
    t = float(t)
    du = 1/n
    u = 0

    userData = []

    x_tangent_point = []
    y_tangent_point = []
    z_tangent_point = []



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
    j = length//3
    set_point_arrays(length, j)
    i = 0

    size = len(xPoint)
    



    for i in range(size - 1):
        j = 0
        u = 0
        if size == 2:
            xt0, yt0, zt0 = T0_prime(x_tangent_point[0], y_tangent_point[0], z_tangent_point[0], t)
            xt1, yt1, zt1 = Tn_prime(x_tangent_point[1], y_tangent_point[1], z_tangent_point[1], t)
        if size >= 4:
            if xPoint[i] == xPoint[0]:
                xt0, yt0, zt0 = T0_prime(x_tangent_point[0], y_tangent_point[0], z_tangent_point[0], t)
                xt1, yt1, zt1 = get_t1(xPoint[i], yPoint[i], zPoint[i], xPoint[i+2], yPoint[i+2], zPoint[i+2], t)
            elif xPoint[i+1] == xPoint[size-1]:
                xt0, yt0, zt0 = get_t0(xPoint[i-1], yPoint[i-1], zPoint[i-1], xPoint[i+1], yPoint[i+1], zPoint[i+1], t)
                xt1, yt1, zt1 = Tn_prime(x_tangent_point[1], y_tangent_point[1], z_tangent_point[1], t)
            elif xPoint[i] != xPoint[0] or xPoint[i+1] != xPoint[size-1]:
                xt0, yt0, zt0 = get_t0(xPoint[i-1], yPoint[i-1], zPoint[i-1], xPoint[i+1], yPoint[i+1], zPoint[i+1], t)
                xt1, yt1, zt1 = get_t1(xPoint[i], yPoint[i], zPoint[i], xPoint[i+2], yPoint[i+2], zPoint[i+2], t)
        
        for j in range(n):
            draw_hermite(xPoint[i], yPoint[i], zPoint[i], xPoint[i+1], yPoint[i+1], zPoint[i+1], xt0, yt0, zt0, xt1, yt1, zt1, t, u)
            j += 1
            u += du
        i += 1
        
    xCoord.append(xPoint[size-1])
    yCoord.append(yPoint[size-1])
    zCoord.append(zPoint[size-1])

    write_out(n)
    

    


    




