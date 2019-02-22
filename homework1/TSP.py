"""
Run a local search formulation on the Traveling Salesman problem.

First use the AIMA hill-climbing, then the simulated annealing implementations.
TODO: hill-climbing
TODO: simulated annealing

Elizabeth Koning, for CS344, February 2019
"""

import string, random
import numpy as np
from search import Problem, hill_climbing, simulated_annealing

class TSP(Problem):
    def __init__(self, initial, distances, num_cities):
        self.initial = initial
        self.distances = distances
        self.num_cities = num_cities

    def actions(self, state):
        # lists all pairs of cities that could be flipped in the order
        starts = np.zeros(0, dtype=np.int8)
        ends   = np.zeros(0, dtype=np.int8)

        for city in range(self.num_cities):
            # create list of this city as the first city to flip
            starts = np.append(starts, np.full(self.num_cities-city-1, city, dtype=np.int8))
            # create list of all the later cities as second cities to switch (all earlier cities will have the current city as the second city of the flip)
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
        value = 0
        for i in range(len(state)):
            value += self.distances[state[i]][state[(i+1)%self.num_cities]]
        return -value


"""
State and action representations
For the local search, the TSP extends the Problem from csp.py and implements states and actions.
The states, as in the n-queens problem, are a complete solution. In this case, we start with a list of the cities. The cities are numbered, so they are in that order to start.
The order of the cities in the list represents the state. The last city loops around and leads back to the first city. This first city is only once in the list because the value() considers that it needs to loop around to the beginning again.
The actions are represented as pairs of cities. Any two cities can be swapped in the travel order. Any of these actions keep the state as a complete solution, but it may make the value larger or smaller.

Below, a system with any number of cities can be created by changing the num_cities variable. From there, it randomly calculates distances between all the cities.
The salesman can travel from any city to any other city in one step.

The hill-climbing algorithm works consistently better and by a significant amount, regardless of the size of the system. (As long as the number of cities is high enough that both algorithms do not always get the ideal solution, as happens with num_cities < 5.)
If the cities were geographically coherent, then this would make sense. Since they are not, this is slightly more surprising.
I would have expected that simulated annealing would work better here. For this problem (since the cities are not geogrpahically cohert), there are times that it is beneficial to be willing to jump to a worse value in order to get out of a local optima and find the global optima.
"""

# set up city with random but symmetrical distances
num_cities = 10
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
