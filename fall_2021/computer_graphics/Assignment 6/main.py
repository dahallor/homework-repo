from system import *
from calculations import *
from classes import *
from output import *

if __name__ == "__main__":
    Aval = 1
    Bval = 1
    Cval = 1
    s1_val = 1
    s2_val = 1
    u_num = 18
    v_num = 9
    shade = "flat"

    points_array = []
    normals = []
    vertex = []
    twoD_array = []
    points = Points()

    Aval, Bval, Cval, s1_val, s2_val, u_num, v_num, shade = command_line(Aval, Bval, Cval, s1_val, s2_val, u_num, v_num, shade)

    draw_SE(points, points_array, Aval, Bval, Cval, s1_val, s2_val, u_num, v_num)
    if shade == "smooth":
        calc_normals(Aval, Bval, Cval, s1_val, s2_val, u_num, v_num, normals)
    faceting(twoD_array, vertex, v_num, u_num)


    write_out(points_array, normals, shade, vertex)
    print_to_terminal()
