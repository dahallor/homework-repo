import sys 

def read_file(userData, inputfile):
    f = open(inputfile, "r")
    lines = f.readlines()
    for line in lines:
        temp = line.split(" ")
        userData.append(float(temp[0]))
        userData.append(float(temp[1]))
        stripped = temp[2]
        stripped = stripped.strip("\n")
        userData.append(float(stripped))
    return userData

def command_line(num_u, num_v, r, inputfile, shade):
    num_elements = len(sys.argv[:])
    i = 0
    for i in range(num_elements):
        if sys.argv[i] == "-u":
            num_u = int(sys.argv[i+1])
        if sys.argv[i] == "-v":
            num_v = int(sys.argv[i+1])
        if sys.argv[i] == "-r":
            r = float(sys.argv[i+1])
        if sys.argv[i] == "-f":
            inputfile = str(sys.argv[i+1])
        if sys.argv[i] == "-F":
            shade = "flat"
        if sys.argv[i] == "-S":
            shade = "smooth"
    
    return num_u, num_v, r, inputfile, shade
