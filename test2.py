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
desc = ee.dash
fn = fr"./data/{ee.serialNumber}_1.hdf"

#dat = mp.load_dataitems_csv("DataItems_Request.csv")
dat = {
    161: ['CountOph', 'h'],
    102: ['PowerAct', 'kW'],
    69: ['Hyd_PressCoolWat', 'bar']
}
#del desc['oph parts']
#del desc['val start']
#del desc['oph@start']
desc['Timezone'] = 'Europe/Vienna'
desc['p_from'] = lfrom
desc['p_to'] = lto
desc['timeCycle'] = cycle
desc['Exported_By'] = mp.username
desc['Export_Date'] = arrow.now().to(
    'Europe/Vienna').format('DD.MM.YYYY - HH:mm')
desc['dataItems'] = dat

pp(desc)

print()
print('Downloading Data from Myplant ...')
df = ee.hist_data(
    # ee.id,
    dat,
    p_from=lfrom,
    p_to=lto,
    timeCycle=cycle,
    slot=0
)

df.to_hdf(fn, "data", complevel=6)

df_desc = pd.DataFrame.from_dict(desc.items()).set_index(0)
df_desc.columns = ['Values']
df_desc.index.name = 'Keys'
# pp(df_desc)
df_desc.to_hdf(fn, "description", complevel=6)
print()
