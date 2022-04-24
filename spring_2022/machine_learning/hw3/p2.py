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

    normals.setNormals(IL)

    #pdb.set_trace()