
def write_out(xCoord, yCoord, zCoord, normals, vertex, xPoint, yPoint, zPoint, r, shade):
    #Header
    output = open("out.iv", "w")
    output.write("#Inventor V2.0 ascii\n\n")
    output.write("ShapeHints {\n\tvertexOrdering\tCOUNTERCLOCKWISE\n}\n")
    output.write("Separator {\n\tCoordinate3 {\n\t\tpoint [\n")
    
    #coordinaates
    i = 0
    for i in range(len(xCoord)):
        output.write("\t\t\t{:.6f} {:.6f} {:.6f},\n".format(xCoord[i], yCoord[i], zCoord[i]))
        i += 1
    output.write("\t\t]\n\t}\n")

    #normals
    if shade == "smooth":
        output.write("NormalBinding {\n\t value\tPER_VERTEX_INDEXED\n}\n")
        output.write("\tNormal {\n\t\tvector [\n")
        i = 0
        for i in range(0, len(normals), 3):
            output.write("\t\t\t{:.6f} {:.6f} {:.6f},\n".format(normals[i], normals[i+1], normals[i+2]))

        output.write("\t\t]\n\t}\n")
    
    #faceting
    output.write("\tIndexedFaceSet {\n\t\tcoordIndex [\n")
    i = 0
    j = 0
    for i in range(0, len(vertex), 4):
        output.write("\t\t\t{}, {}, {}, {},\n".format(vertex[i], vertex[i+1], vertex[i+2], vertex[i+3]))

    output.write("\t\t\t]\n\t\t}\n\t}\n")

    #control points
    i = 0
    for i in range(len(xPoint)):
        output.write("Separator {\nLightModel {\nmodel PHONG\n}\n")
        output.write("Material {\n\tdiffuseColor 1.0 1.0 1.0\n}\n")
        output.write("Transform {}\n\ttranslation {:.1f} {:.1f} {:.1f}\n{}\n".format("{", xPoint[i], yPoint[i], zPoint[i], "}"))
        output.write("Sphere {}\n\tradius {:.2f}\n{}\n{}\n".format("{", r, "}", "}"))
        i += 1
   
    return

def print_to_terminal():
    f = open("out.iv", "r")
    print(f.read())
