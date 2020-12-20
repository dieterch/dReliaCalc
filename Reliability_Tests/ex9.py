from reliability.Distributions import Weibull_Distribution
from reliability.Fitters import Fit_Weibull_3P
from reliability.Other_functions import make_right_censored_data, histogram
import matplotlib.pyplot as plt

a = 30
b = 2
g = 20
threshold = 55
# generate a weibull distribution
dist = Weibull_Distribution(alpha=a, beta=b, gamma=g)
# create some data from the distribution
raw_data = dist.random_samples(500, seed=2)
# right censor some of the data
data = make_right_censored_data(raw_data, threshold=threshold)
print('There are', len(data.right_censored), 'right censored items.')
wbf = Fit_Weibull_3P(failures=data.failures, right_censored=data.right_censored,
                     show_probability_plot=False, print_results=False)  # fit the Weibull_3P distribution
print('Fit_Weibull_3P parameters:\nAlpha:', wbf.alpha,
      '\nBeta:', wbf.beta, '\nGamma', wbf.gamma)
# generates the histogram using optimal bin width and shades the censored part as white
histogram(raw_data, white_above=threshold)
dist.PDF(label='True Distribution')  # plots the true distribution's PDF
# plots to PDF of the fitted Weibull_3P
wbf.distribution.PDF(label='Fit_Weibull_3P', linestyle='--')
plt.title('Fitting comparison for failures and right censored data')
plt.legend()
plt.show()

'''
There are 118 right censored items.
Fit_Weibull_3P parameters:
Alpha: 28.87483648004299
Beta: 2.0295019039127347
Gamma 20.383900235710296
'''
