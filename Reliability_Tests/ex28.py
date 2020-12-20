from reliability.Probability_plotting import QQ_plot_semiparametric
from reliability.Fitters import Fit_Weibull_2P
from reliability.Distributions import Normal_Distribution
import matplotlib.pyplot as plt
data = Normal_Distribution(mu=50, sigma=12).random_samples(100)
fitted_dist = Fit_Weibull_2P(
    failures=data, print_results=False, show_probability_plot=False).distribution
QQ_plot_semiparametric(X_data_failures=data, Y_dist=fitted_dist)
plt.show()
