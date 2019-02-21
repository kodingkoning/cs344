"""
Run a local search on the course scheduling problem

Elizabeth Koning, for CS344, February 2019
"""

from utils import is_in
import sys
#sys.path.append('/home/erk24/344/cs344-code/')
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time

courses = ["cs108", "cs112", "cs212", "cs214", "cs232", "cs262", "cs300"]
faculty = ["dschuurman", "adams", "vlinden", "hplantin", "pmb4"]
times = ["mwf900", "mwf1030", "mwf1130", "mwf1230", "mwf130"]
rooms = ["nh253", "sb382"]
#TODO: add constraints
#constraints = {"cs108": "dschuurman", "cs112":"adams" }

#TODO: implement a solution with AIMA constraint satisfaction and explain why it works

class AbsVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs( x*math.sin(x) )


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    n = 10
    hill_max = 0
    sa_max = 0

    for count in range(n):
        maximum = 30
        initial = randrange(0, maximum)
        p = AbsVariant(initial, maximum, delta=1.0)
        print('Initial                      x: ' + str(p.initial)
              + '\t\tvalue: ' + str(p.value(initial))
              )

        # Solve the problem using hill-climbing.
        start = time.time()
        hill_solution = hill_climbing(p)
        hill_time = time.time() - start
        print('Hill-climbing solution       x: ' + str(hill_solution)
              + '\tvalue: ' + str(p.value(hill_solution))
              + '\ttime: ' + str(hill_time)
              )
        if p.value(hill_solution) > hill_max:
            hill_max = p.value(hill_solution)

        # Solve the problem using simulated annealing.
        start = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        annealing_time = time.time() - start
        print('Simulated annealing solution x: ' + str(annealing_solution)
              + '\tvalue: ' + str(p.value(annealing_solution))
              + '\ttime: ' + str(annealing_time)
              )
        if p.value(annealing_solution) > sa_max:
            sa_max = p.value(annealing_solution)

    print('---------------')
    print('Hill climbing final value: \t\t\t' + str(hill_max))
    print('Simulated annealing final value: \t' + str(sa_max))


