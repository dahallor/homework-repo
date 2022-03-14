from data_in import *
from out import *
from points import *
from calc_r_v2 import *


if __name__ == "__main__":
    userData = []

    r = .1
    inputfile = "patchPoints.txt"
    r = float(r)
    num_u = 11
    num_v = 11
    shade = "flat"

    twoD_array = []
    vertex = []

    points = []
    point_set = []
    normals = []

    xPoint = []
    yPoint = []
    zPoint = []

    xCoord = []
    yCoord = []
    zCoord = []

    P = Points()

    num_u, num_v, r, inputfile, shade = command_line(num_u, num_v, r, inputfile, shade)

    userData = read_file(userData, inputfile)
    length = len(userData)
    num_points = int(length/3)
    xPoint, yPoint, zPoint = P.set_point_arrays(num_points, xPoint, yPoint, zPoint, userData)
    
    for i in range(len(xPoint)):
        P.create_point(points, xPoint[i], yPoint[i], zPoint[i])
    
    temp = []
    for i in range(16):
        temp.append(points[i])
        if (i+1) % 4 == 0:
            point_set.append(temp)
            temp = []

    
    du = float(1/(num_u - 1))
    dv = float(1/(num_v - 1))
  
    v = 0
    for i in range(num_v):
        u = 0
        for j in range(num_u):
            xCoord, yCoord, zCoord = interpolate(u, v, point_set, xCoord, yCoord, zCoord)
            u += du
        v += dv

    twoD_array, vertex = faceting(twoD_array, vertex, num_u, num_v)
    
    tv = float(1/(num_u-1))
    tu = float(1/(num_v-1))
    if(shade == "smooth"):
        u = 0
        for i in range(num_v):
            v = 0
            for j in range(num_u):
                normals = shading(u, v, point_set, normals);
                v += tv
            u += tu

    write_out(xCoord, yCoord, zCoord, normals, vertex, xPoint, yPoint, zPoint, r, shade)
    print_to_terminal()
