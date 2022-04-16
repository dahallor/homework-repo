from matplotlib import pyplot as plt

class Plot:
    def __init__(self):
        pass

    def plotMean(self, log, epoch):
        plt.xlabel("Epoch")
        plt.ylabel("Mean Log Loss")
        plt.plot(epoch, log.meanTrain, label = "Training", color = "blue")
        plt.plot(epoch, log.meanValid, label = "Validation", color = "orange")
        plt.legend()
        plt.show()