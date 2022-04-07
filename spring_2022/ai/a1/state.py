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
            if state[i] == "|":
                matrix.append(line)
                line = []
                continue
            elif state[i] == " ":
                line.append(None)
            elif i == len(state) - 1:
                try:
                    line.append(float(state[i]))
                except Exception:
                    line.append(state[i])
                matrix.append(line)
            else:
                try:
                    line.append(float(state[i]))
                except Exception:
                    line.append(state[i])
        
        return 
        
    def is_goal(self, matrix):
        #this is easier with numpy so see if it can be used first
        pass