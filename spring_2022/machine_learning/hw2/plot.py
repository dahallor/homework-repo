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

    def plotMeanMulticlass(self, log, epoch):
        plt.xlabel("Epoch")
        plt.ylabel("Mean Log Loss")
        plt.plot(epoch, log.mean1v2, label = "1v2", color = "blue")
        plt.plot(epoch, log.mean1v3, label = "1v3", color = "red")
        plt.plot(epoch, log.mean2v3, label = "2v3", color = "green")
        plt.title(label = "Mean Log Loss Vs. Epoch")
        plt.legend()
        plt.show()
    
    def plotPrecisionVSRecall(self, eval):
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        plt.plot(eval.recall_PR_train, eval.prec_PR_train, label = "Training", color = "blue")
        plt.plot(eval.recall_PR_valid, eval.prec_PR_valid, label = "Validation", color = "orange")
        plt.title(label = "Precision-Recall Chart")
        plt.xticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        plt.legend()
        plt.show()