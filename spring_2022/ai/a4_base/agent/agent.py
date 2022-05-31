import json
import os
import random
import pdb
import math

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
            #3 squares 1 row above F
            self.get(self.frog_x - 1, self.frog_y - 1) or '_',
            self.get(self.frog_x, self.frog_y - 1) or '_',
            self.get(self.frog_x + 1, self.frog_y - 1) or '_',
            '|',
            #3 squarees in the 3 rows above F
            self.get(self.frog_x, self.frog_y - 1) or '_',
            self.get(self.frog_x, self.frog_y - 2) or '_',
            self.get(self.frog_x, self.frog_y - 3) or '_',
            '|',
            #3 squares 1 row below F
            self.get(self.frog_x - 1, self.frog_y + 1) or '_',
            self.get(self.frog_x, self.frog_y + 1) or '_',
            self.get(self.frog_x + 1, self.frog_y + 1) or '_',
            '|',
            #3 squarees in the 3 rows below F
            self.get(self.frog_x, self.frog_y + 1) or '_',
            self.get(self.frog_x, self.frog_y + 2) or '_',
            self.get(self.frog_x, self.frog_y + 3) or '_',
            '|',
            #3 squares to left of F
            self.get(self.frog_x - 1, self.frog_y) or '_',
            self.get(self.frog_x - 2, self.frog_y) or '_',
            self.get(self.frog_x - 3, self.frog_y) or '_',
            '|',
            #3 squares to right of F
            self.get(self.frog_x + 1, self.frog_y) or '_',
            self.get(self.frog_x + 2, self.frog_y) or '_',
            self.get(self.frog_x + 3, self.frog_y) or '_',
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

        #how many steps until goal is reached to raise discount factor by. Resets to 0 when goal is reached
        self.current_path = []

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

        q_state = Q_State(state_string)
        if self.train != None:
            #use formula
            self._add_to_QTable(q_state.key)
            action = self._build_path(q_state, q_state.key)
            self._QLearning(q_state)
        else:
            #just return max value in q table
            pass

        #pdb.set_trace()
        return action
        #return random.choice(State.ACTIONS)


    def _add_to_QTable(self, key):
        if key not in self.q:
            self.q[key] = {
            "u" : 0,
            "d" : 0,
            "l" : 0,
            "r" : 0,
            "_" : 0}

        self.save()

    def _max_action(self, q_state, key):
        max_val = -math.inf
        max_move = ""
        for i in range(len(q_state.ACTIONS)):
            a = q_state.ACTIONS[i]
            val = self.q[key][a]
            if val > max_val:
                max_val = val
                max_move = a
        return max_val, max_move

    def _build_path(self, q_state, key):
        probability = random.random()
        if probability <= .4:
            #explore
            action = random.choice(q_state.ACTIONS)
        else:
            #exploit
            val, action = self._max_action(q_state, key)
        temp = []
        temp.append(q_state.key)
        temp.append(action)
        temp.append(q_state.reward())
        self.current_path.append(temp)
        
        return action


    def _QLearning(self, q_state):
        alpha = .1
        gamma = .9
        if len(self.current_path) >= 2:
            t = len(self.current_path)

            #value function
            reward = q_state.reward()
            sum = 0
            for i in range(t-1, -1, -1):
                sum += math.pow(gamma, t) * self.current_path[i][2]
                t -= 1


            for i in range(len(self.current_path) -1, 0, -1):
                key = self.current_path[i][0]
                v, a = self._max_action(q_state, key)
                q_value = (1-alpha) * sum + alpha * (reward + gamma * v)
                self.q[self.current_path[i-1][0]][self.current_path[i-1][1]] = q_value

            #pdb.set_trace()
            if q_state.is_done == True:
                self.current_path = []








