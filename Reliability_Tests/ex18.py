from reliability.Distributions import Lognormal_Distribution, Gamma_Distribution, Weibull_Distribution, Competing_Risks_Model
import matplotlib.pyplot as plt

# create the competing risks model
d1 = Lognormal_Distribution(mu=4, sigma=0.1)
d2 = Weibull_Distribution(alpha=50, beta=2)
d3 = Gamma_Distribution(alpha=30, beta=1.5)
CR_model = Competing_Risks_Model(distributions=[d1, d2, d3])

# plot the 5 functions using the plot() function
CR_model.plot()

# plot the PDF and CDF
plot_components = True  # this plots the component distributions. Default is False
plt.figure(figsize=(9, 5))
plt.subplot(121)
CR_model.PDF(plot_components=plot_components, color='red', linestyle='--')
plt.subplot(122)
CR_model.CDF(plot_components=plot_components, color='red', linestyle='--')
plt.show()

# extract the mean of the distribution
print('The mean of the distribution is:', CR_model.mean)

'''
The mean of the distribution is: 27.04449126273065
'''
