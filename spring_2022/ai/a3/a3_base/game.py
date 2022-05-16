import sys

class Player:
    def __init__(self):
        self.p1_char = "X"
        self.p2_char = "O"

    def choose_action(self, state):
        pass

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play(self, state):
        pass