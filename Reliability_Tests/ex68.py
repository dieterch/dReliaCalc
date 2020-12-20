from reliability.Distributions import Weibull_Distribution
from reliability.Other_functions import similar_distributions
dist = Weibull_Distribution(alpha=50, beta=3.3)
similar_distributions(distribution=dist, include_location_shifted=False)

'''
The input distribution was:
Weibull Distribution (α=50,β=3.3)

The top 3 most similar distributions are:
Normal Distribution (μ=44.8471,σ=14.9226)
Gamma Distribution (α=5.7607,β=7.7849)
Loglogistic Distribution (α=43.465,β=4.7564)
'''
