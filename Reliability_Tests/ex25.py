from reliability.Probability_plotting import Weibull_probability_plot
from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt
import numpy as np

dist_1 = Weibull_Distribution(alpha=200, beta=3)
dist_2 = Weibull_Distribution(alpha=900, beta=4)
plt.subplot(121)  # this is for the PDFs of the 2 individual distributions
dist_1.PDF(label=dist_1.param_title_long)
dist_2.PDF(label=dist_2.param_title_long)
plt.legend()
plt.title(
    'PDF of two different distributions\nthat are contributing the failure data')
plt.subplot(122)  # this will be the probability plot
dist_1_data = dist_1.random_samples(50, seed=1)
dist_2_data = dist_2.random_samples(50, seed=1)
# combine the failure data into one array
all_data = np.hstack([dist_1_data, dist_2_data])
# plot each individual distribution for comparison
dist_1.CDF(label=dist_1.param_title_long)
dist_2.CDF(label=dist_2.param_title_long)
Weibull_probability_plot(failures=all_data)  # do the probability plot
# adjust the figuresize after creation. Necessary to do it after as it it automatically ajdusted within probability_plot
plt.gcf().set_size_inches(13, 7)
plt.subplots_adjust(left=0.08, right=0.96)  # formatting the layout
plt.legend()
plt.show()
