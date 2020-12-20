from reliability.Reliability_testing import reliability_test_duration
import matplotlib.pyplot as plt

reliability_test_duration(
    MTBF_required=2500, MTBF_design=3000, consumer_risk=0.2, producer_risk=0.2)
plt.show()

'''
Reliability Test Duration Solver for time-terminated test
Required test duration: 231615.79491309822 # Note that this duration is the total time on test and may be split across several vehicles.
Specified consumer's risk: 0.2
Specified producer's risk: 0.2
Specified MTBF required by the consumer: 2500
Specified MTBF designed to by the producer: 3000
'''
