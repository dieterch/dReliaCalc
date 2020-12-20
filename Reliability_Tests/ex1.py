from reliability.Distributions import Weibull_Distribution
from reliability.Fitters import Fit_Weibull_2P
from reliability.Probability_plotting import plot_points
import matplotlib.pyplot as plt

# creates the distribution object
dist = Weibull_Distribution(alpha=30, beta=2)
# draws 20 samples from the distribution. Seeded for repeatability
data = dist.random_samples(20, seed=42)
plt.subplot(121)
# fits a Weibull distribution to the data and generates the probability plot
fit = Fit_Weibull_2P(failures=data)
plt.subplot(122)
# uses the distribution object from Fit_Weibull_2P and plots the survival function
fit.distribution.SF(label='fitted distribution')
# plots the survival function of the original distribution
dist.SF(label='original distribution', linestyle='--')
# overlays the original data on the survival function
plot_points(failures=data, func='SF')
plt.legend()
plt.show()
