import numpy

class Polygon:
    def __init__(self, L_value = 0, start1 = [], start2 = [], coordinates = []):
        self.L_value = L_value
        self.start1 = start1
        self.start2 = start2
        self.coordinates = coordinates


    def draw_starting_polygon(self, start1, start2):
        coords = []

        temp = []
        temp.append(start1[0])
        temp.append(start1[1])
        temp.append(start1[2])
        coords.append(temp)

        temp = []
        temp.append(start1[0])
        temp.append(-1 * start1[1])
        temp.append(start1[2])
        coords.append(temp)

        temp = []
        temp.append(-1 * start1[0])
        temp.append(-1 * start1[1])
        temp.append(start1[2])
        coords.append(temp)

        temp = []
        temp.append(-1 * start1[0])
        temp.append(start1[1])
        temp.append(start1[2])
        coords.append(temp)

        temp = []
        temp.append(-1 * start2[0])
        temp.append(-1 * start2[1])
        temp.append(start2[2])
        coords.append(temp)

        temp = []
        temp.append(-1 * start2[0])
        temp.append(start2[1])
        temp.append(start2[2])
        coords.append(temp)

        temp = []
        temp.append(start2[0])
        temp.append(start2[1])
        temp.append(start2[2])
        coords.append(temp)

        temp = []
        temp.append(start2[0])
        temp.append(-1 *start2[1])
        temp.append(start2[2])
        coords.append(temp)
        
        self.coordinates = coords

    def add_coordinate(self, array):
        self.coordinates.append(array)
