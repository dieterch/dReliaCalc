from reliability.PoF import SN_diagram
import matplotlib.pyplot as plt
stress = [340, 300, 290, 275, 260, 255, 250, 235, 230, 220, 215, 210]
cycles = [15000, 24000, 36000, 80000, 177000, 162000,
          301000, 290000, 361000, 881000, 1300000, 2500000]
stress_runout = [210, 210, 205, 205, 205]
cycles_runout = [10 ** 7, 10 ** 7, 10 ** 7, 10 ** 7, 10 ** 7]
SN_diagram(stress=stress, cycles=cycles, stress_runout=stress_runout, cycles_runout=cycles_runout,
           method_for_bounds='residual', cycles_trace=[5 * 10 ** 5], stress_trace=[260])
plt.show()
