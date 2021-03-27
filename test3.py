import arrow
import dmyplant2
import pandas as pd
import numpy as np
from pprint import pprint as pp
import matplotlib.pyplot as plt
import sys

df_desc = pd.read_hdf("./data/1184199_1.hdf", 'description')
df_data = pd.read_hdf("./data/1184199_1.hdf", 'data')

pp(df_desc)


dmyplant2.cred()  # Ask for credentials every month
mp = dmyplant2.MyPlant(7200)  # login to myplant and keep connection
dat = mp.load_dataitems_csv("DataItems_Request.csv")
e = dmyplant2.Engine_SN(mp, '1184199')  # create Engine Class Instance

# dfs = df[
#    (df['datetime'] > pd.to_datetime('2021-02-21 09:00')) &
#    (df['datetime'] < pd.to_datetime('2021-02-21 17:00'))
# ].copy()
#dfs = df_data[:-1].copy()
#dfs['diff'] = np.diff(df_data['PowerAct'])

dfs = df_data.copy()
dfs['frac'] = np.modf(dfs['PowerAct'])[0]
dfs = dfs[dfs['frac'] > 0.0]
dfs2 = dfs[:-1].copy()
dfs2['diff'] = np.round(np.diff(dfs['time']) / 10000.0, 1)*10
dfs2 = dfs2[dfs2['diff'] <= 2.0]

pp(dfs2[['datetime', 'PowerAct', 'diff']])

#dfs['HZ'] = dfs['Various_Values_SpeedAct'] / 1500.0 * 50.0

print(f"Size of Dataframe {sys.getsizeof(df_data) / 1e6} MB")

dset = [{'col': ['Power_PowerAct'], 'ylim':(0, 5000)},
        {'col': ['Various_Values_SpeedAct'], 'ylim':(1350, 1550)},
        {'col': ['HZ'], 'ylim':(47.5, 51.5)},
        {'col': ['Various_Values_PressBoost'], 'ylim':(2, 12)},
        {'col': ['TecJet_Lambda1'], 'ylim':(1.5, 2.5)},
        {'col': ['Various_Values_TempMixture'], 'ylim':(40, 60)},
        {'col': ['Hyd_PressOilDif'], 'ylim':(0, 2)},
        {'col': ['Aux_PreChambDifPress'], 'ylim':(-1500, 1500)},
        ]

dat = {
    161: ['CountOph', 'h'],
    102: ['PowerAct', 'kW'],
    69: ['Hyd_PressCoolWat', 'bar']
}

dset2 = [{'col': ['PowerAct'], 'ylim':(0, 5000)},
         {'col': ['datetime']},
         #{'col': ['diff'], 'ylim':(0, 100)},
         ]
#dmyplant2.chart(dfs2, dset2, title=e, figsize=(12, 8))

dfs2.plot(kind='scatter', x='datetime', y='PowerAct', title='highres areas')

dtrips = e.batch_hist_alarms(
    p_from=arrow.get('2021-01-01 00:00').to('Europe/Vienna'),
    p_to=arrow.get('2021-02-01 00:00').to('Europe/Vienna')
)
dtrips = dtrips[(dtrips['name'] == '1232') | (dtrips['name'] == '1231')]
for row in dtrips[['name', 'message', 'datetime']][::-1].values:
    print(row)
# for i in range(len(dset) - 1):
#     ldset = dset[:(i+2)]
#     dmyplant2.chart(dfs, ldset, title=e, figsize=(12, 8))

plt.show()
