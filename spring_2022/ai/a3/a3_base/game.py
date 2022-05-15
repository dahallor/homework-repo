from sys import ps1


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def choose_action(self, state):
        pass

class Game:
    def __init__(self, p1, p2, state):
        self.p1 = p1
        self.p2 = p2

    def play(self):
        pass