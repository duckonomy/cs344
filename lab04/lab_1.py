'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@modified: Ian Park
@version Feb 29, 2020
'''

from aima.probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Hand Calculation
## P(Cavity | Toothache) = (P(Toothache | Cavity) P(Cavity)) / P(Toothache)
## = P(Cavity and Toothache) / P(Toothache)
## = (0.108 + 0.012) / (0.108 + 0.012 + 0.016 + 0.064)
## = 0.6

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print("P(Cavity | Toothache): " + PC.show_approx())

# Hand Calculation
## P(Cavity | Catch) = (P(Catch | Cavity) P(Cavity)) / P(Catch)
## = P(Cavity and Catch) / P(Catch) = (0.108 + 0.072) / (0.108 + 0.016 + 0.072 + 0.144)
## = 0.5294

# Verification
# Compute P(Cavity|Catch=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print("P(Cavity | Catch): " + PC.show_approx())

# Result: False: 0.471, True: 0.529

# Make the prob dist for a fair coin
P = JointProbDist(['Coin1', 'Coin2'])
H, T = True, False
P[H, T] = 0.25; P[H, H] = 0.25
P[T, H] = 0.25; P[T, T] = 0.25

PC = enumerate_joint_ask('Coin2', {'Coin1': H}, P)
print("P(Coin2|Coin1): ", PC.show_approx())

# Result: False: 0.5, True: 0.5

"""
Q. Does the answer confirm what you believe to be true about the probabilities of flipping coins? Can you see now why the full joint is generally not used in probabilistic systems?
A. Yes. Since the two events are independent events, they do not affect the outcome of the other. So, the  the probability of each flib is 0.5. Yes.
"""
