from prep import *
from input import *
from tree import *
import pdb
import sys

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()
    tree = Tree()

    prep_data_p3(IL)
    tree.setHash(IL)
    tree.fillHashData(IL, "binary")
    #print(tree.featureHash)