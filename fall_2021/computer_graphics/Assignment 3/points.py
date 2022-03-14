class Points:
    def create_point(self, points, x, y, z):
        temp = []
        temp.append(x)
        temp.append(y)
        temp.append(z)
        points.append(temp)

        return points
    
    def set_point_arrays(self, num_points, xPoint, yPoint, zPoint, userData):  
        i = 0
        k = 0
        #enters input into x, y, and z arrays
        for i in range(num_points):
            temp = userData[k] 
            xPoint.append(temp)
            temp = userData[k+1]
            yPoint.append(temp)
            temp = userData[k+2]
            zPoint.append(temp)
            k += 3
            i+=1
        return xPoint, yPoint, zPoint
