from prep import *
from input import *
import pdb
import sys

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()

    prep_data_p2(IL)

    pdb.set_trace()