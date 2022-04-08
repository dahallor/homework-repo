import sys
from state import *
from action import *

DEFAULT_STATE = '12345|1234 |12354'




if __name__ == '__main__':

    cmd = sys.argv[1]
    if cmd:

        state_string = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STATE
        state = State(state_string)

        if cmd == 'print':
            print(state.currentState)
        elif cmd == 'goal':
            matrix = state.convertToMatrix()
            print(matrix)
            print(state.is_goal(matrix))
        elif cmd == 'actions':
            pass  # replace with your code
        elif cmd.startswith('walk'):
            pass  # replace with your code

        