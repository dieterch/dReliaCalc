from reliability.Datasets import mileage
from reliability.Distributions import Normal_Distribution
from reliability.Reliability_testing import chi2test
import numpy as np

data = mileage().failures
dist = Normal_Distribution(mu=30011, sigma=10472)
# it is not necessary to specify the bins and leaving them unspecified is usually best
bins = [0, 13417, 18104, 22791, 27478, 32165, 36852, 41539, 46226, np.inf]
chi2test(distribution=dist, data=data, bins=bins)

'''
Chi-squared statistic: 3.1294947845652
Chi-squared critical value: 12.591587243743977
At the 0.05 significance level, we can ACCEPT the hypothesis that the data comes from a Normal Distribution (μ=30011,σ=10472)
'''
