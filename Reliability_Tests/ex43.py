from reliability.Repairable_systems import ROCOF
import matplotlib.pyplot as plt
t = [104, 131, 1597, 59, 4, 503, 157, 6, 118, 173, 114, 62, 101, 216,
     106, 140, 1, 102, 3, 393, 96, 232, 89, 61, 37, 293, 7, 165, 87, 99]
ROCOF(times_between_failures=t)
plt.show()

'''
Laplace test results: U = 2.409, z_crit = (-1.96,+1.96)
At 95 % confidence level the ROCOF is WORSENING. Assume NHPP.
ROCOF assuming NHPP has parameters: Beta_hat = 1.588 , Lambda_hat = 3.703e-05
'''
