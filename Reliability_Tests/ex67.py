from reliability.ALT_fitters import Fit_Weibull_Power_Exponential
from reliability.Datasets import ALT_temperature_voltage
import matplotlib.pyplot as plt
data = ALT_temperature_voltage()
Fit_Weibull_Power_Exponential(failures=data.failures, failure_stress_thermal=data.failure_stress_temp,
                              failure_stress_nonthermal=data.failure_stress_voltage, use_level_stress=[325, 0.5])
plt.show()

'''
Results from Fit_Weibull_Power_Exponential (95% CI):
           Point Estimate  Standard Error     Lower CI     Upper CI
Parameter
a             3404.485691      627.674716  2174.265854  4634.705528
c                0.087610        0.141217    -0.189170     0.364391
n               -0.713424        0.277561    -1.257434    -0.169414
beta             4.997527        1.173998     3.153512     7.919828
At the use level stresses of 325 and 0.5 , the mean life is 4673.15347
'''
