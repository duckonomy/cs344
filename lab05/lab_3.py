'''
@author: Ian Park, for CS344, Lab05
@version March 7, 2020
'''

from aima.probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

happiness = BayesNet([
    ('Sunny', '', 0.70),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
    ])

# P(Raise | Sunny)
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
# P(Raise | Sunny) = alpha * <P(Raise) * P(Sunny), P(¬Raise) * P(Sunny)>
#                  = alpha * P(Sunny) * <0.01, 0.99>
#                  = <0.01, 0.99>
# The probability of raise does not depend on sunny. So, since we have the probability of a raise, we can easily find the probability.

# P(Raise | Happy ∧ Sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())
# P(Raise | Happy ∧ Sunny) = alpha * <P(Raise) * P(Sunny) * P(Happy | Sunny ∧ Raise), P(¬Raise) * P(Sunny) * P(Happy | Sunny ∧ ¬Raise)>
#                          = alpha * <0.01 * 0.7 * 1.0, 0.99 * 0.7 * 0.9>
#                          = 1 / 0.6307 * <0.007, 0.6237>
#                          = <0.011, 0.989>
# Since happiness depends on sunny and raise, being both happy and true increases the probabilty of there being a raise.

# P(Raise | Happy)
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
# P(Raise | Happy ∧ ¬Sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())

'''
Q. Do these results make sense to you? Why or why not?
A. a.i and a.ii both make sense as I explained above. b.i makes sense since
   being happy implies that either sunny or raise is true. So, the probability
   of a raise is slightly bumped up. However, since getting a raise itself is not
   that likely, it still has a pretty low probability of being true. b.ii also makes
   sense because we are looking at possibilities where sunny is false and the person
   is either just randomly happy or happy from getting a raise. This would be even
   lower.
'''
