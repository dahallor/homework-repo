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
        q_state = Q_State(state_string)
        if self.train != None:
            #use formula
            self._add_to_QTable(q_state.key)
            action = self._init_QLearning(q_state)
        else:
            #just return max value in q table
            pass

        #pdb.set_trace()
        return action
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


    def _add_to_QTable(self, key):
        if key not in self.q:
            self.q[key] = {
            "u" : 0,
            "d" : 0,
            "l" : 0,
            "r" : 0,
            "_" : 0}

        self.save()

    def _get_max_state(self, key):
        max_value = 0
        directions = ["u", "d", "l", "r", "_"]
        max_direction = random.choice(directions)
        for direction in self.q[key]:
            current_val = self.q[key][direction]
            if current_val > max_value:
                max_value = current_val
                max_direction = direction


        return max_value, max_direction

    def _get_current_state_value(self, key, direction):
        current_value = self.q[key][direction]
        return current_value

    def _set_new_q_value(self, key, direction, value):
        self.q[key][direction] = value


    def _init_QLearning(self, q_state):
        alpha = .01
        gamma = .9
        max_value, max_direction = self._get_max_state(q_state.key)
        current_value = self._get_current_state_value(q_state.key, max_direction)
        new_value = (1-alpha) * current_value + alpha * (q_state.reward() + gamma * max_value)
        self._set_new_q_value(q_state.key, max_direction, new_value)
        return max_direction


