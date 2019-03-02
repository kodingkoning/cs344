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
"""
By hand:
P(C | t1 and t2) = alpha * sum[P(Cancer, t1, t2)] = alpha * sum[ P(Cancer) * P(t1 | cancer) * P(t2 | cancer)] = alpha * <0.9*0.9*0.01, 0.2*0.2*0.99> = alpha * <0.0081, 0.0396> = 1/0.0477 * <0.0081, 0.0396> = <0.1698, 0.8302>
"""

# b. P(Cancer | a positive result on test 1, but a negative result on test 2)
print("b. " + enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
"""
By hand:
P(C | t1 and not t2) = alpha * sum[P(Cancer, t1, not t2)] = alpha * sum [ P(Cancer * P(t1 | cancer) * P(not t2 | cancer) ] = alpha * <0.01*0.9*0.1, 0.99*0.2*0.8> = alpha * <0.0009, 0.1584> = 1/0.1593 * <0.0009, 0.1584> = <0.006, 0.994>
"""

"""
These results make sense and they show that each test has a lot of power on the outcome. Because of a fairly high accuracy rate for people with cancer (0.9) and a lower positive result rate for people without cancer (0.8), one failed test is a good indicator that they do not have cancer. This also make sense with how few of the people have cancer. Because only 1% of those tested have cancer, that is a heavier weight on the outcome.
"""
