from reliability.Repairable_systems import MCF_parametric
from reliability.Datasets import MCF_2
import matplotlib.pyplot as plt

times = MCF_2().times
MCF_parametric(data=times, print_results=False)
plt.show()
