from reliability.Fitters import Fit_Weibull_2P
import matplotlib.pyplot as plt
data = [58, 75, 36, 52, 63, 65, 22, 17, 28, 64, 23, 40, 73, 45, 52, 36, 52, 60, 13, 55, 82,
        55, 34, 57, 23, 42, 66, 35, 34, 25]  # made using Weibull Distribution(alpha=50,beta=3)
wb = Fit_Weibull_2P(failures=data)
plt.show()

'''
Results from Fit_Weibull_2P (95% CI):
           Point Estimate  Standard Error   Lower CI   Upper CI
Parameter
Alpha           51.857992        3.556283  45.335934  59.318317
Beta             2.800861        0.414110   2.096238   3.742333
Log-Likelihood: -129.0626756550746
'''
