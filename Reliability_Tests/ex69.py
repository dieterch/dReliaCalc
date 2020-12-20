from reliability.Other_functions import convert_dataframe_to_grouped_lists
import pandas as pd
# create some data in a dataframe
data = {'outcome': ['Failed', 'Censored', 'Failed', 'Failed', 'Censored'],
        'cycles': [1253, 1500, 1342, 1489, 1500]}
df = pd.DataFrame(data, columns=['outcome', 'cycles'])
print(df, '\n')
# usage of the function
lists, names = convert_dataframe_to_grouped_lists(df)
print(names[0], lists[0])
print(names[1], lists[1])

'''
    outcome  cycles
0    Failed    1253
1  Censored    1500
2    Failed    1342
3    Failed    1489
4  Censored    1500

Censored [1500, 1500]
Failed [1253, 1342, 1489]
'''
