from reliability.Distributions import Weibull_Distribution
from reliability.Probability_plotting import Weibull_probability_plot
import matplotlib.pyplot as plt

dist = Weibull_Distribution(alpha=250, beta=3)
for i, x in enumerate([10, 100, 1000]):
    plt.subplot(131 + i)
    dist.CDF(linestyle='--', label='True CDF')
    failures = dist.random_samples(x, seed=42)  # take 10, 100, 1000 samples
    Weibull_probability_plot(failures=failures)  # this is the probability plot
    plt.title(str(str(x) + ' samples'))
# adjust the figure size after creation. Necessary to do it after as it it automatically adjusted within probability_plot
plt.gcf().set_size_inches(15, 7)
plt.tight_layout()
plt.show()
