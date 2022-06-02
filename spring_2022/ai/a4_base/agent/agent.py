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
            #1 square to right of F
            self.get(self.frog_x + 1, self.frog_y) or '_',
            #3 squares 1 row below F
            self.get(self.frog_x - 1, self.frog_y + 1) or '_',
            self.get(self.frog_x, self.frog_y + 1) or '_',
            self.get(self.frog_x + 1, self.frog_y + 1) or '_',
            #1 square to left of F
            self.get(self.frog_x - 1, self.frog_y) or '_'

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
            json.dump(self.q, f, indent = 2)
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
            val = max(self.q[q_state.key])
            index = self.q[q_state.key].index(val)
            action = q_state.ACTIONS[index]

        #Helper code
        action = self._helper_code(q_state, action)
        #pdb.set_trace()
        return action
        #return random.choice(State.ACTIONS)


    def _add_to_QTable(self, key):
        if key not in self.q:
            self.q[key] = [0, 0, 0, 0, 0]
        self.save()

    def _max_action(self, q_state, key):
        array = self.q[key]
        max_val = max(array)
        index = array.index(max_val)
        return index

    def _build_path(self, q_state, key):
        probability = random.random()
        search_type = ""
        if probability <= .3:
            #explore
            search_type = "explore"
            action = random.choice(q_state.ACTIONS)
        else:
            #exploit
            search_type = "exploit"
            index = self._max_action(q_state, key)
            action = q_state.ACTIONS[index]
        temp = []
        temp.append(q_state.key)
        if search_type == "exploit":
            action = self._helper_code(q_state, action)
        temp.append(action)
        temp.append(q_state.reward())
        self.current_path.append(temp)
        
        return action

    def _helper_code(self, q_state, action):
        if q_state.get(q_state.frog_x, q_state.frog_y - 1) == "-" and q_state.get(q_state.frog_x - 1, q_state.frog_y - 1) != ">":
            action = "u"
        if q_state.frog_y == 7 and action == "d":
            if q_state.get(q_state.frog_x, q_state.frog_y - 1) == "-" and q_state.get(q_state.frog_x + 1, q_state.frog_y - 1) != ">":
                action = "u"
        if q_state.frog_y == 4 and q_state.get(q_state.frog_x, q_state.frog_y - 1) == "[":
                action = "u"
        if q_state.frog_y == 4 and action == "d":
            action = random.choice(["l", "r", "_"])
        if q_state.frog_y == 3 and action == "d" and q_state.get(q_state.frog_x - 1, q_state.frog_y) != "_":
            if q_state.get(q_state.frog_x, q_state.frog_y - 1) == "]":
                action = "u"
            else:
                action = random.choice(["l", "r", "_"])
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
                index = self._max_action(q_state, key)
                q_value = (1-alpha) * sum + alpha * (reward + gamma * self.q[key][index])
                action = self.current_path[i-1][1]
                new_index = q_state.ACTIONS.index(action)
                self.q[self.current_path[i-1][0]][new_index] = q_value

            #pdb.set_trace()
            if q_state.is_done == True:
                self.current_path = []








