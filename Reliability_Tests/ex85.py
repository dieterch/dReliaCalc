from reliability.Datasets import mileage
from reliability.Distributions import Normal_Distribution
from reliability.Reliability_testing import KStest

data = mileage().failures
dist = Normal_Distribution(mu=30011, sigma=10472)
KStest(distribution=dist, data=data)

'''
Kolmogorov-Smirnov statistic: 0.07162465859560846
Kolmogorov-Smirnov critical value: 0.13402791648569978
At the 0.05 significance level, we can ACCEPT the hypothesis that the data comes from a Normal Distribution (μ=30011,σ=10472)
'''
