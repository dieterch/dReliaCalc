from reliability.Distributions import Weibull_Distribution
import matplotlib.pyplot as plt

# this created the distribution object
dist = Weibull_Distribution(alpha=50, beta=2)
dist.PDF()  # this creates the plot of the PDF
plt.show()
