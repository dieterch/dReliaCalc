from reliability.Distributions import Weibull_Distribution
from reliability.Fitters import Fit_Weibull_2P
from reliability.Nonparametric import KaplanMeier
from reliability.Other_functions import make_right_censored_data
import matplotlib.pyplot as plt

dist = Weibull_Distribution(alpha=5, beta=2)  # create a distribution
# get some data from the distribution. Seeded for repeatability
raw_data = dist.random_samples(100, seed=2)
data = make_right_censored_data(raw_data, threshold=9)
wbf = Fit_Weibull_2P(failures=data.failures, right_censored=data.right_censored,
                     show_probability_plot=False, print_results=False)  # Fit the Weibull_2P

# Create the subplots and in each subplot we will plot the parametric distribution and obtain the Kaplan Meier fit.
# Note that the plot_type is being changed each time
plt.figure(figsize=(12, 5))
plt.subplot(131)
KaplanMeier(failures=data.failures, right_censored=data.right_censored,
            plot_type='SF', print_results=False, label='Kaplan-Meier')
wbf.distribution.SF(label='Parametric')
plt.legend()
plt.title('SF')
plt.subplot(132)
KaplanMeier(failures=data.failures, right_censored=data.right_censored,
            plot_type='CDF', print_results=False, label='Kaplan-Meier')
wbf.distribution.CDF(label='Parametric')
plt.legend()
plt.title('CDF')
plt.subplot(133)
KaplanMeier(failures=data.failures, right_censored=data.right_censored,
            plot_type='CHF', print_results=False, label='Kaplan-Meier')
wbf.distribution.CHF(label='Parametric')
plt.legend()
plt.title('CHF')
plt.subplots_adjust(left=0.07, right=0.95, top=0.92,
                    wspace=0.25)  # format the plot layout
plt.show()
