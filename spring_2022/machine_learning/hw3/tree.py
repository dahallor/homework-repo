class Tree:
    def __init__(self):
        self.featureHash = {}

    def setHash(self, IL):
        for i in range(len(IL.trainX[0])):
            var = "x" + str(i+1)
            self.featureHash[var] = {}
        self.featureHash["total obs"] = [len(IL.trainX)]
        

    def fillHashData(self, IL):
        for i in range(len(IL.trainX)):
            for j in range(len(IL.trainX[i])):
                var = "x" + str(j + 1)
                answer = IL.trainY[i]
                feature = IL.trainX[i][j]
                hash = self.featureHash[var]
                #print(var, answer, feature, hash)
                if feature not in hash:
                    #format is list[0]: Y = 0 list[1]: Y = 1 list[2] = Entropy
                    self.featureHash[var][feature] = [0, 0, 0]
                match answer:
                    case 0:
                        arr = self.featureHash[var][feature]
                        arr[0] += 1
                    case 1:
                        arr = self.featureHash[var][feature]
                        arr[1] += 1




