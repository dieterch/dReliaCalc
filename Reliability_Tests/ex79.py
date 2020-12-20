from reliability.Reliability_testing import two_proportion_test
result = two_proportion_test(
    sample_1_trials=500, sample_1_successes=490, sample_2_trials=800, sample_2_successes=770)
print(result)

'''
(-0.0004972498915250083, 0.03549724989152493, 'non-significant')
'''
