"""
CS 344: Lab 05
Elizabeth Koning, February 2019

Exercise 5.2
"""

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2}),
    ])

# a. P(Cancer | positive results on both tests)
print("a. " + enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# b. P(Cancer | a positive result on test 1, but a negative result on test 2)
print("b. " + enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

"""
These results make sense and they show that each test has a lot of power on the outcome. Because of a fairly high accuracy rate for people with cancer (0.9) and a lower positive result rate for people without cancer (0.8), one failed test is a good indicator that they do not have cancer. This also make sense with how few of the people have cancer. Because only 1% of those tested have cancer, that is a heavier weight on the outcome.
"""