import arrow
import dmyplant2
import pandas as pd
import numpy as np
from pprint import pprint as pp
import matplotlib.pyplot as plt
import sys

# df_desc = pd.read_hdf("./data/1184199_1.hdf", 'description')
# df_data = pd.read_hdf("./data/1184199_1.hdf", 'data')

# pp(df_desc)

dmyplant2.cred()  # Ask for credentials every month
mp = dmyplant2.MyPlant(7200)  # login to myplant and keep connection
dat = mp.load_dataitems_csv("DataItems_Request.csv")
ee = dmyplant2.Engine_SN(mp, '1184199')  # create Engine Class Instance

dat = {
    161: ['CountOph', 'h'],
    102: ['PowerAct', 'kW'],
    69: ['Hyd_PressCoolWat', 'bar']
}

print()
print('Downloading Data from Myplant ...')

lfrom = arrow.get('2021-01-01 00:00').to('Europe/Vienna')
lto = arrow.get('2021-01-30 00:00').to('Europe/Vienna')
cycle = 1

df = ee.hist_data(
    dat,
    p_from=lfrom,
    p_to=lto,
    timeCycle=cycle,
    slot=0
)


# dfs = df[
#    (df['datetime'] > pd.to_datetime('2021-02-21 09:00')) &
#    (df['datetime'] < pd.to_datetime('2021-02-21 17:00'))
# ].copy()
#dfs = df_data[:-1].copy()
#dfs['diff'] = np.diff(df_data['PowerAct'])

dfs = df.copy()
dfs['frac'] = np.modf(dfs['PowerAct'])[0]
dfs = dfs[dfs['frac'] > 0.0]
dfs2 = dfs[:-1].copy()
dfs2['diff'] = np.round(np.diff(dfs['time']) / 10000.0, 1)*10
dfs2 = dfs2[dfs2['diff'] <= 2.0]

pp(dfs2[['datetime', 'PowerAct', 'diff']])

#dfs['HZ'] = dfs['Various_Values_SpeedAct'] / 1500.0 * 50.0

print(f"Size of Dataframe {sys.getsizeof(df) / 1e6} MB")

dat = {
    161: ['CountOph', 'h'],
    102: ['PowerAct', 'kW'],
    69: ['Hyd_PressCoolWat', 'bar']
}

dset2 = [{'col': ['PowerAct'], 'ylim':(0, 5000)},
         {'col': ['datetime']},
         {'col': ['diff'], 'ylim':(0, 100)},
         ]
#dmyplant2.chart(dfs2, dset2, title=ee, figsize=(12, 8))

#dfs2.plot(kind='scatter', x='datetime', y='PowerAct', title='highres areas')


df = ee.scan_for_highres_DataFrames(dat)
df.info()
print(df.head(5))
print(df.tail(5))

dset2 = [
    {'col': ['PowerAct']},
    {'col': ['datetime']},
    {'col': ['Hyd_PressCoolWat']}
]
dmyplant2.chart(df, dset2, title=ee, figsize=(12, 8))

# dtrips = ee.batch_hist_alarms(
#     p_from=arrow.get('2021-01-01 00:00').to('Europe/Vienna'),
#     p_to=arrow.get('2021-02-01 00:00').to('Europe/Vienna')
# )
# dtrips = dtrips[(dtrips['name'] == '1232') | (dtrips['name'] == '1231')]
# for row in dtrips[['name', 'message', 'datetime']][::-1].values:
#     print(row)
# for i in range(len(dset) - 1):
#     ldset = dset[:(i+2)]
#     dmyplant2.chart(dfs, ldset, title=e, figsize=(12, 8))

plt.show()
