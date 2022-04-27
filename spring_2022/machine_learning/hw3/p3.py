from prep import *
from input import *
from tree import *
import pdb
import sys

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()
    prep_data_p3(IL)
    tree_train = Tree(IL.trainX)
    tree_valid = Tree(IL.validX)

    tree_train.setHash(IL)
    tree_train.fillHashData(IL, "binary")
    tree_train.calcEntropy()
    print(tree_train.getRoot())
    #print(tree_train.featureHash)