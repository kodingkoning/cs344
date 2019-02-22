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
#TODO: figure out which things we need to import for the constraint satisfaction

courses = ["cs108", "cs112", "cs212", "cs214", "cs232", "cs262", "cs300"]
faculty = ["dschuurman", "adams", "vlinden", "hplantin", "pmb4"]
times = ["mwf900", "mwf1030", "mwf1130", "mwf1230", "mwf130"]
rooms = ["nh253", "sb382"]
# TODO: add constraints
assignments = {"cs108": "dschuurman", "cs112": "adams", "cs212":"hplantin", "cs214":"adams", "cs232":"pmb4", "cs262":"vlinden"}

# TODO: implement a solution with AIMA constraint satisfaction and explain why it works

class CourseScheduling(CSP):

    def __init__(self, courses, course_properties, neighbors, constraints):
        """
        :param courses: list of courses to assign
        :param domains: list of faculty, times, and rooms to assign to courses
        :param neighbors: pairs of
        :param constraints:
        NOTE: if any two courses have more than 1 common domain, then they break the constraint rule
        NOTE: need to show that
        """
        CSP.__init__(self, courses, course_properties, neighbors, constraints)

    def display(self, assignment):
        pass
        # TODO: print for debugging and result display

    # TODO: figure out what other methods we need
"""
TODO:
variables -- list of courses
domains -- dict of entries
neighbors -- pairs that have issues with constraints
constraints -- function that say if neighbors satisfy the constraints
"""
