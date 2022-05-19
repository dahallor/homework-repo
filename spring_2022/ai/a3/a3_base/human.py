from game import *

class HumanPlayer(Player):
    def __init__(self, char):
        super().__init__(char)


    def choose_action(self, state):
        actions = state.actions(self.char)
        for i in range(len(actions)):
            print("{}: {}".format(i, actions[i]))
        answer = input("Please choose an action: ")
        try:
            state.execute(actions[int(answer)])
        except:
            raise Exception("Invalid Answer")
        return state
