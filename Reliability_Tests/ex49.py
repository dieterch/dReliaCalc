from reliability.PoF import stress_strain_life_parameters_from_data
import matplotlib.pyplot as plt
strain_data = [0.02, 0.015, 0.01, 0.006, 0.0035, 0.002]
stress_data = [650, 625, 555, 480, 395, 330]
cycles_data = [200, 350, 1100, 4600, 26000, 560000]
params = stress_strain_life_parameters_from_data(
    stress=stress_data, strain=strain_data, cycles=cycles_data, E=216000)
plt.show()

'''
K (cyclic strength coefficient): 1462.4649152172044
n (strain hardening exponent): 0.19810419512368083
sigma_f (fatigue strength coefficient): 1097.405402055844
epsilon_f (fatigue strain coefficient): 0.23664541556833998
b (elastic strain exponent): -0.08898339316495743
c (plastic strain exponent): -0.4501077996416115
'''
