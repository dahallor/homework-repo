def write_out(points_array, normals, shade, vertex):
    output = open("out.iv", "w")
    output.write("#Inventor V2.0 ascii\n\n")
    output.write("ShapeHints {\n\tvertexOrdering\tCOUNTERCLOCKWISE\n}\n")
    
    output.write("Separator {\n\tCoordinate3 {\n\t\tpoint [\n")
    for i in range(len(points_array)):
        output.write("\t\t\t{:.6f} {:.6f} {:.6f},\n".format(points_array[i][0], points_array[i][1], points_array[i][2]))
    output.write("\t\t]\n\t}\n")

    output.write("NormalBinding {\n\tvalue\tPER_VERTEX_INDEXED\n}\n")
    if shade == "smooth":
        output.write("\tNormal {\n\t\tvector [\n") 
        for i in range(len(normals)):
            output.write("\t\t\t{:.6f} {:.6f} {:.6f},\n".format(normals[i][0], normals[i][1], normals[i][2]))
        output.write("\t\t]\n\t}\n")

    output.write("\tIndexedFaceSet {\n\t\tcoordIndex [\n")
    for i in range(0, len(vertex), 4):
        output.write("\t\t\t{}, {}, {}, {},\n".format(vertex[i], vertex[i+1], vertex[i+2], vertex[i+3]))
    output.write("\t\t\t]\n\t\t}\n}")


def print_to_terminal():
    f = open("out.iv", "r")
    print(f.read())
