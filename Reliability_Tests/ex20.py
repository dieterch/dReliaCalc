from reliability.Distributions import Weibull_Distribution, Competing_Risks_Model
from reliability.Fitters import Fit_Weibull_CR, Fit_Weibull_Mixture
import matplotlib.pyplot as plt
import pandas as pd

# create some data from a competing risks model
d1 = Weibull_Distribution(alpha=250, beta=2)
d2 = Weibull_Distribution(alpha=210, beta=10)
CR_model = Competing_Risks_Model(distributions=[d1, d2])
data = CR_model.random_samples(50, seed=2)

CR_fit = Fit_Weibull_CR(failures=data)  # fit the Weibull competing risks model
MM_fit = Fit_Weibull_Mixture(failures=data)  # fit the Weibull mixture model
plt.legend()
plt.show()

# create a dataframe to display the goodness of fit criterion as a table
goodness_of_fit = {'Model': ['Competing Risks', 'Mixture'], 'AICc': [
    CR_fit.AICc, MM_fit.AICc], 'BIC': [CR_fit.BIC, MM_fit.BIC], 'AD': [CR_fit.AD, MM_fit.AD]}
df = pd.DataFrame(goodness_of_fit, columns=['Model', 'AICc', 'BIC', 'AD'])
print(df)

'''
Results from Fit_Weibull_CR (95% CI):
           Point Estimate  Standard Error    Lower CI    Upper CI
Parameter
Alpha 1        229.832608       51.142184  148.594556  355.484273
Beta 1           2.501343        0.746502    1.393607    4.489586
Alpha 2        199.720752        8.561263  183.626538  217.225567
Beta 2           9.201575        2.200422    5.758505   14.703291
Log-Likelihood: -255.44383742100507

Results from Fit_Weibull_Mixture (95% CI):
              Point Estimate  Standard Error    Lower CI    Upper CI
Parameter
Alpha 1           110.618178       29.929617   65.090789  187.989443
Beta 1              3.632755        1.543561    1.579646    8.354346
Alpha 2           191.064502        3.430400  184.457963  197.907661
Beta 2              8.049745        1.161811    6.066373   10.681571
Proportion 1        0.248562        0.074431    0.131549    0.419395
Log-Likelihood: -254.69963111152975

             Model        AICc         BIC        AD
0  Competing Risks  519.776564  526.535767  0.582669
1          Mixture  520.762899  528.959377  0.550508
'''
