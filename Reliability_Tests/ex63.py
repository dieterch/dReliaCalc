from reliability.ALT_probability_plotting import ALT_probability_plot_Weibull, ALT_probability_plot_Exponential
import matplotlib.pyplot as plt
import numpy as np
from reliability.Distributions import Exponential_Distribution

# create the data using an Exponential distribution
data1 = Exponential_Distribution(Lambda=1 / 100).random_samples(20, seed=2)
data2 = Exponential_Distribution(Lambda=1 / 500).random_samples(20, seed=3)
data3 = Exponential_Distribution(Lambda=1 / 3000).random_samples(20, seed=4)
f = np.hstack([data1, data2, data3])
f_stress = np.hstack(
    [np.ones_like(data1) * 50, np.ones_like(data1) * 40, np.ones_like(data1) * 30])
# plot the data
plt.subplot(121)
ALT_probability_plot_Exponential(failures=f, failure_stress=f_stress)
plt.subplot(122)
ALT_probability_plot_Weibull(
    failures=f, failure_stress=f_stress, common_shape_method='average')
plt.gcf().set_size_inches((11, 7))
plt.show()

'''
ALT Exponential probability plot results:
  stress  weibull alpha  weibull beta  new 1/Lambda  common shape shape change
    30.0    3950.302619      0.775461   4154.505068           1.0      +28.96%
    40.0     366.204477      1.066262    357.669530           1.0       -6.21%
    50.0      73.371485      1.254340     68.352088           1.0      -20.28%
Total AICc: 864.1158725562174
Total BIC: 866.4364027102126
Total AICc (weibull): 864.3730503138722
Total BIC (weibull): 866.6935804678675

ALT Weibull probability plot results:
  stress  original alpha  original beta    new alpha  common beta beta change
    30.0     3950.302619       0.775461  3950.303608     1.032021     +33.08%
    40.0      366.204477       1.066262   361.817836     1.032021      -3.21%
    50.0       73.371485       1.254340    68.996497     1.032021     -17.72%
Total AICc: 864.3730503138722
Total BIC: 866.6935804678675
'''
