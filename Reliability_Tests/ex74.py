from reliability.Other_functions import make_right_censored_data
output = make_right_censored_data(
    data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], fraction_censored=0.5, seed=1)
print('Failures:', output.failures)
print('Right Censored:', output.right_censored)

'''
Failures: [4 1 5 2 3] # half of the data has not been censored. It has been shuffled so its order will be different from the order of the input data.
Right Censored: [5.89006504 8.71327034 4.27673283 3.11056676 2.728583] # half of the data has been censored at some value between 0 and the original value
'''
