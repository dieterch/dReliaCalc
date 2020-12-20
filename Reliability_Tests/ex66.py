from reliability.ALT_fitters import Fit_Weibull_Power
from reliability.Datasets import ALT_load2
import matplotlib.pyplot as plt
data = ALT_load2()
Fit_Weibull_Power(failures=data.failures, failure_stress=data.failure_stresses,
                  right_censored=data.right_censored, right_censored_stress=data.right_censored_stresses, use_level_stress=60)
plt.show()

'''
Results from Fit_Weibull_Power (95% CI):
           Point Estimate  Standard Error       Lower CI      Upper CI
Parameter
a           398816.331485   519397.960450 -619184.964641  1.416818e+06
n               -1.417306        0.243944      -1.895428 -9.391834e-01
beta             3.017297        0.716426       1.894563  4.805374e+00
At the use level stress of 60 , the mean life is 1075.32845
'''
