import numpy
from data_in import *
from polygons import *
from data_out import *
from matrix import *
from calculations import *



if __name__ == "__main__":
    radius = .02
    theta1 = float(-51)
    theta2 = float(39)
    theta3 = float(65)
    L1 = float(4)
    L2 = float(3)
    L3 = float(2.5)

    theta1, theta2, theta3, L1, L2, L3 = command_line(theta1, theta2, theta3, L1, L2, L3)

    P0 = Polygon(0, [-2, -2, 0], [2, 2, 1])
    P1 = Polygon(L1, [-.5, -.5, 0], [.5, .5, L1])
    P2 = Polygon(L2, [-.5, -.5, 0], [.5, .5, L2])
    P3 = Polygon(L3, [-.5, -.5, 0], [.5, .5, L3])

    P0.draw_starting_polygon(P0.start1, P0.start2)
    P1.draw_starting_polygon(P1.start1, P1.start2)
    P2.draw_starting_polygon(P2.start1, P2.start2)
    P3.draw_starting_polygon(P3.start1, P3.start2)

    P1_prime, P2_prime, P3_prime, end_point = computation(P0, P1, P2, P3, theta1, theta2, theta3)

    write_out(P0, P1_prime, P2_prime, P3_prime, end_point)
    print_to_terminal()
