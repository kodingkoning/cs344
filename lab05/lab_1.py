"""
CS 344: Lab 05
Elizabeth Koning, February 2019

Exercise 5.1
"""
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# i. P(Alarm | burglary ∧ ¬earthquake)
print("i. " + enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# this matches the results we pulled directly from the table during class

# ii. P(John | burglary ∧ ¬earthquake)
print("ii. " + enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# this matches the results we got when we did the problem by hand in class, considering the possibilities that John eithre calls because of an alarm (caused by a burglary, or independent of it) or just calls anyway

# iii. P(Burglary | alarm)
print("iii. " + enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# this can be done by hand by pulling values off the chart. If there has been an alarm, then we can normalize the possible combinations of burglary and earthquake that led to that

# iv. P(Burglary | john ∧ mary)
print("iv. " + enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# this can also be found by going up the chart, like we did for the probability of an alarm given a burglary but not an earthquake
