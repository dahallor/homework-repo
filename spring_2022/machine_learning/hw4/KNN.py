import numpy as np
import pdb


class KNN:
    def distance(self, pca, IL, k):
        NN = []
        for i in range(k):
            temp = [9999999999999999, 0]
            NN.append(temp)
        for i in range(len(IL.validX)):
            sum = 0
            for j in range(len(IL.validX[i])):
                A = IL.trainX[i][j]
                B = IL.validX[i][j]
                sum += np.pow((A-B), 2)
            sum = np.sqrt(sum)
            for j in range(k):
                NN[i][0]
                if sum < NN[j][0]:
                    NN[j][0] = sum
                    NN[j][1] = IL.validY[i][0]
                    break
        
        

    def plottingPoints(self, pca, max_values, X):
        #D x k
        self.trainingPCA = np.zeros((len(X), len(max_values)))
        print("Calculating Training Principle Components...")
        for i in range(len(X)):
            for j in range(len(max_values)):
                vector = max_values[j]
                currentEigvector = pca.eigvectors[:, vector:vector+1]
                self.trainingPCA[i][j] = np.matmul(X[i], currentEigvector)
    
    def plottingPointsValid(self, pca, max_values, X):
        #D x k
        self.validPCA = np.zeros((len(X), len(max_values)))
        print("Calculating Validation Principle Components...")
        for i in range(len(X)):
            for j in range(len(max_values)):
                vector = max_values[j]
                currentEigvector = pca.eigvectorsValid[:, vector:vector+1]
                self.validPCA[i][j] = np.matmul(X[i], currentEigvector)

 