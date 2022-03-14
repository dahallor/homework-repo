def write_out(P0, P1, P2, P3, end_point):
    f = open("out.iv", "w")
    f.write("#Inventor V2.0 ascii\n\n")

    index_line_set = """    IndexedLineSet {
            coordIndex [
                0, 1, 2, 0, -1,
                0, 2, 3, 0, -1,
                7, 6, 5, 7, -1,
                7, 5, 4, 7, -1,
                0, 3, 7, 0, -1,
                0, 7, 4, 0, -1,
                1, 5, 6, 1, -1,
                1, 6, 2, 1, -1,
                0, 4, 5, 0, -1,
                0, 5, 1, 0, -1,
                3, 2, 6, 3, -1,
                3, 6, 7, 3, -1
        ]
    }
}\n"""

    prefix ="""Separator {
    Coordinate3 {
        point [\n"""

    close_prefix ="""
        ]
    }\n"""

    endpoint_1 ="""Separator {
LightModel {
model PHONG
}
Material {
    diffuseColor 1.0 1.0 1.0
}\n"""

    endpoint_2 ="""Sphere {
    radius 0.20
}
}\n"""

    f.write(prefix)
    for i in range(8):
        f.write("\t\t\t{:.6f} {:.6f} {:.6f},\n".format(P0.coordinates[i][0], P0.coordinates[i][1], P0.coordinates[i][2]))
    f.write(close_prefix)
    f.write(index_line_set)


    f.write(prefix)
    for i in range(8):
        x = P1[i][0]
        x = float(x)
        y = P1[i][1]
        y = float(y)
        z = P1[i][2]
        z = float(z)

        f.write("\t\t\t{:.6f} {:.6f} {:.6f},\n".format(x, y, z))
    f.write(close_prefix)
    f.write(index_line_set)


    f.write(prefix)
    for i in range(8):
        x = P2[i][0]
        x = float(x)
        y = P2[i][1]
        y = float(y)
        z = P2[i][2]
        z = float(z)

        f.write("\t\t\t{:.6f} {:.6f} {:.6f},\n".format(x, y, z))
    f.write(close_prefix)
    f.write(index_line_set)


    f.write(prefix)
    for i in range(8):
        x = P3[i][0]
        x = float(x)
        y = P3[i][1]
        y = float(y)
        z = P3[i][2]
        z = float(z)

        f.write("\t\t\t{:.6f} {:.6f} {:.6f},\n".format(x, y, z))
    f.write(close_prefix)
    f.write(index_line_set)


    f.write(endpoint_1)
    f.write(endpoint_2)
    
    f.write(endpoint_1)
    end_x = float(end_point[0])
    end_y = float(end_point[1])
    end_z = float(end_point[2])
    f.write("Transform {}\n\ttranslation {:.6f} {:.6f} {:.6f}\n{}\n".format("{", end_x, end_y, end_z, "}"))
    f.write(endpoint_2)


def print_to_terminal():
    f = open("out.iv", "r")
    print(f.read())

