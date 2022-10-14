import numpy as np
import sys

def parse_CSV():
    return np.genfromtxt(fname="CS590-HW1.csv", dtype=str, delimiter=",", skip_header=1)

def convert_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'y':
                array[i][j] = 1
            else:
                array[i][j] = 0
    array = array.astype('int32')
    return array

def get_physician_fee(array):
    #physician fee freeze at column index 3
    return array[:, 3]

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    array = parse_CSV()
    array = convert_array(array)

    fee_col = get_physician_fee(array)
    print(sum(fee_col))

    