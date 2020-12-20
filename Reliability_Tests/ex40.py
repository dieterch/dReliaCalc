from reliability import Distributions
from reliability.Stress_strength import Probability_of_failure_normdist
import matplotlib.pyplot as plt

stress = Distributions.Normal_Distribution(mu=20, sigma=6)
strength = Distributions.Normal_Distribution(mu=40, sigma=7)
Probability_of_failure_normdist(stress=stress, strength=strength)
plt.show()

'''
Probability of failure: 0.015029783946206214
'''
