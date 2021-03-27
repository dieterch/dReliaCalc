import arrow
from tabulate import tabulate
import dmyplant2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint as pp
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# Read Input CSV files (Upload first ... )
dval = pd.read_csv("input2.csv", sep=';', encoding='utf-8')
dval['val start'] = pd.to_datetime(dval['val start'], format='%d.%m.%Y')
failures = pd.read_csv("failures.csv", sep=';', encoding='utf-8')
failures['date'] = pd.to_datetime(failures['date'], format='%d.%m.%Y')

# identify yourself & create instances
dmyplant2.cred()
mp = dmyplant2.MyPlant(600)
vl = dmyplant2.Validation(mp, dval, cui_log=False)
d = vl.dashboard

tdef = {1258: 'OperationalCondition', 19074: 'Various_Bits_CollAlarm'}
ntable = [[e] + [e.get_dataItem(v) for v in tdef.values()] for e in vl.engines]
dft = pd.DataFrame(ntable, columns=['Name'] + list(tdef.values()))

#pp(d['oph parts'].describe())

# Summary of current Operation condition
print(
    f"\n{dft.OperationalCondition.count()} Validation Engines with {d['oph parts'].sum()} cumulated oph, fleet leader {d['oph parts'].max()} oph observed.")
print(f"{dft[dft.OperationalCondition == 'Running'].OperationalCondition.count()} Validation Engines UP and Running")
print(f"{dft[dft.OperationalCondition != 'Running'].OperationalCondition.count()} Validation Engines not Running: \n")
print(tabulate(dft[dft.OperationalCondition !=
                   'Running'], headers=dft.columns), "\n")
dtripped = dft[dft.OperationalCondition == 'Tripped']
for eng in dtripped.values:
    le = eng[0]
    print(le)
    dtrips = le.batch_hist_alarms(p_severities=[800], p_offset=0, p_limit=5)
    dtrips['datetime'] = pd.to_datetime(
        dtrips['timestamp'] * 1000000.0).dt.strftime("%m-%d-%Y %H:%m")
    print(tabulate(dtrips[['datetime', 'message', 'name', 'severity']]))
    print()

print(tabulate(failures, headers=failures.columns))

e = vl.eng_serialNumber(1225799)
#id = e.id

# fetch Lube Oil Consuption data
locdef = {227: ['OilConsumption', 'g/kWh'],
          237: ['DeltaOpH', 'h'],
          228: ['OilVolume', 'l'],
          225: ['ActiveEnergy', 'MWh'],
          226: ['AvgPower', 'kW']}

limit = 2500

# call myplant
df = e._batch_hist_dataItems(itemIds=locdef, p_limit=limit, timeCycle=30)

# Set Type of time column to DateTime
df['datetime'] = pd.to_datetime(df['time'] * 1000000)

# Filter to Validation Period
df = df[df.datetime > pd.to_datetime(e._d['val start'])]

# Filter Oil Consumption outliers by < 3 * stdev
df = df[np.abs(df.OilConsumption-df.OilConsumption.mean())
        <= (3*df.OilConsumption.std())]

# Calc Rolling Mean values
df['LOC'] = df.OilConsumption.rolling(10).mean()
df['Pow'] = df.AvgPower.rolling(10).mean()

dfl = df[['datetime', 'OilConsumption', 'LOC', 'AvgPower', 'Pow']]
dfl = df[['datetime', 'LOC', 'Pow']]
ax = dfl.plot(subplots=False, x='datetime', secondary_y=[
              'AvgPower', 'Pow'], ylim=(0, 1.0), figsize=(12, 8), title=e, grid=True)
ax.set_ylim(1000, 5000)

dat = {
    161: ['CountOph', 'h'],
    102: ['PowerAct', 'kW'],
    217: ['Hyd_PressCrankCase', 'mbar'],
    16546: ['Hyd_PressOilDif', 'bar']
    # ,1001101: 'RMD_ListBuffMAvgOilConsume_OilConsumption'
}

df = e.hist_data(
    itemIds=dat,
    p_from=arrow.get(arrow.get(e.valstart_ts)),
    # p_from=arrow.now('Europe/Vienna').shift(weeks=-3),
    p_to=arrow.now('Europe/Vienna'),
    timeCycle=30)


# Set Type of time column to DateTime
df['datetime'] = pd.to_datetime(df['time'] * 1000000)
df['CountOph'] = df.CountOph - e.oph_start
dff = df[df.Hyd_PressCrankCase <= 10.0]

# Just include the data to plot
dfp = dff[['datetime', 'CountOph', 'PowerAct',
           'Hyd_PressCrankCase', 'Hyd_PressOilDif']]
dfp.set_index('datetime')

dmyplant2.chart(dfp, [
    {'col': ['PowerAct'], 'ylim': [0, 5000], 'color': 'black'},
    {'col': ['CountOph'], 'ylim': [0, 1000]},
    {'col': ['Hyd_PressCrankCase'], 'ylim': [-50, 50]},
    {'col': ['Hyd_PressOilDif'], 'ylim': [0, 1]}
],
    title=e,
    figsize=(12, 8)
)

plt.show()
