from matplotlib import pyplot as plt
import pdb

class Plot:
    def plotP1(self, X1_1, X1_2, Y1, X2_1, X2_2, Y2):
        #pdb.set_trace()
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.scatter(X1_1, Y1, marker = "s", color = "blue", label = "Class 1")
        plt.scatter(X1_2, Y1, marker = "s", color = "blue")
        plt.scatter(X2_1, Y2, marker = "o", color = "orange", label = "Class 2")
        plt.scatter(X2_2, Y2, marker = "o", color = "orange")
        plt.legend()
        plt.show()