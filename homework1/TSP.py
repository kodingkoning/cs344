"""
Run a local search formulation on the Traveling Salesman problem.

First use the AIMA hill-climbing, then the simulated annealing implementations.
TODO: hill-climbing
TODO: simulated annealing

Elizabeth Koning, for CS344, February 2019
"""

import string, random
import numpy as np
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule
# need hill_climbing and simulated_annealing for the two approaches, need exp_schedule for annealing

class TSP(Problem):
    """
    TODO: describe why I did this (in the Jupyter notebook)
    """

    def __init__(self, initial, distances, num_cities):
        self.initial = initial
        self.distances = distances
        self.num_cities = num_cities

    def actions(self, state):
        # lists all pairs of cities that could be flipped in the order
        starts = np.zeros(0, dtype=np.int8)
        ends   = np.zeros(0, dtype=np.int8)

        # TODO: look for a way to do this without a for loop
        for city in range(self.num_cities):
            starts = np.append(starts, np.full(self.num_cities-city-1, city, dtype=np.int8))
            ends   = np.append(ends, np.arange(city+1, self.num_cities, dtype=np.int8))

        actions = np.append(starts, ends)
        actions = actions.reshape(-1, 2, order='F')
        return actions

    def result(self, state, action):
        # return the state that results from executing the given action in the current state
        new_state = np.copy(state)
        city1 = state[action[0]]
        city2 = state[action[1]]
        new_state[action[0]] = city2
        new_state[action[1]] = city1
        return new_state

    def value(self, state):
        # TODO: make it count up the length of the route
        # NOTE: this will be maximized, so make sure that higher is better
        value = 0
        for i in range(len(state)):
            value += self.distances[state[i]][state[(i+1)%self.num_cities]]
        return -value

# TODO: describe state and action representations
# TODO: configure the system to build TSP worlds of any number of cities with random distances (symmetric)
# TODO: explain which local search algorithm works better

if __name__ == '__main__':
    # set up city with random but symmetrical distances
    num_cities = 100
    min_dist = 1
    max_dist = 10
    initial = np.arange(num_cities)

    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities-i):
            row = i
            col = num_cities-j-1
            if row == (col):
                distances[row][col] = 0
            else:
                distances[row][col] = random.randint(min_dist, max_dist)
                distances[col][row] = distances[row][col]

    print("Distances:")
    print(distances)

    p = TSP(initial, distances, num_cities)
    print("Initial:")
    print(initial)

    hill_solution = hill_climbing(p)
    print("\nHill-climbing solution:")
    print(hill_solution)
    print("Hill-climbing value = " + str(p.value(hill_solution)))

    annealing_solution = simulated_annealing(p)
    print("\nSimulated Annealing soltion:")
    print(annealing_solution)
    print("Simulated Annealing value = " + str(p.value(annealing_solution)))

    #TODO: write up explanations of the problem and its setup.
    #TODO: explain why hill-climbing works better here