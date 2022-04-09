class State:
    """
    Represents a state.
    """

    def __init__(self, string):
        self.currentState = string
        self.goal = False

    def setCurrentState(self, data):
        self.currentState = data
        
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
                        line.append(float(state[i]))
                    except Exception:
                        line.append(state[i])
            if i == len(state) - 1:
                matrix.append(line)

        return matrix
 
    def is_goal(self, matrix):
        width = len(matrix[0])
        height = len(matrix)

        if len(matrix) == 0:
            return False

        for i in range(width):
            top_value = matrix[0][i]
            for j in range(1, height):
                current_value = matrix[j][i]
                if current_value == None:
                    continue
                if current_value == top_value:
                    continue
                else:
                    return False

        return True
