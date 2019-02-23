"""
CS 344 Lab 04
Exercise 2

Elizabeth Koning -- February 22, 2019
"""

from probability import JointProbDist, enumerate_joint_ask

"""
Excersie 2a

"""

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288
P[T, T, T, F] = 0.027; P[T, T, F, F] = 0.006
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288

"""
i. The full joing probability distribution now contains 16 entries, or twice as many as it did before.
ii. Yes, the probabilities sum to 1. I adjusted them all so that the sum would still come to 1. This should be the case because one of these outcomes must be the case, and the probability of having an outcome (any, not a specific one) can't be higher or lower than one.
iii. I used T and F for this because it matched with the other variables. I could have added more names for True and False, but T and F fit well here, so I kept them.
iv. Yes, I just divided all the probabilities by 2 and so the other variables and Rain should be independent.
"""

"""
Exercise 2b

pencil and paper version:
P(Toothache|Rain) = P(Toothache ^ Rain) / P(Rain) = (0.054+0.006+0.008+0.032) / 0.5 = 0.2
distribution: True: 0.2, False: 0.8

code version:
"""

# Compute P(Toothache|Rain=T)  (see the text, page 493).
TR = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(TR.show_approx())
