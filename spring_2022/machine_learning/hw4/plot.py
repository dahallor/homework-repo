from matplotlib import pyplot as plt
import numpy as np
import pdb

class Plot:
    def plotP1(self, c1_X, c1_Y, c2_X, c2_Y):
        #pdb.set_trace()
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.scatter(c1_X, c1_Y, marker = "s", color = "blue", label = "Class 1")
        plt.scatter(c2_X, c2_Y, marker = "o", color = "orange", label = "Class 2")
        plt.legend()
        plt.show()

    def plotPCA(self, PC1, PC2):
        plt.xlabel("PC-1")
        plt.ylabel("PC-2")
        plt.scatter(PC1, PC2)
        plt.show()

    def plotPCA_P4_TopValue(self, PC):
        Y = np.zeros((len(PC), 1))
        plt.xlabel("PC")
        plt.scatter(PC, Y)
        plt.show()

    def plotPCA_Whiten(self, PC1, PC2):
        plt.xlabel("PC-1")
        plt.ylabel("PC-2")
        plt.scatter(PC1, PC2)
        plt.show()

    def plotP1_1D(self, PC1, PC2):
        PC1_c1 = PC1[:5]
        PC1_c2 = PC1[5:]
        PC2_c1 = PC2[:5]
        PC2_c2 = PC2[5:]
        Y = np.zeros((5, 1))

        plt.xlabel("X")
        plt.ylim(-.00000001, 0.00000001)
        plt.scatter(PC1_c1, Y, marker = "s", color = "blue", label = "Class 1, PC1")
        plt.scatter(PC2_c1, Y, marker = "s", color = "orange", label = "Class 1, PC2")
        plt.scatter(PC1_c2, Y, marker = "o", color = "blue", label = "Class 2, PC1")
        plt.scatter(PC2_c2, Y, marker = "o", color = "orange", label = "Class 2, PC2")
        plt.legend()
        plt.show()

    def plotP1_LDA(self, X):
        LDA_1 = X[:5]
        LDA_2 = X[5:]
        Y = np.zeros((5, 1))

        plt.xlabel("X")
        plt.ylim(-.00000001, 0.00000001)
        plt.scatter(LDA_1, Y, marker = "s", color = "blue", label = "Class 1, PC1")
        plt.scatter(LDA_2, Y, marker = "o", color = "orange", label = "Class 2, PC2")
        plt.legend()
        plt.show()

    def displayImage(self, img_arr):
        plt.imshow(img_arr, cmap = "gray")
        plt.show()