from reliability.Probability_plotting import PP_plot_semiparametric
from reliability.Fitters import Fit_Normal_2P
from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt
data = Weibull_Distribution(alpha=5, beta=3).random_samples(100)
dist = Fit_Normal_2P(failures=data, show_probability_plot=False,
                     print_results=False).distribution
PP_plot_semiparametric(X_data_failures=data, Y_dist=dist)
plt.show()
