import sys

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
        #pdb.set_trace()

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

class Action():
    def __init__(self):
        pass
    
    def slide(self, state, aux, x1, y1, x2, y2):
        aux.__str__(state, "append")

        currentMatrix = state.matrix

        if currentMatrix[y2][x2] != None:
            return
        coordinates = [x1, y1]

        sub = []
        for i in range(len(state.boarderingSpace)):
            sub.append(state.boarderingSpace[i][:2])
        #pdb.set_trace()
        if coordinates in sub:
            value = currentMatrix[y1][x1]
            currentMatrix[y2][x2] = value
            currentMatrix[y1][x1] = None
            state.matrix = currentMatrix
            aux.clone(state)
            #pdb.set_trace()



    def rotate(self, state, aux, y, dx):
        aux.__str__(state, "append")
        match dx:
            case 1:
                currentMatrix = state.matrix
                value = currentMatrix[y][-1]
                currentMatrix[y].pop(-1)
                currentMatrix[y].insert(0, value)
                state.matrix = currentMatrix
                aux.clone(state)
                #pdb.set_trace()
            case -1:
                currentMatrix = state.matrix
                value = currentMatrix[y][0]
                currentMatrix[y].pop(0)
                currentMatrix[y].append(value)
                state.matrix = currentMatrix
                aux.clone(state)
                #pdb.set_trace()
            case _:
                print("Please enter either 1 for a right turn or -1 for a left turn")

class State:
    def __init__(self, string):
        self.startState = string
        self.currentState = self.startState
        self.goal = False
        self.matrix = []
        self.boarderingSpace = []
        self.possibleActions = []
        self.previousStates = []
 
    def is_goal(self):
        width = len(self.matrix[0])
        height = len(self.matrix)

        if len(self.matrix) == 0:
            self.goal = False
            return self.goal

        for i in range(width):
            top_value = self.matrix[0][i]
            for j in range(1, height):
                current_value = self.matrix[j][i]
                if current_value == None:
                    continue
                if current_value == top_value:
                    continue
                else:
                    self.goal = False
                    return self.goal
        self.goal = True
        return self.goal

    def actions(self, aux, option):
        aux.setBoarderSpace(self)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == None:
                    x = j
                    y = i
        for i in range(len(self.matrix)):
            #pdb.set_trace()
            left = "rotate({}, -1)".format(i)
            right = "rotate({}, 1)".format(i)
            self.possibleActions.append(left)
            self.possibleActions.append(right)
            if option == "print":
                print(left)
                print(right)
        for i in range(len(self.boarderingSpace)):
            slide = "slide({}, {}, {}, {})".format(self.boarderingSpace[i][0], self.boarderingSpace[i][1], x, y)
            self.possibleActions.append(slide)
            if option == "print":
                print(slide)


    def execute(self, action, index, aux):
        self.actions(aux, "no print")
        currentAction = self.possibleActions[index]


        array = aux.extractAction(index, self)
        if array[0] == "r":
            while(self.currentState not in self.previousStates):
                print(self.currentState)
                try:
                    action.rotate(self, aux, array[1], array[2])

                except Exception:
                    break
                      
        if array[0] == "s":
            direction = ""
            for i in range(len(self.boarderingSpace)):
                if self.boarderingSpace[i][0] == array[1] and self.boarderingSpace[i][1] == array[2]:
                    direction = self.boarderingSpace[i][2]
            
            x1 = array[1]
            y1 = array[2]
            x2 = array[3]
            y2 = array[4]
            while(self.currentState not in self.previousStates):
                print(self.currentState)
                action.slide(self, aux, x1, y1, x2, y2)
                aux.setBoarderSpace(self)
                #pdb.set_trace()
                for i in range(len(self.boarderingSpace)):
                    if direction == self.boarderingSpace[i][2]:
                        x1 = self.boarderingSpace[i][0]
                        y1 = self.boarderingSpace[i][1]
                        
                x2, y2 = aux.findNull(self)

DEFAULT_STATE = '12345|1234 |12354'


if __name__ == '__main__':

    cmd = sys.argv[1]
    if cmd:

        aux = Aux()
        state_string = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STATE
        state = State(state_string)
        matrix = aux.convertToMatrix(state)
        action = Action()

        if cmd == 'print':
            print(state.currentState)
        elif cmd == 'goal':
            print(state.is_goal())
        elif cmd == 'actions':
            state.actions(aux, "print")
        elif cmd.startswith('walk'):
            index = int(sys.argv[1][4])
            state.execute(action, index, aux)
