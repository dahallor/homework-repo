import math
from classes import *

def initialize(u_num, v_num):
    para_v = abs((-1 * math.pi/2) - (math.pi/2))
    v = math.pi/2
    dv = para_v/(v_num-1)
    
    para_u = abs(-1 * math.pi - math.pi)
    u = math.pi
    du = para_u/(u_num-1)

    return u, v, du, dv



def draw_SE(points, points_array, Aval, Bval, Cval, s1_val, s2_val, u_num, v_num):
    u, v, du, dv = initialize(u_num, v_num)
    for i in range(v_num):
        if i == 0:
            x = 0
            y = 0
            z = Cval
            points.set_points(points_array, x, y, z)
            v -= dv
            continue
        if i == v_num-1:
            x = 0
            y = 0
            z = -1 * Cval
            points.set_points(points_array, x, y, z)
            break
        for j in range(u_num-1):
            #x value
            omega = v
            m = s1_val
            c1 = aux_function_c(omega, m)
            omega = u
            m = s2_val
            c2 = aux_function_c(omega, m)
            x = -1 * (Aval * c1 * c2)

            #y value
            omega = v
            m = s1_val
            c = aux_function_c(omega, m)
            omega = u
            m = s2_val
            s = aux_function_s(omega, m)
            y = Bval * c * s

            #z value
            omega = v
            m = s1_val
            s = aux_function_s(omega, m)
            z = Cval * s
            points.set_points(points_array, x, y, z)
            u -= du
        v -= dv
        u = math.pi

    return points_array

def aux_function_c(omega, m):
    parameter = math.cos(omega)
    epsilon = .0000000000001
    if parameter < 0:
        sign = -1
    elif 0 < parameter < epsilon:
        sign = 0
    else:
        sign = 1

    temp = abs(parameter)

    c = sign * (math.pow(temp, m))

    return c

def aux_function_s(omega, m):
    parameter = math.sin(omega)
    epsilon = .0000000000001
    if parameter < 0:
        sign = -1
    elif 0 < parameter < epsilon:
        sign = 0
    else:
        sign = 1

    temp = abs(parameter)
    s = sign * (math.pow(temp, m))

    return s
    
def calc_normals(Aval, Bval, Cval, s1_val, s2_val, u_num, v_num, normals):
    u, v, du, dv = initialize(u_num, v_num)

    for i in range(v_num):
        if i == 0:
            nx = 0
            ny = 0
            nz = 1
            norm_point = []
            norm_point.append(nx)
            norm_point.append(ny)
            norm_point.append(nz)
            normals.append(norm_point)
            v += dv
            continue
        if i == v_num-1:
            nx = 0
            ny = 0
            nz = -1
            norm_point = []
            norm_point.append(nx)
            norm_point.append(ny)
            norm_point.append(nz)
            normals.append(norm_point)
            break
        for j in range(u_num-1):
            #x value
            omega = v
            m = 2 - s1_val
            c1 = aux_function_c(omega, m)
            omega = u
            m = 2 - s2_val
            c2 = aux_function_c(omega, m)
            nx = (1/Aval) * c1 * c2

            #y value
            omega = v
            m = 2 - s1_val
            c = aux_function_c(omega, m)
            omega = u
            m = 2 - s2_val
            s = aux_function_s(omega, m)
            ny = (1/Bval) * c * s

            #z value
            omega = v
            m = 2 - s1_val
            s = aux_function_s(omega, m)
            nz = (1/Cval) * s

            norm_point = []
            norm_point.append(nx)
            norm_point.append(ny)
            norm_point.append(nz)
            normals.append(norm_point)
            u += du 
        v += dv
        u = -1 * math.pi


    return normals



def faceting(twoD_array, vertex, v_num, u_num):
    point = []
    k = 0
    count = 0


    for i in range(v_num-2):
        if count == 0 or count == v_num-3:
            for j in range(u_num): 
                point.append(k)
                k += 1
            count += 1
        else:
            for j in range(u_num-1):
                point.append(k)
                k += 1
            count += 1
        twoD_array.append(point)
        point = []

    
    k = 0
    count = 0
    
    for count in range(len(twoD_array)+1):
        if count == 0:
            m = 0
            for j in range(u_num-2):
                vertex.append(twoD_array[0][m+1])
                vertex.append(twoD_array[0][m+2])
                vertex.append(twoD_array[0][0])
                vertex.append(-1)
                m += 1
            vertex.append(twoD_array[0][-1])
            vertex.append(twoD_array[0][1])
            vertex.append(twoD_array[0][0])
            vertex.append(-1)
            k += 1
            continue
        elif count == 1:
            m = 0
            for j in range(u_num-2):
                vertex.append(twoD_array[-1][-1])
                vertex.append(twoD_array[-1][m+1])
                vertex.append(twoD_array[-1][m])
                vertex.append(-1)
                m += 1
            vertex.append(twoD_array[-1][-1])
            vertex.append(twoD_array[-1][0])
            vertex.append(twoD_array[-1][m])
            vertex.append(-1)
            continue
        
        elif k == 1:
            l = 0
            for i in range(len(twoD_array[k])):
                if l == len(twoD_array[k]) - 1:
                    vertex.append(twoD_array[k][l])
                    vertex.append(twoD_array[k][0])
                    vertex.append(twoD_array[k-1][1])
                    vertex.append(-1)
                    vertex.append(twoD_array[k][l])
                    vertex.append(twoD_array[k-1][1])
                    vertex.append(twoD_array[k-1][-1])
                    vertex.append(-1)
                    break
                vertex.append(twoD_array[k][l])
                vertex.append(twoD_array[k][l+1])
                vertex.append(twoD_array[k-1][l+2])
                vertex.append(-1)
                vertex.append(twoD_array[k][l])
                vertex.append(twoD_array[k-1][l+2])
                vertex.append(twoD_array[k-1][l+1])
                vertex.append(-1)
                l += 1
            k += 1
        elif k == len(twoD_array) - 1:
            l = 0
            for i in range(len(twoD_array[k])):
                if l == len(twoD_array[k]) - 2:
                    vertex.append(twoD_array[k][l])
                    vertex.append(twoD_array[k][0])
                    vertex.append(twoD_array[k-1][0])
                    vertex.append(-1)
                    vertex.append(twoD_array[k][l])
                    vertex.append(twoD_array[k-1][0])
                    vertex.append(twoD_array[k-1][-1])
                    vertex.append(-1)
                    break
                vertex.append(twoD_array[k][l])
                vertex.append(twoD_array[k][l+1])
                vertex.append(twoD_array[k-1][l+1])
                vertex.append(-1)
                vertex.append(twoD_array[k][l])
                vertex.append(twoD_array[k-1][l+1])
                vertex.append(twoD_array[k-1][l])
                vertex.append(-1)
                l += 1
            k += 1           

        else:
            l = 0
            for i in range(len(twoD_array[k])):
                if l == len(twoD_array[k])-1:
                    vertex.append(twoD_array[k][l])
                    vertex.append(twoD_array[k][0])
                    vertex.append(twoD_array[k-1][0])
                    vertex.append(-1)
                    vertex.append(twoD_array[k][l])
                    vertex.append(twoD_array[k-1][0])
                    vertex.append(twoD_array[k-1][-1])
                    vertex.append(-1)
                    continue
                vertex.append(twoD_array[k][l])
                vertex.append(twoD_array[k][l+1])
                vertex.append(twoD_array[k-1][l+1])
                vertex.append(-1)
                vertex.append(twoD_array[k][l])
                vertex.append(twoD_array[k-1][l+1])
                vertex.append(twoD_array[k-1][l])
                vertex.append(-1)
                l += 1
            k += 1

    return twoD_array, vertex

  
