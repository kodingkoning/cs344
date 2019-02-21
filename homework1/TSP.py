"""
Run a local search formulation on the Traveling Salesman problem.

First use the AIMA hill-climbing, then the simulated annealing implementations.
TODO: hill-climbing
TODO: simulated annealing

Elizabeth Koning, for CS344, February 2019
"""

import sys
sys.path.append('/home/erk24/344/cs344-code/tools/aima/')
#TODO: import hill-climbing and simmulated annealing
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule
#need hill_climbing and simulated_annealing for the two approaches, need exp_schedule for annealing

#TODO: setup the problem
#states
#actions

#TODO: implement with

print("Starting hill climbing")


class TSP(Problem):
    """
    State:
    Move:
    """
    def __init__(self, initial):
        #TODO: decide how to formulate the problem
        self.initial = initial
        pass

    def actions(self, state):
        #TODO: decide what actions are valid
        #basically need to be able to flip cities around in order and see if it gets better
        pass

    def result(self, state, action):
        #TODO: return the state that results from executing the given action in the current state
        pass

    def value(self, state):
        #TODO: make it count up the length of the route
        #NOTE: this will be maximized, so make sure that higher is better
        return 0

#TODO: describe state and action representations
#TODO: configure the system to build TSP worlds of any number of cities with random distances (symmetric)
#TODO: explain which local search algorithm works better



#print("Starting simulated annealing")
