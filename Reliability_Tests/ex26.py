from reliability.Probability_plotting import Weibull_probability_plot, Exponential_probability_plot
from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt

data = Weibull_Distribution(alpha=5, beta=3).random_samples(100, seed=1)
plt.subplot(121)
Weibull_probability_plot(failures=data)
plt.title('Example of a good fit')
plt.subplot(122)
Exponential_probability_plot(failures=data)
plt.title('Example of a bad fit')
plt.subplots_adjust(bottom=0.1, right=0.94, top=0.93,
                    wspace=0.34)  # adjust the formatting
plt.show()
