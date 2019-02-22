"""
Run a local search on the course scheduling problem

Elizabeth Koning, for CS344, February 2019
"""

from csp import min_conflicts, CSP, parse_neighbors


# constants for keeping track of order of faculty, time and room in variable lists
PROF = 0
TIME = 1
ROOM = 2

courses = ['cs108', 'cs112', 'cs212', 'cs214', 'cs232', 'cs262', 'cs300']
faculty = ['dschuurman', 'adams', 'vlinden', 'hplantin', 'pmb4']
times = ['mwf900', 'mwf1030', 'mwf1130', 'mwf1230', 'mwf130']
rooms = ['nh253', 'sb382']
assignments = {'cs108': 'dschuurman', 'cs112': 'adams', 'cs212':'hplantin', 'cs214':'adams', 'cs232':'pmb4', 'cs262':'vlinden', 'cs300':'vlinden'}
num_courses = len(courses)

# neighbors: list all pairs of courses in the format needed for parse_neighbors
# does not include pairing courses with themselves or pairs that are the same in the other order
neighbors_string = ""
for i in range(num_courses):
    for j in range(num_courses-i-1):
        course1 = courses[i]
        course2 = courses[num_courses-j-1]
        neighbors_string += course1 + ":" + course2 + ";"

neighbors_string = neighbors_string[:-1] # get rid of the last semicolon
neighbors = parse_neighbors(neighbors_string, variables=courses)

# list all teaching combinations (of faculty, time, and room) that could be assigned to a course
domains = {}
for course in courses:
    domains[course] = []
    for prof in faculty:
        for time in times:
            for room in rooms:
                domains[course].append( [prof, time, room] )


# return whether the pair of courses do not conflict
def scheduling_constraints(courseA, variableA, courseB, variableB):
    """
    if the courses have the same room, same time, that fails the requirements
    if the courses have the same prof, same time, that fails the requirements
    if the courses have the wrong prof, that also fails the requirements
    """

    # check if they are in the same room or with the same faculty member at the same time
    if variableA[TIME] == variableB[TIME] and (variableA[ROOM] == variableB[ROOM] or variableA[PROF] == variableB[PROF]):
        return False

    # check that each course is with the correct professor
    if variableA[PROF] != assignments[courseA] or variableB[PROF] != assignments[courseB]:
        return False

    # if it didn't fail yet, it's valid
    return True


result = min_conflicts(CSP(courses, domains, neighbors, scheduling_constraints))
print(result)

"""
An explanation of the reasoning of this solution should start at the end. Because of the requirements, the min_conflicts function and the CSP class are necessary components of the solution. To decide how to go about filling the requirements of the CSP class constructor, I looked at the Sudoku, Queens, and Zebra problems. The Sudoku was a particularly helpful one. The Zebra problem wsa confusing because of documentation issues, and the queens problem sent me down the wrong track with building a subclass of CSP.
Making the list of requirements was very straightforward from the problem description.
From there, the problem got more complicated to approach. It make sense to have the courses be the variables because they are fixed and the other parameters need to be assigned to them.
Once we were told that it worked to make all the combinations of faculty, time, and room domains, the rest of it could use strategies from the Zebra problem, but actually simpler.

As you can see by running the code, this solution works and gives a schedule that fills the requirements.
"""
