import sys

DEFAULT_STATE = '12345|1234 |12354'


class Action:
    """
    Represents an action that can be performed on a state.
    """

    def __init__(self):
        """
        Initializes an action. Additional arguments will be needed to specify the details
        of the action. You may find it preferable to subclass this class for each of
        the possible action types.
        """
        pass  # replace with your code


class State:
    """
    Represents a state.
    """

    def __init__(self, string):
        self.currentState = string

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
        
        return matrix


if __name__ == '__main__':

    cmd = sys.argv[1]
    if cmd:

        state_string = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STATE
        state = State(state_string)

        if cmd == 'print':
            print(state.currentState)
        elif cmd == 'goal':
            pass  # replace with your code
        elif cmd == 'actions':
            pass  # replace with your code
        elif cmd.startswith('walk'):
            pass  # replace with your code

        state.convertToMatrix()
