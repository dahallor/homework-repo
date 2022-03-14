import math


def interpolate(u, v, point_set, xCoord, yCoord, zCoord):
    n = 3
    totalx = 0
    totaly = 0
    totalz = 0

    for i in range(n+1):
        coef_v = math.factorial(n)/(math.factorial(i) * math.factorial(n-i))

        for j in range(n+1):
            coef_u = math.factorial(n)/(math.factorial(j) * math.factorial(n-j))
   
            totalx += (coef_u * math.pow(u, j) * math.pow(1-u, n-j)) * (coef_v * math.pow(v, i) * math.pow(1-v, n-i)) *  point_set[i][j][0]
            totaly += (coef_u * math.pow(u, j) * math.pow(1-u, n-j)) * (coef_v * math.pow(v, i) * math.pow(1-v, n-i)) * point_set[i][j][1]
            totalz += (coef_u * math.pow(u, j) * math.pow(1-u, n-j)) * (coef_v * math.pow(v, i) * math.pow(1-v, n-i)) * point_set[i][j][2]
   

    xCoord.append(totalx)
    yCoord.append(totaly)
    zCoord.append(totalz)

    return xCoord, yCoord, zCoord

def faceting(twoD_array, vertex, num_u, num_v):
    point = []
    k = 0
    for i in range(num_v):
        for j in range(num_u): 
            point.append(k)
            k += 1
        twoD_array.append(point)
        point = []
 

    for i in range(num_v-1):
        for j in range(num_u-1):
            vertex.append(twoD_array[i][j])
            vertex.append(twoD_array[i+1][j])
            vertex.append(twoD_array[i+1][j+1])
            vertex.append(-1)
            vertex.append(twoD_array[i][j])
            vertex.append(twoD_array[i+1][j+1])
            vertex.append(twoD_array[i][j+1])
            vertex.append(-1)
                 
    return twoD_array, vertex

def shading(u, v, point_set, normals):
    n = 3
    du_x = 0
    du_y = 0
    du_z = 0
    dv_x = 0
    dv_y = 0
    dv_z = 0


    bu0 = math.pow(1-u, 3)
    bu1 = 3 * u * math.pow(1-u, 2)
    bu2 = 3 * math.pow(u, 2) * (1-u)
    bu3 = math.pow(u,3)

    bv0 = math.pow(1-v,3)
    bv1 = 3 * v * math.pow(1-v, 2)
    bv2 = 3 * math.pow(v, 2) * (1-v)
    bv3 = math.pow(v, 3)

    du0 = -3 * math.pow(1-u, 2)
    du1 = 3 * (3 * math.pow(u, 2) - 4 * u + 1)
    du2 = 3 * (2 * u - 3 * math.pow(u,2))
    du3 = 3 * math.pow(u, 2)

    dv0 = -3 * math.pow(1-v, 2)
    dv1 = 3 * (3 * math.pow(v, 2) - 4 * v + 1)
    dv2 = 3 * (2 * v - 3 * math.pow(v, 2))
    dv3 = 3 * math.pow(v, 2)


    k = 0
    #derivative of u
    for i in range(n+1):
        for j in range(n+1):
            if k == 0:
                du_x += du0 * bv0 * point_set[i][j][0]
                du_y += du0 * bv0 * point_set[i][j][1]
                du_z += du0 * bv0 * point_set[i][j][2]
            if k == 1:
                du_x += du0 * bv1 * point_set[i][j][0]
                du_y += du0 * bv1 * point_set[i][j][1]
                du_z += du0 * bv1 * point_set[i][j][2]
            if k == 2:
                du_x += du0 * bv2 * point_set[i][j][0]
                du_y += du0 * bv2 * point_set[i][j][1]
                du_z += du0 * bv2 * point_set[i][j][2]
            if k == 3:
                du_x += du0 * bv3 * point_set[i][j][0]
                du_y += du0 * bv3 * point_set[i][j][1]
                du_z += du0 * bv3 * point_set[i][j][2]
            if k == 4:
                du_x += du1 * bv0 * point_set[i][j][0]
                du_y += du1 * bv0 * point_set[i][j][1]
                du_z += du1 * bv0 * point_set[i][j][2]
            if k == 5:
                du_x += du1 * bv1 * point_set[i][j][0]
                du_y += du1 * bv1 * point_set[i][j][1]
                du_z += du1 * bv1 * point_set[i][j][2]
            if k == 6:
                du_x += du1 * bv2 * point_set[i][j][0]
                du_y += du1 * bv2 * point_set[i][j][1]
                du_z += du1 * bv2 * point_set[i][j][2]
            if k == 7:
                du_x += du1 * bv3 * point_set[i][j][0]
                du_y += du1 * bv3 * point_set[i][j][1]
                du_z += du1 * bv3 * point_set[i][j][2]
            if k == 8:
                du_x += du2 * bv0 * point_set[i][j][0]
                du_y += du2 * bv0 * point_set[i][j][1]
                du_z += du2 * bv0 * point_set[i][j][2]
            if k == 9:
                du_x += du2 * bv1 * point_set[i][j][0]
                du_y += du2 * bv1 * point_set[i][j][1]
                du_z += du2 * bv1 * point_set[i][j][2]
            if k == 10:
                du_x += du2 * bv2 * point_set[i][j][0]
                du_y += du2 * bv2 * point_set[i][j][1]
                du_z += du2 * bv2 * point_set[i][j][2]
            if k == 11:
                du_x += du2 * bv3 * point_set[i][j][0]
                du_y += du2 * bv3 * point_set[i][j][1]
                du_z += du2 * bv3 * point_set[i][j][2]
            if k == 12:
                du_x += du3 * bv0 * point_set[i][j][0]
                du_y += du3 * bv0 * point_set[i][j][1]
                du_z += du3 * bv0 * point_set[i][j][2]
            if k == 13:
                du_x += du3 * bv1 * point_set[i][j][0]
                du_y += du3 * bv1 * point_set[i][j][1]
                du_z += du3 * bv1 * point_set[i][j][2]
            if k == 14:
                du_x += du3 * bv2 * point_set[i][j][0]
                du_y += du3 * bv2 * point_set[i][j][1]
                du_z += du3 * bv2 * point_set[i][j][2]
            if k == 15:
                du_x += du3 * bv3 * point_set[i][j][0]
                du_y += du3 * bv3 * point_set[i][j][1]
                du_z += du3 * bv3 * point_set[i][j][2]

            k += 1
            
    k = 0
    #derivative of v 
    for i in range(n+1):
        for j in range(n+1):
            if k == 0:
                dv_x += bu0 * dv0 * point_set[i][j][0]
                dv_y += bu0 * dv0 * point_set[i][j][1]
                dv_z += bu0 * dv0 * point_set[i][j][2]
            if k == 1:
                dv_x += bu0 * dv1 * point_set[i][j][0]
                dv_y += bu0 * dv1 * point_set[i][j][1]
                dv_z += bu0 * dv1 * point_set[i][j][2]
            if k == 2:
                dv_x += bu0 * dv2 * point_set[i][j][0]
                dv_y += bu0 * dv2 * point_set[i][j][1]
                dv_z += bu0 * dv2 * point_set[i][j][2]
            if k == 3:
                dv_x += bu0 * dv3 * point_set[i][j][0]
                dv_y += bu0 * dv3 * point_set[i][j][1]
                dv_z += bu0 * dv3 * point_set[i][j][2]
            if k == 4:
                dv_x += bu1 * dv0 * point_set[i][j][0]
                dv_y += bu1 * dv0 * point_set[i][j][1]
                dv_z += bu1 * dv0 * point_set[i][j][2]
            if k == 5:
                dv_x += bu1 * dv1 * point_set[i][j][0]
                dv_y += bu1 * dv1 * point_set[i][j][1]
                dv_z += bu1 * dv1 * point_set[i][j][2]
            if k == 6:
                dv_x += bu1 * dv2 * point_set[i][j][0]
                dv_y += bu1 * dv2 * point_set[i][j][1]
                dv_z += bu1 * dv2 * point_set[i][j][2]
            if k == 7:
                dv_x += bu1 * dv3 * point_set[i][j][0]
                dv_y += bu1 * dv3 * point_set[i][j][1]
                dv_z += bu1 * dv3 * point_set[i][j][2]
            if k == 8:
                dv_x += bu2 * dv0 * point_set[i][j][0]
                dv_y += bu2 * dv0 * point_set[i][j][1]
                dv_z += bu2 * dv0 * point_set[i][j][2]
            if k == 9:
                dv_x += bu2 * dv1 * point_set[i][j][0]
                dv_y += bu2 * dv1 * point_set[i][j][1]
                dv_z += bu2 * dv1 * point_set[i][j][2]
            if k == 10:
                dv_x += bu2 * dv2 * point_set[i][j][0]
                dv_y += bu2 * dv2 * point_set[i][j][1]
                dv_z += bu2 * dv2 * point_set[i][j][2]
            if k == 11:
                dv_x += bu2 * dv3 * point_set[i][j][0]
                dv_y += bu2 * dv3 * point_set[i][j][1]
                dv_z += bu2 * dv3 * point_set[i][j][2]
            if k == 12:
                dv_x += bu3 * dv0 * point_set[i][j][0]
                dv_y += bu3 * dv0 * point_set[i][j][1]
                dv_z += bu3 * dv0 * point_set[i][j][2]
            if k == 13:
                dv_x += bu3 * dv1 * point_set[i][j][0]
                dv_y += bu3 * dv1 * point_set[i][j][1]
                dv_z += bu3 * dv1 * point_set[i][j][2]
            if k == 14:
                dv_x += bu3 * dv2 * point_set[i][j][0]
                dv_y += bu3 * dv2 * point_set[i][j][1]
                dv_z += bu3 * dv2 * point_set[i][j][2]
            if k == 15:
                dv_x += bu3 * dv3 * point_set[i][j][0]
                dv_y += bu3 * dv3 * point_set[i][j][1]
                dv_z += bu3 * dv3 * point_set[i][j][2]
            k += 1

    nx = du_y * dv_z - dv_y * du_z
    ny = du_z * dv_x - dv_z * du_x
    nz = du_x * dv_y - dv_x * du_y
    normals.append(nx)
    normals.append(ny)
    normals.append(nz)


            
    return normals
