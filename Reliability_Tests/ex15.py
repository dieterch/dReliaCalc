from reliability.Distributions import Lognormal_Distribution, Gamma_Distribution, Weibull_Distribution, Mixture_Model
import matplotlib.pyplot as plt

# create the mixture model
d1 = Lognormal_Distribution(mu=2, sigma=0.8)
d2 = Weibull_Distribution(alpha=50, beta=5, gamma=100)
d3 = Gamma_Distribution(alpha=5, beta=3, gamma=30)
mixture_model = Mixture_Model(
    distributions=[d1, d2, d3], proportions=[0.3, 0.4, 0.3])

# plot the 5 functions using the plot() function
mixture_model.plot()

# plot the PDF and CDF
plot_components = True  # this plots the component distributions. Default is False
plt.figure(figsize=(9, 5))
plt.subplot(121)
mixture_model.PDF(plot_components=plot_components, color='red', linestyle='--')
plt.subplot(122)
mixture_model.CDF(plot_components=plot_components, color='red', linestyle='--')
plt.subplots_adjust(left=0.1, right=0.95)
plt.show()

# extract the mean of the distribution
print('The mean of the distribution is:', mixture_model.mean)

'''
The mean of the distribution is: 74.91674657035722
'''
