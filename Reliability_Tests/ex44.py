from reliability.Repairable_systems import MCF_nonparametric
import matplotlib.pyplot as plt
times = [[5, 10, 15, 17], [6, 13, 17, 19], [
    12, 20, 25, 26], [13, 15, 24], [16, 22, 25, 28]]
MCF_nonparametric(data=times)
plt.show()

'''
Mean Cumulative Function results (95.0% CI)
       time  MCF_lower      MCF MCF_upper  variance
state
F         5  0.0459299      0.2  0.870893     0.032
F         6    0.14134      0.4   1.13202     0.064
F        10   0.256603      0.6   1.40294     0.096
F        12   0.383374      0.8   1.66939     0.128
F        13   0.517916        1   1.93081      0.16
F        13   0.658169      1.2   2.18789     0.192
F        15   0.802848      1.4   2.44131     0.224
F        15   0.951092      1.6   2.69164     0.256
F        16    1.10229      1.8   2.93935     0.288
F        17    1.25598        2   3.18478      0.32
C        17
C        19
F        20    1.49896  2.33333   3.63215  0.394074
F        22    1.74856  2.66667   4.06684  0.468148
C        24
F        25    2.12259  3.16667   4.72431  0.593148
F        25     2.5071  3.66667   5.36255  0.718148
C        26
C        28
'''
