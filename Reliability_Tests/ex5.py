from reliability.Distributions import Weibull_Distribution, Lognormal_Distribution, Exponential_Distribution
import matplotlib.pyplot as plt
import numpy as np
xvals = np.linspace(0, 1000, 1000)
infant_mortality = Weibull_Distribution(alpha=400, beta=0.7).HF(
    xvals=xvals, label='infant mortality [Weibull]')
random_failures = Exponential_Distribution(Lambda=0.001).HF(
    xvals=xvals, label='random failures [Exponential]')
wear_out = Lognormal_Distribution(mu=6.8, sigma=0.1).HF(
    xvals=xvals, label='wear out [Lognormal]')
combined = infant_mortality+random_failures+wear_out
plt.plot(xvals, combined, linestyle='--', label='Combined hazard rate')
plt.legend()
plt.title('Example of how multiple failure modes at different stages of\nlife create a "Bathtub curve" for the total Hazard function')
plt.show()
