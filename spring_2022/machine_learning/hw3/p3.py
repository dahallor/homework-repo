from prep import *
from input import *
from treev2 import *
import pdb
import sys

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()
    prep_data_p3(IL)
    tree_train = Tree(IL.trainX)
    tree_valid = Tree(IL.validX)

    tree_train.convertFeaturesToBinary(IL, IL.trainX)
    tree_train.setInitialExamples(IL)
    tree_train.setAttributes(IL.trainX)
    tree_train.DTL(tree_train.examples, tree_train.attributes, 0, 2, "binary")
    #pdb.set_trace()

    '''
    tree_train.setAttribute(IL)
    tree_train.fillHashData(IL, "binary")
    #tree_train.getEntropy(tree_train.attributes, tree_train.examples, 2)
    pdb.set_trace()
    
    tree_train.setHash(IL)
    tree_train.fillHashData(IL, "binary")
    tree_train.calcEntropy(2)
    print(tree_train.getRoot())
    pdb.set_trace()
    #print(tree_train.featureHash)
    '''