"""
CS 344 Lab 04
Exercise 1

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
ii. code below, which agrees with my hand-calculated version
"""

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

"""
1 (cont)
c.
"""
P_coins = JointProbDist(["coin1", "coin2"])
H, T = True, False
P_coins[H, T] = 1/4;
P_coins[T, T] = 1/4;
P_coins[T, H] = 1/4;
P_coins[H, H] = 1/4;

PH = enumerate_joint_ask('coin2', {'coin1': H}, P_coins)
print(PH.show_approx())

"""
1c (cont)
This answer does confirm what I already knew about flipping coins. I also know see why the full joint is generally not used. This means a lot of extra work for a very straightforward problem, at least in this case.
"""