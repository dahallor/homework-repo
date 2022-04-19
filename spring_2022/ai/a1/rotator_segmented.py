import sys
from state import *
from action import *
from helpers import *

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

        
