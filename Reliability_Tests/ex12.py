from reliability.Fitters import Fit_Weibull_2P_grouped
import pandas as pd

# option 1 for importing this dataset (from an excel file on your desktop)
filename = 'C:\\Users\\Current User\\Desktop\\data.xlsx'
df = pd.read_excel(io=filename)

# option 2 for importing this dataset (from the dataset in reliability)
# from reliability.Datasets import electronics
# df = electronics().dataframe

print(df.head(15), '\n')
# note that the TNC optimiser usually underperforms the default (L-BFGS-B) optimiser but in this case it is better
Fit_Weibull_2P_grouped(dataframe=df, optimizer='TNC',
                       show_probability_plot=False)

'''
     time  quantity category
0     220         1        F
1     179         1        F
2     123         1        F
3     146         1        F
4     199         1        F
5     181         1        F
6     191         1        F
7     216         1        F
8       1         1        F
9      73         1        F
10  44798       817        C
11  62715       823        C
12  81474       815        C
13  80632       813        C
14  62716       804        C

Results from Fit_Weibull_2P_grouped (95% CI):
           Point Estimate  Standard Error      Lower CI      Upper CI
Parameter
Alpha        6.205380e+21    7.780317e+22  1.319435e+11  2.918427e+32
Beta         1.537356e-01    4.863029e-02  8.270253e-02  2.857789e-01
Log-Likelihood: -144.61675864154972
Number of failures: 10
Number of right censored: 4072
Fraction censored: 99.75502 %
'''
