"""
CS 344 Lab 4

Elizabeth Koning -- February 22, 2019
"""

from probability import JointProbDist, enumerate_joint_ask

"""
Exercise 4.1

a.
joint.py computes the probability distrubtion for Cavity, given that toothache = True. It computes this by using the AIMA class that allows it to calculate the conditional probability from the table. In this case, it would do that by (P being the probability, ProbDist being the distribution):
P(Cavity|toothache) = P(Cavity ^ toothache) / P(toothache) = (0.108+0.012)/(0.108+0.012+0.016+0.064)
Therefore, the distribution is as the code outputs, with False: 0.4, True: 0.6 

b.
i. P(Cavity|catch) = P(Cavity ^ catch) / P(catch) = (0.108+0.072) / (0.108+0.016+0.072+0.144) = 0.529
So the distribution is: True: 0.529, False: 0.471
ii. code below
"""



