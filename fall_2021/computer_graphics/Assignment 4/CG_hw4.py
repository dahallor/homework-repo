import math
import sys
import numpy

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

def set_point_arrays(num_points, xPoint, yPoint, zPoint, x_tangent, y_tangent, z_tangent):  
    i = 0
    k = 0
    #enters input into x, y, and z arrays
    for i in range(num_points):
        if i < 2:
            temp = userData[k] 
            x_tangent.append(temp)
            temp = userData[k+1]
            y_tangent.append(temp)
            temp = userData[k+2]
            z_tangent.append(temp)
            k += 3
            i+=1
            continue
        else:
            temp = userData[k] 
            xPoint.append(temp)
            temp = userData[k+1]
            yPoint.append(temp)
            temp = userData[k+2]
            zPoint.append(temp)
            k += 3
            i+=1
    return xPoint, yPoint, zPoint, x_tangent, y_tangent, z_tangent

def command_line():
    global num_u
    global r
    global inputfile
    global shade
    global num_t
    global cap
    num_elements = len(sys.argv[:])
    i = 0

    for i in range(num_elements):
        if sys.argv[i] == "-u":
            num_u = int(sys.argv[i+1])
        if sys.argv[i] == "-t":
            num_t == int(sys.args[i+1])
        if sys.argv[i] == "-r":
            r = float(sys.argv[i+1])
        if sys.argv[i] == "-f":
            inputfile = str(sys.argv[i+1])
        if sys.argv[i] == "-F":
            shade = "flat"
        if sys.argv[i] == "-S":
            shade = "smooth"
        if sys.argv[i] == "-C":
            cap == "cap"
        i += 1
    return


def faceting(twoD_array, vertex):
    #TODO: nested for loops
    point = []
    k = 0
    num_curves = len(xPoint)-1
    for curve in range(num_curves):
        for i in range(num_u):
            for j in range(num_t): 
                point.append(k)
                k += 1
            twoD_array.append(point)
            point = []
     
    
    k=0
    count = 0
    
    while(1):
        if(k == len(twoD_array)-1):
            break
        for i in range(num_u-1):
            l = 0
            for j in range(num_t -1):
                
                vertex.append(twoD_array[k][l])
                vertex.append(twoD_array[k+1][l])
                vertex.append(twoD_array[k+1][l+1])
                vertex.append(-1)
                vertex.append(twoD_array[k][l])
                vertex.append(twoD_array[k+1][l+1])
                vertex.append(twoD_array[k][l+1])
                vertex.append(-1)
                l += 1
            k += 1
            if(k == len(twoD_array)-1):
                    break

                 
    return twoD_array, vertex


def hermite_u(xq0, yq0, zq0, xq1, yq1, zq1, xt0, yt0, zt0, xt1, yt1, zt1, u, theta):
    h1u = (2 * math.pow(u, 3) - 3 * math.pow(u, 2) + 1)
    h2u = (-2 * math.pow(u, 3) + 3 * math.pow(u, 2))
    h3u = (math.pow(u, 3) - 2 * math.pow(u, 2) + u)
    h4u = (math.pow(u, 3) - math.pow(u, 2))

    x = h1u * xq0 + h2u * xq1 + h3u * xt0 + h4u * xt1
    y = h1u * yq0 + h2u * yq1 + h3u * yt0 + h4u * yt1
    z = h1u * zq0 + h2u * zq1 + h3u * zt0 + h4u * zt1

    surface_theta(xq0, yq0, zq0, xq1, yq1, zq1, xt0, yt0, zt0, xt1, yt1, zt1, x, y, z, u, theta)
 
def get_tangents(size):
    for i in range(size - 1):
        j = 0
        k = 0
        theta = 0
        t = 0
        if size == 2:
            xt0, yt0, zt0 = T0_prime(x_tangent[0], y_tangent[0], z_tangent[0], t)
            xt1, yt1, zt1 = Tn_prime(x_tangent[1], y_tangent[1], z_tangent[1], t)
        if size >= 4:
            if xPoint[i] == xPoint[0]:
                xt0, yt0, zt0 = T0_prime(x_tangent[0], y_tangent[0], z_tangent[0], t)
                xt1, yt1, zt1 = get_t1(xPoint[i], yPoint[i], zPoint[i], xPoint[i+2], yPoint[i+2], zPoint[i+2], t)
            elif xPoint[i+1] == xPoint[size-1]:
                xt0, yt0, zt0 = get_t0(xPoint[i-1], yPoint[i-1], zPoint[i-1], xPoint[i+1], yPoint[i+1], zPoint[i+1], t)
                xt1, yt1, zt1 = Tn_prime(x_tangent[1], y_tangent[1], z_tangent[1], t)
            elif xPoint[i] != xPoint[0] or xPoint[i+1] != xPoint[size-1]:
                xt0, yt0, zt0 = get_t0(xPoint[i-1], yPoint[i-1], zPoint[i-1], xPoint[i+1], yPoint[i+1], zPoint[i+1], t)
                xt1, yt1, zt1 = get_t1(xPoint[i], yPoint[i], zPoint[i], xPoint[i+2], yPoint[i+2], zPoint[i+2], t)
        u = 0
        for k in range(num_u):
            for j in range(num_t):
                theta = j * dt * two_pi
                u = k * du
                hermite_u(xPoint[i], yPoint[i], zPoint[i], xPoint[i+1], yPoint[i+1], zPoint[i+1], xt0, yt0, zt0, xt1, yt1, zt1, u, theta)
        i += 1

    #hermite_u(xPoint[-2], yPoint[-2], zPoint[-2], xPoint[-1], yPoint[-1], zPoint[-1], xt0, yt0, zt0, xt1, yt1, zt1, 1, two_pi)
    

def surface_theta(xq0, yq0, zq0, xq1, yq1, zq1, xt0, yt0, zt0, xt1, yt1, zt1, x, y, z, u, theta):
    f_of_u = x
    g_of_u = z

    x = f_of_u * math.cos(theta)
    y = f_of_u * math.sin(theta)
    z = g_of_u

    xCoord.append(x)
    yCoord.append(y)
    zCoord.append(z) 
    if shade == "smooth":
        derivatives(xq0, yq0, zq0, xq1, yq1, zq1, xt0, yt0, zt0, xt1, yt1, zt1, f_of_u, u, theta)

def derivatives(xq0, yq0, zq0, xq1, yq1, zq1, xt0, yt0, zt0, xt1, yt1, zt1, f_of_u, u, theta):
    dh1 = (6 * math.pow(u, 2) - 6 * u)
    dh2 = (-6 * math.pow(u, 2) + 6 * u)
    dh3 = (3 * math.pow(u, 2) - 4 * u + 1)
    dh4 = (3 * math.pow(u, 2) - 2 * u)

    x = dh1 * xq0 + dh2 * xq1 + dh3 * xt0 + dh4 * xt1
    y = dh1 * yq0 + dh2 * yq1 + dh3 * yt0 + dh4 * yt1
    z = dh1 * zq0 + dh2 * zq1 + dh3 * zt0 + dh4 * zt1

    f_prime = x
    g_prime = z

    xu = f_prime * math.cos(theta)
    yu = f_prime * math.sin(theta)
    zu = g_prime

    xt = -1 * f_of_u * math.sin(theta)
    yt = f_of_u * math.cos(theta)
    zt = 0

    normals.append(yu * zt - yt * zu)
    normals.append(zu * xt - zt * xu)
    normals.append(xu * yt - xt * yu)

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

  
def write_out():
    #Header
    output = open("out.iv", "w")
    output.write("#Inventor V2.0 ascii\n\n")
    output.write("ShapeHints {\n\tvertexOrdering COUNTERCLOCKWISE\n}\n")
    output.write("Separator {\n\tCoordinate3 {\n\t\tpoint [\n")
    
    #coordinaates
    i = 0
    for i in range(len(xCoord)):
        output.write("\t\t\t{:.6f} {:.6f} {:.6f}, \n".format(xCoord[i], yCoord[i], zCoord[i]))
        i += 1
    output.write("\t\t]\n\t}\n")

    #normals
    if shade == "smooth":
        output.write("\tNormalBinding {\n\t\tvalue PER_VERTEX_INDEXED\n\t}\n\n")
        output.write("\tNormal {\n\t\tvector [\n")
        i = 0
        for i in range(0, len(normals), 3):
            output.write("\t\t\t{:.6f} {:.6f} {:.6f}, \n".format(normals[i], normals[i+1], normals[i+2]))
        output.write("\t\t]\n\t}\n")
    
    #faceting
    output.write("\tIndexedFaceSet {\n\t\tcoordIndex [\n")
    i = 0
    j = 0
    for i in range(0, len(vertex), 4):
        output.write("\t\t\t{}, {}, {}, {},\n".format(vertex[i], vertex[i+1], vertex[i+2], vertex[i+3]))
    output.write("\t\t\t]\n\t\t}\n\t}\n")

    return

def print_to_terminal():
    f = open("out.iv", "r")
    print(f.read())

if __name__ == "__main__":
    userData = []

    r = .1
    inputfile = "rev_surf_in0.txt"
    r = float(r)
    num_u = 12
    num_t = 22
    shade = "flat"
    tu = 0
    tt = 0
    t = 0
    cap = "no cap"
    two_pi = 2 * math.pi

    twoD_array = []
    vertex = []
    normals = []

    x_tangent = []
    y_tangent = []
    z_tangent = []

    xPoint = []
    yPoint = []
    zPoint = []

    xCoord = []
    yCoord = []
    zCoord = []


    command_line()
    read_file(userData)
    length = len(userData)
    num_points = int(length/3)
    set_point_arrays(num_points, xPoint, yPoint, zPoint, x_tangent, y_tangent, z_tangent)
    du = float(1/(num_u - 1))
    dt = float(1/(num_t - 1))
 
    get_tangents(len(xPoint))
    faceting(twoD_array, vertex)

    write_out() 
    print_to_terminal()
