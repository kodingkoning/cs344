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
# P(Alarm | burglary ^ not earthquake) = <0.94, 1-0.94> = <0.94, 0.06>

# ii. P(John | burglary ∧ ¬earthquake)
print("ii. " + enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# for this, it makes sense to use enumeration (as we did in class)
# P(John | burglary ^ not earthquake) = alpha * sum P(J, a, b, not e) = alpha * sum[ P(J|a) * P(a|b, not e) * P(b) * P(not e)] = alpha * P(b) * P(not e) * sum[P(J|a) * P(a|b, not e)] = alpha * 0.001 * 0.998 * <0.9*0.94 + 0.05 * 0.06> = alpha * <0.000847, 0.000150698> = <0.85, 0.15>

# iii. P(Burglary | alarm)
print("iii. " + enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# this can be done with enumeration, with a diagnostic computation
# P(Burglary | alarm) = alpha * sum[ P(Burglary, alarm)] = alpha * sum[P(B) * P(e) * P(a|B, e)] = alpha * <0.001 * 0.002 * 0.95+0.001 * 0.998 * 0.94>, 0.999*0.002*0.29+0.999*0.998*0.001> = alpha * <0.00094002, 0.001576422> = <0.374, 0.626>

# iv. P(Burglary | john ∧ mary)
print("iv. " + enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# This one is more difficult to do by hand, but it can be done with an enumeration diagnostic computation. For that, we would have worked our way up the chart and found what probabilities of things are that could cause both of those calls.
