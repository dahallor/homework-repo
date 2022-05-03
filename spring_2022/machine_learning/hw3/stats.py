class Stats:
    def __init__(self):
        self.ratio = {
            "T+" : 0,
            "T-" : 0,
            "F+" : 0,
            "F-" : 0
        }
        self.ratioMulticlass = {
            "T" : 0,
            "F" : 0
        }
        self.accuracy = 0
        self.precision = 0
        self.recall = 0
        self.f = 0

    def setAllStats(self):
        self.setPrecision()
        self.setRecall()
        self.setF_Measure()
        self.setAccuracy()

    def printStats(self):
        print("Precision: {}\nRecall: {}\nF Measure: {}\nAccuracy: {}".format(self.precision, self.recall, self.f, self.accuracy))

    def printAccuracy(self):
        print("Accuracy: {}".format(self.accuracy))

    def addGuess(self, y, yhat):
        if int(y) == 1 and int(yhat) == 1:
            self.ratio["T+"] += 1
        if int(y) == 1 and int(yhat) == 0:
            self.ratio["F-"] += 1
        if int(y) == 0 and int(yhat) == 1:
            self.ratio["F+"] += 1
        if int(y) == 0 and int(yhat) == 0:
            self.ratio["T-"] += 1
        #pdb.set_trace()

    def addGuessMulticlass(self, y, yhat):
        if int(y) == 1 and int(yhat) == 1:
            self.ratioMulticlass["T"] += 1
        elif int(y) == 2 and int(yhat) == 2:
            self.ratioMulticlass["T"] += 1
        elif int(y) == 3 and int(yhat) == 3:
            self.ratioMulticlass["T"] += 1
        else:
            self.ratioMulticlass["F"] += 1

    def setAccuracy(self):
        sum = self.ratio["T+"] + self.ratio["T-"]
        N = sum + self.ratio["F+"] + self.ratio["F-"]
        self.accuracy = (1/N) * sum

    def setAccuracyMulticlass(self):
        sum = self.ratioMulticlass["T"]
        N = sum + self.ratioMulticlass["F"]
        self.accuracy = (1/N) * sum


    def setPrecision(self):
        TP = self.ratio["T+"]
        FP = self.ratio["F+"]
        try:
            self.precision = TP/(TP+FP)
        except Exception:
            self.precision = 1

    def setRecall(self):
        TP = self.ratio["T+"]
        FN = self.ratio["F-"]  
        try:
            self.recall = TP/(TP+FN)
        except Exception:
            self.recall = 0 

    def setF_Measure(self):
        self.f = (2 * self.precision * self.recall)/(self.precision + self.recall) 