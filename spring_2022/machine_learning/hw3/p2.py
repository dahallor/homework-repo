from prep import *
from input import *
from dist import *
import pdb
import sys

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()
    normals = Normals()

    prep_data_p2(IL)

    normals.setStatsp2(IL.trainX0, IL.trainX1)

    pdb.set_trace()