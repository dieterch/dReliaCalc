from reliability.Fitters import Fit_Weibull_Mixture
from reliability.Distributions import Weibull_Distribution
from reliability.Other_functions import histogram
import numpy as np
import matplotlib.pyplot as plt

# create some failures from two distributions
group_1 = Weibull_Distribution(alpha=10, beta=3).random_samples(40, seed=2)
group_2 = Weibull_Distribution(alpha=40, beta=4).random_samples(60, seed=2)
all_data = np.hstack([group_1, group_2])  # combine the data
results = Fit_Weibull_Mixture(failures=all_data)  # fit the mixture model

# this section is to visualise the histogram with PDF and CDF
# it is not part of the default output from the Fitter
plt.figure(figsize=(9, 5))
plt.subplot(121)
histogram(all_data)
results.distribution.PDF()
plt.subplot(122)
histogram(all_data, cumulative=True)
results.distribution.CDF()

plt.show()

'''
Results from Fit_Weibull_Mixture (95% CI):
              Point Estimate  Standard Error   Lower CI   Upper CI
Parameter
Alpha 1             8.654923        0.394078   7.916006   9.462815
Beta 1              3.910594        0.509724   3.028959   5.048845
Alpha 2            38.097040        1.411773  35.428112  40.967028
Beta 2              3.818227        0.421366   3.075574   4.740207
Proportion 1        0.388206        0.050264   0.295325   0.489987
Log-Likelihood: -375.9906311550037
'''
