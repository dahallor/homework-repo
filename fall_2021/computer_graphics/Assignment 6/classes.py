class Points():
    def set_points(self, points_array, x, y, z):
        point = []
        point.append(x)
        point.append(y)
        point.append(z)
        points_array.append(point)

        return points_array
