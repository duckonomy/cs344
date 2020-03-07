'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@modified by: Ian Park, for CS344, Lab05
@version March 7, 2020
'''

from aima.probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

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

# P(Alarm | burglary ∧ ¬earthquake)
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# P(John | burglary ∧ ¬earthquake)
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# P(Burglary | alarm)
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# P(Burglary | john ∧ mary)
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

'''
Q. Do the results match those of the exact inference algorithms? Why or why not?
A. No, the results do not match those of the exact inference algorithms.
   This is primarily because they are not using sampling data rather
   than doing actual calculations (like you would with hand computation).
   By doing so, the approximate inference algorithms decrease computational
   runtime while giving a close results.
'''
