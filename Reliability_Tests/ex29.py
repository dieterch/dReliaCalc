from reliability.Probability_plotting import QQ_plot_parametric, PP_plot_parametric
from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt
Field = Weibull_Distribution(alpha=350, beta=2.01)
Lab = Weibull_Distribution(alpha=128, beta=2.11)
plt.figure(figsize=(10, 5))
plt.subplot(121)
QQ_plot_parametric(X_dist=Lab, Y_dist=Field,
                   show_diagonal_line=True, show_fitted_lines=False)
plt.subplot(122)
PP_plot_parametric(X_dist=Lab, Y_dist=Field, show_diagonal_line=True)
plt.show()
