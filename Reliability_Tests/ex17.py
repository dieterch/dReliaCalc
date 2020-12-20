from reliability.Fitters import Fit_Weibull_Mixture, Fit_Weibull_2P
from reliability.Distributions import Weibull_Distribution
from reliability.Other_functions import histogram, make_right_censored_data
import numpy as np
import matplotlib.pyplot as plt

# create some failures and right censored data
group_1 = Weibull_Distribution(alpha=10, beta=2).random_samples(700, seed=2)
group_2 = Weibull_Distribution(alpha=30, beta=3).random_samples(300, seed=2)
all_data = np.hstack([group_1, group_2])
data = make_right_censored_data(all_data, threshold=30)

# fit the Weibull Mixture and Weibull_2P
mixture = Fit_Weibull_Mixture(failures=data.failures, right_censored=data.right_censored,
                              show_probability_plot=False, print_results=False)
single = Fit_Weibull_2P(failures=data.failures, right_censored=data.right_censored,
                        show_probability_plot=False, print_results=False)
print('Weibull_Mixture BIC:', mixture.BIC, '\nWeibull_2P BIC:',
      single.BIC)  # print the goodness of fit measure

# plot the Mixture and Weibull_2P
histogram(all_data, white_above=30)
mixture.distribution.PDF(label='Weibull Mixture')
single.distribution.PDF(label='Weibull_2P')
plt.title('Comparison of Weibull_2P with Weibull Mixture')
plt.legend()
plt.show()

'''
Weibull_Mixture BIC: 6432.417425636481
Weibull_2P BIC: 6511.51175959736
'''
