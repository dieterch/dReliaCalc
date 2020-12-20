from reliability.Distributions import Weibull_Distribution, Competing_Risks_Model
from reliability.Fitters import Fit_Weibull_CR
from reliability.Other_functions import histogram
import matplotlib.pyplot as plt

# create some data that requires a competing risks models
d1 = Weibull_Distribution(alpha=50, beta=2)
d2 = Weibull_Distribution(alpha=40, beta=10)
CR_model = Competing_Risks_Model(distributions=[d1, d2])
data = CR_model.random_samples(100, seed=2)

# fit the Weibull competing risks model
results = Fit_Weibull_CR(failures=data)

# this section is to visualise the histogram with PDF and CDF
# it is not part of the default output from the Fitter
plt.figure(figsize=(9, 5))
plt.subplot(121)
histogram(data)
results.distribution.PDF()
plt.subplot(122)
histogram(data, cumulative=True)
results.distribution.CDF()

plt.show()

'''
Results from Fit_Weibull_CR (95% CI):
           Point Estimate  Standard Error   Lower CI   Upper CI
Parameter
Alpha 1         55.185550       14.385243  33.108711  91.983192
Beta 1           1.896577        0.454578   1.185637   3.033816
Alpha 2         38.192099        1.083595  36.126262  40.376067
Beta 2           7.978213        1.181428   5.968403  10.664810
Log-Likelihood: -352.47978488894165
'''
