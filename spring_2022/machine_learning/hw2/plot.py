from matplotlib import pyplot as plt

class Plot:
    def __init__(self):
        pass

    def plotMean(self, log, epoch):
        plt.xlabel("Epoch")
        plt.ylabel("Mean Log Loss")
        plt.plot(epoch, log.meanTrain, label = "Training", color = "blue")
        plt.plot(epoch, log.meanValid, label = "Validation", color = "orange")
        plt.title(label = "Mean Log Loss Vs. Epoch")
        plt.legend()
        plt.show()
    
    def plotPrecisionVSRecall(self, eval):
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.plot(eval.recall_PR, eval.prec_PR, color = "blue")
        plt.title(label = "Precision-Recall Chart")
        plt.xticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        plt.legend()
        plt.show()