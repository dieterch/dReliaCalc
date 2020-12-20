from reliability.Fitters import Fit_Everything
from reliability.Distributions import Weibull_Distribution
from reliability.Other_functions import make_right_censored_data

raw_data = Weibull_Distribution(alpha=12, beta=3).random_samples(
    100, seed=2)  # create some data
data = make_right_censored_data(
    raw_data, threshold=14)  # right censor the data
results = Fit_Everything(failures=data.failures,
                         right_censored=data.right_censored)  # fit all the models
print('The best fitting distribution was', results.best_distribution_name,
      'which had parameters', results.best_distribution.parameters)

'''
                  Alpha     Beta     Gamma       Mu     Sigma     Lambda        AICc         BIC         AD
Distribution
Weibull_2P      11.2773  3.30301                                          488.041154  493.127783  44.945028
Normal_2P                                   10.1194   3.37466             489.082213  494.168842  44.909765
Gamma_2P        1.42315  7.21352                                          490.593729  495.680358  45.281749
Loglogistic_2P  9.86245  4.48433                                          491.300512  496.387141  45.200181
Weibull_3P      10.0786  2.85825   1.15083                                489.807329  497.372839  44.992658
Gamma_3P        1.42315  7.21352         0                                492.720018  500.285528  45.281749
Lognormal_2P                                2.26524  0.406436             495.693518  500.780147  45.687381
Lognormal_3P                      0.883941  2.16125  0.465752             500.938298  500.780147  45.687381
Loglogistic_3P  9.86245  4.48433         0                                493.426801  500.992311  45.200181
Exponential_2P                     2.82802                      0.121869  538.150905  543.237534  51.777617
Exponential_1P                                                 0.0870022  594.033742  596.598095  56.866106

The best fitting distribution was Weibull_2P which had parameters [11.27730642  3.30300716  0.        ]
'''
