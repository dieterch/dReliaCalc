# example 1
from reliability.Reliability_testing import reliability_test_planner
reliability_test_planner(test_duration=19520, CI=0.8,
                         number_of_failures=7, one_sided=False)

'''
Reliability Test Planner results for time-terminated test
Solving for MTBF
Test duration: 19520
MTBF (lower confidence bound): 1658.3248534993454
Number of failures: 7
Confidence interval (2 sided): 0.8
'''

# example 2
output = reliability_test_planner(
    number_of_failures=6, test_duration=10000, CI=0.8, print_results=False)
print(output.MTBF)

'''
1101.8815940201118
'''
