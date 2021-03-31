#%%
print("Hello world")

#%%
import arrow
from pprint import pprint as pp
import sys

import dmyplant2
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)


lfrom = arrow.get('2021-01-01 00:00').to('Europe/Vienna')
lto = arrow.get('2021-02-01 00:00').to('Europe/Vienna')
cycle = 1

dmyplant2.cred()  # Ask for credentials every month
mp = dmyplant2.MyPlant(7200)  # login to myplant and keep connection
ee = dmyplant2.Engine_SN(mp, '1184199')  # create Engine Class Instance
print()
print(ee)
# %%
