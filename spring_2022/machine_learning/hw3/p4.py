from prep import *
from input import *
from normals import *
from stats import *
from bayes import *
from treev2 import *
import pdb
import sys

def _runBayes():
    IL = InputLayer()
    normals = Normals()
    stats = Stats()
    bayes = Bayes()

    prep_data_p4(IL)
    normals.setNormalModelsP4(IL.trainX1, IL.trainX2, IL.trainX3)
    bayes.runNaiveBayesP4(normals, stats, IL)
    stats.setAccuracyMulticlass()
    stats.printAccuracy()

def _runDT():
    IL = InputLayer()
    prep_data_p4(IL)
    tree_train = Tree(IL.trainX)

    tree_train.convertFeaturesToBinary(IL, IL.trainX)
    tree_train.setInitialExamples(IL)
    tree_train.setAttributes(IL.trainX)
    tree_train.DTL(tree_train.examples, tree_train.attributes, 0, 3, "multiclass")
    tree_train.printTree()

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    _runBayes()
    #_runDT()



    
