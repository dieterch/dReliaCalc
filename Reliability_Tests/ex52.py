from reliability.PoF import strain_life_diagram
import matplotlib.pyplot as plt
strain_life_diagram(E=210000, sigma_f=1000, epsilon_f=1.1, b=-0.1,
                    c=-0.6, K=1200, n=0.2, max_strain=0.0049, min_strain=-0.0029)
plt.show()

'''
Failure will occur in 13771.39 cycles (27542.78 reversals).
'''
