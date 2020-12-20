from reliability.Other_functions import crosshairs
from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt

Weibull_Distribution(alpha=50, beta=2).CDF()
crosshairs(xlabel='t', ylabel='F')  # it is important to call this last
plt.show()
