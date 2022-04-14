import pdb

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







