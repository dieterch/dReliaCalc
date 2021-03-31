import arrow
from pprint import pprint as pp
import sys

import dmyplant2
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

dmyplant2.cred()  # Ask for credentials every month
mp = dmyplant2.MyPlant(7200)  # login to myplant and keep connection
ee = dmyplant2.Engine_SN(mp, '1184199')  # create Engine Class Instance
print()
print(ee)

#dat = mp.load_dataitems_csv("DataItems_Request.csv")
dat = {
    161: ['CountOph', 'h'],
    102: ['PowerAct', 'kW'],
    69: ['Hyd_PressCoolWat', 'bar']
}

print()
print('Downloading Data from Myplant ...')

lfrom = arrow.get('2021-01-01 00:00').to('Europe/Vienna')
lto = arrow.get('2021-01-02 00:00').to('Europe/Vienna')
cycle = 1

df = ee.hist_data(
    # ee.id,
    dat,
    p_from=lfrom,
    p_to=lto,
    timeCycle=cycle,
    slot=0
)
pp(df.shape)
pp(df.tail(20))
