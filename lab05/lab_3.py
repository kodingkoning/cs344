"""
CS 344: Lab 05
Elizabeth Koning, February 2019

Exercise 5.3
"""

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

weather = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
    ])

# a. P(Cancer | positive results on both tests)
print("a.")
print("i. " + enumeration_ask('Raise', dict(Sunny=T), weather).show_approx())
print("ii. " + enumeration_ask('Raise', dict(Happy=T, Sunny=T), weather).show_approx())

# b. P(Cancer | a positive result on test 1, but a negative result on test 2)
print("b.")
print("i. " + enumeration_ask('Raise', dict(Happy=T), weather).show_approx())
print("ii. " + enumeration_ask('Raise', dict(Happy=T, Sunny=F), weather).show_approx())

"""
These results make sense. For the less obvious ones (the two of part b), we again have cases where the rarity of getting a raise becomes a factor. Because raises aren't very common, it makes sense that even if we know the agent is happy (which may be because of a raise), it doesn't lead to a very high probability that they received a raise. However, if it isn't sunny, then we can see that the conditional probabilities are much more skewed. But because of the rarity of raises, it's still more likely that it's the case where the probability of being happy is 0.1 and sunny and raise are both false.
"""
