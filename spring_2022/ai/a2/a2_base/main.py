from rgb import *
from util import *
from agent import *
import sys




if __name__ == '__main__':
    
    cmd = sys.argv[1]
    if cmd:

        state_string = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STATE
        state = State(state_string)
        agent = Agent()
        n = 8

        if cmd == 'random':
            agent.random_walk(state, n)

