class State:
    def __init__(self, string):
        self.currentState = string
        self.goal = False
        self.matrix = []
        self.boarderingSpace = []

    def setCurrentState(self, data):
        self.currentState = data

    def setBoarderSpace(self):
        self.boarderingSpace = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == None:
                    y = i
                    x = j
        #Up
        try:
            yPrime = y - 1
            if yPrime < 0:
                raise Exception
            self.boarderingSpace.append([x, yPrime])
        except Exception:
            pass

        #Down
        try:
            yPrime = y + 1
            if yPrime > len(self.matrix) - 1:
                raise Exception
            self.boarderingSpace.append([x, yPrime])
        except Exception:
            pass

        #Right
        try:
            xPrime = x + 1
            if xPrime > len(self.matrix[y]) - 1:
                raise Exception
            self.boarderingSpace.append([xPrime, y])
        except Exception:
            pass

        #Left
        try:
            xPrime = x - 1
            if xPrime < 0:
                raise Exception
            self.boarderingSpace.append([xPrime, y])
        except Exception:
            pass
        
    def convertToMatrix(self):
        state = self.currentState
        matrix = []
        line = []
        for i in range(len(state)):
            match state[i]:
                case "|":
                    matrix.append(line)
                    line = []
                case " ":
                    line.append(None)
                case _:
                    try:
                        line.append(int(state[i]))
                    except Exception:
                        line.append(state[i])
            if i == len(state) - 1:
                matrix.append(line)
        self.matrix = matrix
        return matrix
 
    def is_goal(self, matrix):
        width = len(matrix[0])
        height = len(matrix)

        if len(matrix) == 0:
            self.goal = False
            return self.goal

        for i in range(width):
            top_value = matrix[0][i]
            for j in range(1, height):
                current_value = matrix[j][i]
                if current_value == None:
                    continue
                if current_value == top_value:
                    continue
                else:
                    self.goal = False
                    return self.goal
        self.goal = True
        return self.goal

    def actions(self):
        self.setBoarderSpace()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == None:
                    x = j
                    y = i
        for i in range(len(self.matrix)):
            print("rotate({}, -1)".format(i))
            print("rotate({}, 1)".format(i))
        for i in range(len(self.boarderingSpace)):
            print("slide({}, {}, {}, {})".format(self.boarderingSpace[i][0], self.boarderingSpace[i][1], x, y))


    def execute(action):
        pass
            
