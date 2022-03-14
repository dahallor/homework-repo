import sys


def command_line(Aval, Bval, Cval, s1_val, s2_val, u_num, v_num, shade):

    num_elements = len(sys.argv[:])
    for i in range(num_elements):
        if sys.argv[i] == "-r":
            s1_val = float(sys.argv[i+1])
        if sys.argv[i] == "-t":
            s2_val = float(sys.argv[i+1])
        if sys.argv[i] == "-A":
            Aval = float(sys.argv[i+1])
        if sys.argv[i] == "-B":
            Bval = float(sys.argv[i+1])
        if sys.argv[i] == "-C":
            Cval = float(sys.argv[i+1])
        if sys.argv[i] == "-u":
            u_num = int(sys.argv[i+1])
        if sys.argv[i] == "-v":
            v_num = int(sys.argv[i+1])
        if sys.argv[i] == "-F":
            shade = "flat"
        if sys.argv[i] == "-S":
            shade = "smooth"
    return Aval, Bval, Cval, s1_val, s2_val, u_num, v_num, shade
