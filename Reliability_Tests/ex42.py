from reliability.Repairable_systems import optimal_replacement_time
import matplotlib.pyplot as plt
optimal_replacement_time(cost_PM=1, cost_CM=5,
                         weibull_alpha=1000, weibull_beta=2.5, q=0)
plt.show()

'''
Cost model assuming as good as new replacement (q=0):
The minimum cost per unit time is 0.0035
The optimal replacement time is 493.19
'''
