from reliability.PoF import SN_diagram
import matplotlib.pyplot as plt
stress = [340, 300, 290, 275, 260, 255, 250, 235, 230, 220, 215, 210]
cycles = [15000, 24000, 36000, 80000, 177000, 162000,
          301000, 290000, 361000, 881000, 1300000, 2500000]
SN_diagram(stress=stress, cycles=cycles)
plt.show()
