from reliability.Datasets import automotive
from reliability.Fitters import Fit_Weibull_2P
Fit_Weibull_2P(failures=automotive().failures, right_censored=automotive(
).right_censored, show_probability_plot=True)

'''
Results from Fit_Weibull_2P (95% CI):
           Point Estimate  Standard Error      Lower CI       Upper CI
Parameter
Alpha       140882.303527    49299.609699  70956.382925  279718.647273
Beta             1.132769        0.301468      0.672370       1.908422
Log-Likelihood: -128.98350896528038
'''
