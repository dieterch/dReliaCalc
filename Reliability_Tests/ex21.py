from reliability.Distributions import Normal_Distribution
from reliability.Probability_plotting import Normal_probability_plot
import matplotlib.pyplot as plt

dist = Normal_Distribution(mu=50, sigma=10)
failures = dist.random_samples(100, seed=5)
Normal_probability_plot(failures=failures)  # generates the probability plot
# this is the actual distribution provided for comparison
dist.CDF(linestyle='--', label='True CDF')
plt.legend()
plt.show()
