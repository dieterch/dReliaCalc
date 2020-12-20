import numpy as np
# create the data
failure_times_at_stress_1 = [800, 850, 910, 940]
failure_stress_1 = [40, 40, 40, 40]
failure_times_at_stress_2 = [650, 670, 715, 740]
failure_stress_2 = [50, 50, 50, 50]
failure_times_at_stress_3 = [300, 320, 350, 380]
failure_stress_3 = [60, 60, 60, 60]
# combine the data
failures = np.hstack([failure_times_at_stress_1,
                      failure_times_at_stress_2, failure_times_at_stress_3])
failure_stresses = np.hstack(
    [failure_stress_1, failure_stress_2, failure_stress_3])
# print for inspection
print(failures)
print(failure_stresses)

'''
[800 850 910 940 650 670 715 740 300 320 350 380]
[40 40 40 40 50 50 50 50 60 60 60 60]
'''
