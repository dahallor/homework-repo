import sys
import numpy as np
from prep import *
from data_input import *


if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)
    IL = InputLayer()

    prepP2(IL) 