import math
import sys

class node:
    def __init__(self, data = None):
        self.data = data
        self.next_node = None

class linkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        position = self.head
        while position.next_node != None:
            position = position.next_node
        position.next_node = new_node 

    def length(self):
        position = self.head
        i = 0
        while position.next_node != None:
            i += 1
            position = position.next_node
        return i

    def display(self):
        elements = []
        current_position = self.head
        while current_position.next_node != None:
            current_position = current_position.next_node
            elements.append(current_position.data)
        print(elements)


    def get_node(self, i):
        if i >= self.length():
            return None
        current_i = 0
        current_node = self.head
        while True:
            current_node = current_node.next_node
            if current_i == i:
                return current_node.data
            current_i += 1

    def delete_node(self, i):
        if i >= self.length():
            return
        current_i = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next_node
            if current_i == i:
                last_node.next = current_node.next
                return
            current_i += 1

class polygon:
    def __init__(self, points = [], x_value = [], y_value = []):
        self.x_value = x_value
        self.y_value = y_value
        self.point = points

    def set_points(self, points, x_value, y_value):
        for i in range(len(x_value)):
            temp = []
            temp.append(x_value[i])
            temp.append(y_value[i])
            points.append(temp)

        return points


def read_file(ax, ay, bx, by):
    breakpoint = 0
    f = open(inputfile, "r")
    lines = f.readlines()
    for line in lines:
        temp = line.split(" ")
        if len(temp) == 1:
            if temp[0] == "stroke\n":
                breakpoint += 1
            continue
        if breakpoint == 0:
            ax.append(int(temp[0]))
            ay.append(int(temp[1]))
        if breakpoint == 1:
            bx.append(int(temp[0]))
            by.append(int(temp[1]))

    return ax, ay, bx, by

def command_line():
    global inputfile
    num_elements = len(sys.argv[:])
    
    for i in range(num_elements):
        if sys.argv[i] == "-f":
            inputfile = str(sys.argv[i+1])

    return


def join(polygonA, polygonB):
    t_value = []
    output = []
    Polygon0 = []
    Polygon1 = []
    tempPolygon = []
    temp_node = None

    for j in range(polygonA.length() - 1):
        Polygon0.append(polygonA.get_node(j))
        if j+1 >= polygonA.length() - 1:
            Polygon0.append(polygonA.get_node(0))
    for j in range(polygonB.length() - 1):
        Polygon1.append(polygonB.get_node(j))
    if j+1 >= polygonB.length() - 1:
        Polygon1.append(polygonB.get_node(0))

    node = 0
    while(1):
        if(find_outside(polygonA, polygonB, node) == True):
            break
        else:
            node += 1
    
    output.append(polygonA.get_node(node)) 

    #make node the index of polygonA you start at    
    while(len(output) < 2 or output[0] != output[-1]):
        if node >= len(Polygon0) - 1:
            node = 0
        if temp_node != None:
            node = temp_node
            temp_node = None
        edge0 = []
        edge2_p1 = []
        intersecting_edges = []
        intersection_point = []
        edge0.append(Polygon0[node])
        edge0.append(Polygon0[node+1])

        for index in range(len(Polygon1) - 1):
            edge2 = []
            edge2.append(Polygon1[index])
            if index > len(Polygon1):
                edge2.append(Polygon1[0])
            else:
                edge2.append(Polygon1[index+1])
            intersect, t_value = intersection(edge0, edge2, t_value)
            if intersect == True:
                edge2_p1.append(edge2[1])



        if len(edge2_p1) == 0:
            output.append(Polygon0[node+1])
        else:
            t = min(t_value) 
            
            ptx = float((1-t) * int(edge0[0][0]) + t * int(edge0[1][0]))
            pty = float((1-t) * int(edge0[0][1]) + t * int(edge0[1][1]))
            intersection_point.append(int(ptx))
            intersection_point.append(int(pty))
            output.append(intersection_point)
            if min(t_value) == t_value[0]:
                temp = edge2_p1[0]
                output.append(temp)
            else:
                temp = edge2_p1[1]
                output.append(temp)

            tempPolygon = Polygon1
            Polygon1 = Polygon0
            Polygon0 = tempPolygon

            temp = output[-1]
            temp_node = Polygon0.index(temp)
            t_value = []
        node += 1
            

    return output




def find_outside(polygonA, polygonB, node):
    num_intersections = 0
    num_points = polygonB.length()
    p = polygonA.get_node(node)
    p_prime = [10000, p[1]]
    edge0 = []
    edge0.append(p)
    edge0.append(p_prime)
    t_value = []
    intersect = False
    

    i = 0
    j = 0

    for i in range(num_points-1):
        edge2 = []
        edge2.append(polygonB.get_node(i))
        if i+1 >= num_points:
            edge2.append(polygonB.get_node(0))
        else:
            edge2.append(polygonB.get_node(i+1))
        intersect, t_value = intersection(edge0, edge2, t_value)
        if intersect == True:
            num_intersections += 1
        j += 1      
    if num_intersections % 2 == 0 or num_intersections == 0:
        outside = True
    else:
        outside = False

    return outside


   
def intersection(edge0, edge2, t_value): 

    x11 = int(edge0[0][0])
    x12 = int(edge0[1][0])
    x21 = int(edge2[0][0])
    x22 = int(edge2[1][0])

    y11 = int(edge0[0][1])
    y12 = int(edge0[1][1])
    y21 = int(edge2[0][1])
    y22 = int(edge2[1][1])

    dx1 = x12 - x11
    dx2 = x22 - x21
    dy1 = y12 - y11
    dy2 = y22 - y21
    
    denominator0 = float((dy1 * dx2 - dx1 * dy2))
    denominator2 = float((dy2 * dx1 - dx2 * dy1))
    
    epsilon = .00000000000000000000001
    if 0 <= denominator0 <= epsilon or 0 <= denominator2 <= epsilon:
        intersection = False
        return intersection, t_value
    else:

        t0 = float(((x11 - x21) * dy2 + (y21 - y11) * dx2)/denominator0)        
        t2 = float(((x21 - x11) * dy1 + (y11 - y21) * dx1)/denominator2)

    if 0 < t0 < 1 and 0 < t2 < 1:
        intersection = True
        t_value.append(t0)
    else:
        intersection = False

    
    return intersection, t_value


def write_out(output):
    f = open("out.ps", "w")
    f.write("%!PS-Adobe-2.0\n")
    f.write("%%%BEGIN\n")
    for i in range(len(output)):
        if i == 0:
            f.write("{} {} moveto\n".format(output[i][0], output[i][1]))
        else:
            f.write("{} {} lineto\n".format(output[i][0], output[i][1]))
    f.write("stroke\n")
    f.write("%%%END\n")
    return


def print_to_terminal():
    f = open("out.ps", "r")
    print(f.read())
    return


if __name__ == "__main__":
    inputfile = "HW3_a_in.ps"
    ax = []
    ay = []
    bx = []
    by = []

    pointsA = []
    pointsB = []
   
    command_line()
    read_file(ax, ay, bx, by)


    proto_polygonA = polygon(pointsA, ax, ay)
    proto_polygonA.set_points(pointsA, ax, ay)
    proto_polygonB = polygon(bx, by)
    proto_polygonB.set_points(pointsB, bx, by)


    polygonA = linkedList()
    polygonB = linkedList()

    for i in range(len(pointsA)):
        polygonA.append(pointsA[i])
    for i in range(len(pointsB)):
        polygonB.append(pointsB[i])

    output = join(polygonA, polygonB)

    write_out(output)
    print_to_terminal()
