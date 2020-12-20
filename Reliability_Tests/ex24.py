from reliability.Distributions import Exponential_Distribution
from reliability.Probability_plotting import Exponential_probability_plot, Weibull_probability_plot, Exponential_probability_plot_Weibull_Scale
import matplotlib.pyplot as plt

# should give Lambda = 0.01 OR Weibull alpha = 10
data1 = Exponential_Distribution(
    Lambda=1 / 10, gamma=5).random_samples(50, seed=42)
# should give Lambda = 0.001 OR Weibull alpha = 100
data2 = Exponential_Distribution(
    Lambda=1 / 100, gamma=5).random_samples(50, seed=42)
plt.subplot(131)
Exponential_probability_plot(failures=data1, fit_gamma=True)
Exponential_probability_plot(failures=data2, fit_gamma=True)
plt.subplot(132)
Weibull_probability_plot(failures=data1, fit_gamma=True)
Weibull_probability_plot(failures=data2, fit_gamma=True)
plt.subplot(133)
Exponential_probability_plot_Weibull_Scale(failures=data1, fit_gamma=True)
Exponential_probability_plot_Weibull_Scale(failures=data2, fit_gamma=True)
plt.gcf().set_size_inches(15, 7)
plt.subplots_adjust(left=0.08, right=0.97, top=0.91,
                    wspace=0.30)  # format the plot
plt.show()
