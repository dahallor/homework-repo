import pdb

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
                






    
            
