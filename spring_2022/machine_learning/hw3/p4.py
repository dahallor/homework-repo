from prep import *
from input import *
from normals import *
from stats import *
from bayes import *
import pdb
import sys

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()
    normals = Normals()
    stats = Stats()
    bayes = Bayes()

    prep_data_p4(IL)

    normals.setNormalModelsp2(IL.trainX0, IL.trainX1)
    bayes.runNaiveBayesP2(normals, stats, IL)
    stats.setAllStats()
    stats.printStats()
    
