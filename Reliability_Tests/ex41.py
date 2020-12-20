from reliability.Repairable_systems import reliability_growth
import matplotlib.pyplot as plt
times = [10400, 26900, 43400, 66400, 89400,
         130400, 163400, 232000, 242000, 340700]
reliability_growth(times=times, target_MTBF=50000,
                   label='Reliability growth curve', xmax=500000)
plt.legend()
plt.show()

'''
Reliability growth model parameters:
lambda: 0.002355878294089656
beta: 0.6638280053477188
Time to reach target MTBF: 428131.18039448344
'''
