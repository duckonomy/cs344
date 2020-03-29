'''
@author: Ian Park, for CS344, Lab05
@version March 7, 2020
'''

from aima.probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20}),
    ])

# P(Cancer | positive results on both tests)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# P(Cancer | Test1 ∧ Test2) = alpha * <P(Cancer) * P(Test1 | Cancer) * P(Test2 | Cancer), P(¬Cancer) * P(Test1 | ¬Cancer) * P(Test2 | ¬Cancer)>
#                           = alpha * <0.9 * 0.9 * 0.01, 0.2 * 0.2 * 0.99>
#                           = alpha * <0.0081, 0.0396>
#                           = 1 / 0.0477 * <0.0081, 0.0396>
#                           = <0.1698, 0.8302>

# P(Cancer | a positive result on test 1, but a negative result on test 2)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
# P(Cancer | Test1 ∧ ¬Test2) = alpha * <P(Cancer) * P(Test1 | Cancer) * P(¬Test2 | Cancer), P(¬Cancer) * P(Test1 | ¬Cancer), P(¬Test2 | ¬Cancer)>
#                            = alpha * <0.01 * 0.9 * 0.1, 0.99 * 0.2 * 0.8>
#                            = alpha * <0.0009, 0.1584>
#                            = 1 / 0.1593 * <0.0009, 0.1584>
#                            = <0.006, 0.994>

'''
Q. Do the results make sense? How much effect does one failed test have on the probability of having cancer?
A. Yes, the results do make sense. Each test has much impact on the outcome.
   Since the tests have a high accuracy for people with cancer (0.9) and lower positive for those without (0.8),
   failing a test decreases the probability of one having cancer significantly.
'''
