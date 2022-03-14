import sys

def command_line(theta1, theta2, theta3, L1, L2, L3):
    num_elements = len(sys.argv[:])
    for i in range(num_elements):
        if sys.argv[i] == "-t":
            theta1 = float(sys.argv[i+1])
        if sys.argv[i] == "-u":
            theta2 = float(sys.argv[i+1])
        if sys.argv[i] == "-v":
            theta3 = float(sys.argv[i+1])
        if sys.argv[i] == "-l":
            L1 = float(sys.argv[i+1])
        if sys.argv[i] == "-m":
            L2 = float(sys.argv[i+1])
        if sys.argv[i] == "-n":
            L3 = float(sys.argv[i+1])

    return theta1, theta2, theta3, L1, L2, L3
