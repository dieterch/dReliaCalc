from reliability import Distributions
from reliability.Stress_strength import Probability_of_failure
import matplotlib.pyplot as plt

stress = Distributions.Weibull_Distribution(alpha=2, beta=3, gamma=1)
strength = Distributions.Gamma_Distribution(alpha=2, beta=3, gamma=3)
Probability_of_failure(stress=stress, strength=strength)
plt.show()

'''
Probability of failure: 0.0017078235941570912
'''
