import pdb

class Aux:
    def __init__(self):
        pass

    def __str__(self, state, cmd):
        string = ""
        for i in range(len(state.matrix)):
            for j in range(len(state.matrix[i])):
                if state.matrix[i][j] == None:
                    string += " "
                else:
                    string += str(state.matrix[i][j])
            if i < len(state.matrix) -1:
                string += "|"
        if cmd == "append":
            state.previousStates.append(string)
        if cmd == "return str":
            return string
        
    def __eq__(self, state):
        currentString = self.__str__("return str")
        for i in range(len(state.previousStates)):
            if currentString == state.previousStates[i]:
                return True
        return False

    def clone(self, state):
        string = self.__str__(state, "return str")
        state.currentState = string
        #pdb.set_trace()




    def setBoarderSpace(self, state):
        state.boarderingSpace = []
        x, y = self.findNull(state)

        #Up
        try:
            yPrime = y - 1
            if yPrime < 0:
                raise Exception
            state.boarderingSpace.append([x, yPrime, "up"])
        except Exception:
            pass

        #Down
        try:
            yPrime = y + 1
            if yPrime > len(state.matrix) - 1:
                raise Exception
            state.boarderingSpace.append([x, yPrime, "down"])
        except Exception:
            pass

        #Right
        try:
            xPrime = x + 1
            if xPrime > len(state.matrix[y]) - 1:
                raise Exception
            state.boarderingSpace.append([xPrime, y, "right"])
        except Exception:
            pass

        #Left
        try:
            xPrime = x - 1
            if xPrime < 0:
                raise Exception
            state.boarderingSpace.append([xPrime, y, "left"])
        except Exception:
            pass

    def continueSlide(self, state, direction, x, y):
        match direction:
            case "up":
                yPrime = y - 1
                if yPrime < 0:
                    raise Exception
                return x, yPrime

            case "down":
                yPrime = y + 1
                if yPrime > len(state.matrix) - 1:
                    raise Exception
                return x, yPrime

            case "right":
                xPrime = x + 1
                if xPrime > len(state.matrix[y]) - 1:
                    raise Exception
                return xPrime, y

            case "left":
                xPrime = x - 1
                if xPrime < 0:
                    raise Exception
                return xPrime, y

            case _:
                raise Exception


        
    def convertToMatrix(self, state):
        localState = state.currentState
        
        localMatrix = []
        line = []
        for i in range(len(localState)):
            match localState[i]:
                case "|":
                    localMatrix.append(line)
                    line = []
                case " ":
                    line.append(None)
                case _:
                    try:
                        line.append(int(localState[i]))
                    except Exception:
                        line.append(localState[i])
            if i == len(localState) - 1:
                localMatrix.append(line)
        state.matrix = localMatrix

    def extractAction(self, index, state):
        action = state.possibleActions[index]
        actions = []
        actions.append(action[0])
        for i in range(len(action)):
            try:
                if action[i-1] == "-":
                    digit = action[i-1] + action[i]
                    actions.append(int(digit))
                else:
                    digit = int(action[i])
                    actions.append(digit)
            except Exception:
                continue

        return actions

    def findNull(self, state):
        for i in range(len(state.matrix)):
            for j in range(len(state.matrix[i])):
                if state.matrix[i][j] == None:
                    y = i
                    x = j

        return x, y

