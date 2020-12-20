from reliability.Distributions import Exponential_Distribution
from reliability.Probability_plotting import Exponential_probability_plot
import matplotlib.pyplot as plt
from reliability.Other_functions import make_right_censored_data

dist = Exponential_Distribution(Lambda=0.25, gamma=12)
# draw some random data from an exponential distribution
raw_data = dist.random_samples(100, seed=42)
# right censor the data at 17
data = make_right_censored_data(raw_data, threshold=17)
# we can't plot dist because it will be location shifted
Exponential_Distribution(Lambda=0.25).CDF(linestyle='--', label='True CDF')
# do the probability plot. Note that we have specified to fit gamma
Exponential_probability_plot(
    failures=data.failures, right_censored=data.right_censored, fit_gamma=True)
plt.legend()
plt.show()
