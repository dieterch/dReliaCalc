from reliability.Probability_plotting import QQ_plot_parametric
from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt
Field = Weibull_Distribution(alpha=350, beta=2.01)
Lab = Weibull_Distribution(alpha=128, beta=2.11)
QQ_plot_parametric(X_dist=Lab, Y_dist=Field)
plt.show()
