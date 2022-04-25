from rgb import *
from util import *
from agent import *
import sys




if __name__ == '__main__':
    
    cmd = sys.argv[1]
    
    state_string = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STATE
    state = State(state_string)
    agent = Agent()
    #action = Action(None, None, None, None)
    n = 8

    match cmd:
        case 'random':
            agent.random_walk(state, n)
        case "bfs":
            agent._search(state, "BFS")
        case "dfs":
            agent._search(state, "DFS")
        case _:
            raise Exception("Command not recognized")

