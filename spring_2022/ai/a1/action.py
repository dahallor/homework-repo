class Action():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == None:
                    string += " "
                else:
                    string += str(self.matrix[i][j])
            if i < len(self.matrix) -1:
                string += "|"
        print(string)
        
    
    def slide(self, state, x1, y1, x2, y2):
        state.setBoarderSpace()
        currentMatrix = self.matrix
        if currentMatrix[y2][x2] != None:
            return
        coordinates = [x1, y2]
        if coordinates in state.boarderingSpace:
            value = currentMatrix[y1][x1]
            currentMatrix[y2][x2] = value
            currentMatrix[y1][x1] = None
            self.matrix = currentMatrix
            print(self.matrix)


    def rotate(self, y, dx):
        match dx:
            case 1:
                currentMatrix = self.matrix
                value = currentMatrix[y][-1]
                currentMatrix[y].pop(-1)
                currentMatrix[y].insert(0, value)
                self.matrix = currentMatrix
            case -1:
                currentMatrix = self.matrix
                value = currentMatrix[y][0]
                currentMatrix[y].pop(0)
                currentMatrix[y].append(value)
                self.matrix = currentMatrix
            case _:
                print("Please enter either 1 for a right turn or -1 for a left turn")






