from reliability.Other_functions import make_right_censored_data
output = make_right_censored_data(
    data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], threshold=6)
print('Failures:', output.failures)
print('Right Censored:', output.right_censored)

'''
Failures: [1 2 3 4 5 6]
Right Censored: [6 6 6 6] #the numbers 7 to 10 have been set equal to the threshold
'''
