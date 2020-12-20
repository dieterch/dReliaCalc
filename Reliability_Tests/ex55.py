from reliability.PoF import creep_rupture_curves
import matplotlib.pyplot as plt
TEMP = [900, 900, 900, 900, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
        1100, 1100, 1100, 1100, 1100, 1200, 1200, 1200, 1200, 1350, 1350, 1350]
STRESS = [90, 82, 78, 70, 80, 75, 68, 60, 56, 49, 43,
          38, 60.5, 50, 40, 29, 22, 40, 30, 25, 20, 20, 15, 10]
TTF = [37, 975, 3581, 9878, 7, 17, 213, 1493, 2491, 5108, 7390, 10447,
       18, 167, 615, 2220, 6637, 19, 102, 125, 331, 3.7, 8.9, 31.8]
creep_rupture_curves(temp_array=TEMP, stress_array=STRESS,
                     TTF_array=TTF, stress_trace=70, temp_trace=1100)
plt.show()
