from reliability.Probability_plotting import PP_plot_semiparametric, QQ_plot_semiparametric
from reliability.Fitters import Fit_Normal_2P
from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt
data = Weibull_Distribution(
    alpha=100, beta=3).random_samples(100)  # create some data
dist = Fit_Normal_2P(failures=data, print_results=False,
                     show_probability_plot=False).distribution  # fit a normal distribution
plt.figure(figsize=(10, 5))
plt.subplot(121)
QQ_plot_semiparametric(X_data_failures=data, Y_dist=dist,
                       show_fitted_lines=False, show_diagonal_line=True)
plt.subplot(122)
PP_plot_semiparametric(X_data_failures=data, Y_dist=dist)
plt.show()
