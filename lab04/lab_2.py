'''
Lab 04 Exercise 4.2

@author: Ian Park
@version Feb 29, 2020
'''

from aima.probability import JointProbDist, enumerate_joint_ask

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

# Compute P(Toothache|Rain=T)  (see the text, page 493).
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())

"""
Q. How many entries does your full joint probability distribution contain now?
A. 16 entries.
"""

"""
Q. Do the probabilities sum up to 1.0? Should they? Explain why or why not.
A. Yes. Although the variables are adjusted (halfed), the probabilities must still add up to 1 by definition.
"""

"""
Q. Did you think that you can use anything other than T or F values for the values for the random variables? Explain why or why not.
A. It wouldn't be necessary for this problem. So, I just went with T/F.
"""

"""
Q. Did the probabilities you chose indicate that the value of Rain is independent of the original values?
A. Yes. This is testable by using stuff in lab_1.py to check.

     PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
     print("P(Cavity | Toothache): " + PC.show_approx())

   This yields the same values (i.e. 0.6/0.4)
"""

"""
Hand Calculation:
P(Toothache | Rain) = P(Toothache and Rain) / P(Rain)
                    = (0.054 + 0.006 + 0.008 + 0.032) / (0.054 + 0.006 + 0.036 + 0.004 + 0.008 + 0.032 + 0.072 + 0.288)
                    = 0.1 / 0.5
                    = 0.2
"""
