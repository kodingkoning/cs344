"""
Run a local search on the course scheduling problem

Elizabeth Koning, for CS344, February 2019
"""

from csp import min_conflicts, CSP, parse_neighbors

courses = ['cs108', 'cs112', 'cs212', 'cs214', 'cs232', 'cs262', 'cs300']
faculty = ['dschuurman', 'adams', 'vlinden', 'hplantin', 'pmb4']
times = ['mwf900', 'mwf1030', 'mwf1130', 'mwf1230', 'mwf130']
rooms = ['nh253', 'sb382']
# TODO: add constraints
assignments = {'cs108': 'dschuurman', 'cs112': 'adams', 'cs212':'hplantin', 'cs214':'adams', 'cs232':'pmb4', 'cs262':'vlinden', 'cs300':'vlinden'}
# neighbors = all combinations of classes
num_courses = len(courses)

# neighbors = []
# list all pairs of courses
# does not include pairing courses with themselves or pairs that are the same in the other order
# TODO: make a function for this
neighbors_string = ""
for i in range(num_courses):
    for j in range(num_courses-i-1):
        course1 = courses[i]
        course2 = courses[num_courses-j-1]
        neighbors_string += course1 + ":" + course2 + ";"
        # neighbors.append([course1, course2])

neighbors_string = neighbors_string[:-1] # get rid of the last semicolon
neighbors = parse_neighbors(neighbors_string, variables=courses)

PROF = 0
TIME = 1
ROOM = 2

def scheduling_constraints(courseA, variableA, courseB, variableB):
    # TODO: fill this in with requirements
    """
    if the courses have the same room, same time, that doesn't work
    if the courses have the same prof, same time, that doesn't work
    if the courses have the wrong prof, that doesn't work (check assignments list)
    each course need a faculty member, time, and room
    """

    # variables are formatted as [prof, time, room]

    # check if they are in the same room or with the same faculty member at the same time
    if variableA[TIME] == variableB[TIME] and (variableA[ROOM] == variableB[ROOM] or variableA[PROF] == variableB[PROF]):
        return False

    # check that each course is with the correct professor
    if variableA[PROF] != assignments[courseA] or variableB[PROF] != assignments[courseB]:
        return False

    return True

domains = {}
for course in courses:
    domains[course] = []
    for prof in faculty:
        for time in times:
            for room in rooms:
                domains[course].append( [prof, time, room] )



result = min_conflicts(CSP(courses, domains, neighbors, scheduling_constraints))
print(result)


# TODO: implement a solution with AIMA constraint satisfaction and explain why it works

# class CourseScheduling(CSP):
#
#     def __init__(self, courses, course_properties, neighbors, constraints):
#         """
#         :param courses: list of courses to assign
#         :param domains: list of faculty, times, and rooms to assign to courses
#         :param neighbors: pairs of
#         :param constraints:
#         NOTE: if any two courses have more than 1 common domain, then they break the constraint rule
#         NOTE: need to show that
#         """
#         CSP.__init__(self, courses, course_properties, neighbors, constraints)
#
#     def display(self, assignment):
#         pass
#         # TODO: print for debugging and result display
#
#     # TODO: figure out what other methods we need


# define a function that compares all the classes and says if they break rules.
# neighbors -- all combinations of classes


"""
TODO:
variables -- list of courses
domains -- dict of entries
neighbors -- pairs that have issues with constraints
constraints -- function that say if neighbors satisfy the constraints
"""

"""
have the classes be the variables
min_conflicts(CSP(courses, domains, neighbors, different_faculty_slot_constraint))
where domains are all possible combinations of times, assignments, rooms, ...
Make sure that either that there aren't too many similarities
Have to check every pair of classes that they are okay
constraints -- the variable class, has the value [prof, room, time] and compare with another class
"""
