from reliability.Repairable_systems import MCF_parametric
import matplotlib.pyplot as plt
times = [[5, 10, 15, 17], [6, 13, 17, 19], [
    12, 20, 25, 26], [13, 15, 24], [16, 22, 25, 28]]
MCF_parametric(data=times)
plt.show()

'''
Mean Cumulative Function Parametric Model (95% CI):
MCF = (t/α)^β
           Point Estimate  Standard Error   Lower CI   Upper CI
Parameter
Alpha           11.980590        0.401372  11.219187  12.793666
Beta             1.673622        0.094654   1.498017   1.869813
Since Beta is greater than 1, the system repair rate is WORSENING over time.
'''
