import json
import os
import random
import pdb

from .state import State


class Q_State(State):
    '''Augments the game state with Q-learning information'''

    def __init__(self, string):
        super().__init__(string)

        # key stores the state's key string (see notes in _compute_key())
        self.key = self._compute_key()

    def _compute_key(self):
        '''
        Returns a key used to index this state.

        The key should reduce the entire game state to something much smaller
        that can be used for learning. When implementing a Q table as a
        dictionary, this key is used for accessing the Q values for this
        state within the dictionary.
        '''

        # this simple key uses the 3 object characters above the frog
        # and combines them into a key string
        return ''.join([
            self.get(self.frog_x - 1, self.frog_y - 1) or '_',
            self.get(self.frog_x, self.frog_y - 1) or '_',
            self.get(self.frog_x + 1, self.frog_y - 1) or '_',
        ])

    def reward(self):
        '''Returns a reward value for the state.'''

        if self.at_goal:
            return self.score
        elif self.is_done:
            return -10
        else:
            return 0


class Agent:

    def __init__(self, train=None):

        # train is either a string denoting the name of the saved
        # Q-table file, or None if running without training
        self.train = train

        # q is the dictionary representing the Q-table
        self.q = {}

        # name is the Q-table filename
        # (you likely don't need to use or change this)
        self.name = train or 'q'

        # path is the path to the Q-table file
        # (you likely don't need to use or change this)
        self.path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'train', self.name + '.json')

        self.load()

    def load(self):
        '''Loads the Q-table from the JSON file'''
        try:
            with open(self.path, 'r') as f:
                self.q = json.load(f)
            if self.train:
                print('Training {}'.format(self.path))
            else:
                print('Loaded {}'.format(self.path))
        except IOError:
            if self.train:
                print('Training {}'.format(self.path))
            else:
                raise Exception('File does not exist: {}'.format(self.path))
        return self

    def save(self):
        '''Saves the Q-table to the JSON file'''
        with open(self.path, 'w') as f:
            json.dump(self.q, f, indent = 1)
        return self

    def choose_action(self, state_string):
        '''
        Returns the action to perform.

        This is the main method that interacts with the game interface:
        given a state string, it should return the action to be taken
        by the agent.

        The initial implementation of this method is simply a random
        choice among the possible actions. You will need to augment
        the code to implement Q-learning within the agent.
        '''


        matrix = self._convert_to_matrix(state_string)
        Fx, Fy = self._get_current_position(matrix)
        up, down, left, right, none, dy_up, dy_down, dx_left, dx_right = self._get_new_Q(Fx, Fy, matrix)
        self._set_new_Q(up, down, left, right, none, dy_up, dy_down, dx_left, dx_right, Fx, Fy)

        pdb.set_trace()
        #return random.choice(State.ACTIONS)

    def _convert_to_matrix(self, state_string):
        step = 16
        prev_step = 0
        current_step = 16
        state_matrix = []
        for i in range(9):
            slice = state_string[prev_step:current_step]
            state_matrix.append(slice)
            prev_step = current_step + 1
            current_step = prev_step + step
        return state_matrix

    def _get_current_position(self, matrix):
        for i in range(9):
            try:
                Fx = matrix[i].index("F")
                Fy = i
            except ValueError:
                pass
        return Fx, Fy

    def _get_new_Q(self, Fx, Fy, matrix):
        bad_states = ["~", ">", "<"]
        #up
        try:
            dy_up = Fy - 1
            square = matrix[dy_up][Fx]
            if square in bad_states:
                up = -10
            else:
                up = .5
        except Exception:
            up = 0
            dy_up = None

        #down
        try:
            dy_down = Fy + 1
            square = matrix[dy_down][Fx]
            if square in bad_states:
                down = -10
            else:
                down = .5
        except Exception:
            down = 0
            dy_down = None

        #right
        try:
            dx_right = Fx + 1
            square = matrix[Fy][dx_right]
            if square in bad_states:
                right = -10
            else:
                right = .5
        except Exception:
            right = 0
            dx_right = None

        #left
        try:
            dx_left = Fx - 1
            square = matrix[Fy][dx_left]
            if square in bad_states:
                left = -10
            else:
                left = .5
        except Exception:
            left = 0
            dx_left = None

        #null
        try:
            dx = Fx - 1
            square = matrix[Fy][dx]
            if square == ">":
                none = -10
            dx = Fx + 1
            square = matrix[Fy][dx]
            if square == "<":
                none = -10
            else:
                none = .5
        except Exception:
            none = 0

        return up, down, left, right, none, dy_up, dy_down, dx_left, dx_right
        

    def _set_new_Q(self, up, down, left, right, none, dy_up, dy_down, dx_left, dx_right, Fx, Fy):
        alpha = .01
        discount = .9
        current_state = "S_" + str(Fy) + str(Fx)
        Q_new_none = (1 - alpha) * (self.q[current_state]["none"])
        

    def initQTable(self):
        x = 16
        y = 9
        for i in range(y):
            for j in range(x):
                state_name = "S_"
                state_name += str(i)
                state_name += ","
                state_name += str(j)
                if i != 0:
                    self.q[state_name] = {
                    "u" : 0,
                    "d" : 0,
                    "l" : 0,
                    "r" : 0,
                    "_" : 0}
                else:
                    self.q[state_name] = 10
        self.save()

