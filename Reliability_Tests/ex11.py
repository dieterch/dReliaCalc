from reliability.Distributions import Weibull_Distribution
from reliability.Fitters import Fit_Weibull_2P
from reliability.Other_functions import crosshairs
import matplotlib.pyplot as plt

dist = Weibull_Distribution(alpha=500, beta=6)
data = dist.random_samples(50, seed=1)  # generate some data
# this will produce the large table of percentiles below the first table of results
Fit_Weibull_2P(failures=data, percentiles=True,
               CI=0.8, show_probability_plot=False)
print('----------------------------------------------------------')
# repeat the process but using specified percentiles.
output = Fit_Weibull_2P(failures=data, percentiles=[5, 50, 95], CI=0.8)
# these points have been manually annotated on the plot using crosshairs
crosshairs()
plt.show()

# the values from the percentiles dataframe can be extracted as follows:
lower_estimates = output.percentiles['Lower Estimate'].values
print('\nLower estimates:', lower_estimates)

'''
Results from Fit_Weibull_2P (80% CI):
           Point Estimate  Standard Error    Lower CI    Upper CI
Parameter
Alpha          489.117377       13.921709  471.597466  507.288155
Beta             5.207995        0.589270    4.505014    6.020673
Log-Likelihood: -301.6579198472162

Table of percentiles (80% CI bounds on time):
            Lower Estimate  Point Estimate  Upper Estimate
Percentile
1               175.215220      202.211975      233.368328
5               250.234954      276.521341      305.569030
10              292.686602      317.508291      344.435017
20              344.277189      366.718796      390.623252
25              363.578675      385.050426      407.790228
50              437.690233      455.879011      474.823648
75              502.940450      520.776175      539.244407
80              517.547404      535.916489      554.937539
90              553.266964      574.067575      595.650206
95              580.174021      603.820155      628.430033
99              625.681232      655.789604      687.346819
----------------------------------------------------------
Results from Fit_Weibull_2P (80% CI):
           Point Estimate  Standard Error    Lower CI    Upper CI
Parameter
Alpha          489.117377       13.921709  471.597466  507.288155
Beta             5.207995        0.589270    4.505014    6.020673
Log-Likelihood: -301.6579198472162

Table of percentiles (80% CI bounds on time):
            Lower Estimate  Point Estimate  Upper Estimate
Percentile
5               250.234954      276.521341      305.569030
50              437.690233      455.879011      474.823648
95              580.174021      603.820155      628.430033

Lower estimates: [250.23495375 437.69023325 580.17402096]
'''
