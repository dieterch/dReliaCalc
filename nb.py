import arrow
from pprint import pprint as pp
import sys

import dmyplant2
import pandas as pd

dmyplant2.cred()  # Ask for credentials every month
mp = dmyplant2.MyPlant(7200)  # login to myplant and keep connection
ee = dmyplant2.Engine_SN(mp, '1195712')  # create Engine Class Instance
print()
print(ee)
pp(ee.dash)

print()
print(f"Bore:\t{ee.bore:0.1f} mm")
print(f"Stroke:\t{ee.stroke:0.1f} mm")
print(f"Volume per Cyl:\t{ee.cylvol:0.2f} l")
print(f"Volume per Eng:\t{ee.engvol:0.2f} l")
print(f"No of Cyl:\t{ee.Cylinders}")
print(f"Speed:\t{ee.Speed_nominal}")
print(f"BMEP:\t{ee.BMEP:0.1f} bar")
print(f"el. Power\t{ee.P_nominal:0.1f} kW")
print(f"mech. Power\t{ee.Pmech_nominal:0.1f} kW")
print(f"Gen. Eff\t{ee.Generator_Efficiency * 100 :0.1f} %")
print(f"Gen. CosPhi\t{ee.cos_phi:0.1f}")
print()
print(
    f"J920 Power at 22 bar BMEP:\t{ee._mechpower('9', 20, 22, 1000):0.1f} kW")
print()
for p in ['9', '6', '4', '3']:
    print(
        f"platform {p},\tVol per cylinder {ee._cylvol(p):0.2f} l,\tbore {ee._bore(p)} mm, stroke {ee._stroke(p)} mm")

print()
# read datapoint definition from file
# dat = {
#     161: ['CountOph','h'],
#     102: ['PowerAct','kW'],
#     107: ['Various_Values_SpeedAct','1/min'],
#     217: ['Hyd_PressCrankCase','mbar'],
#     16546: ['Hyd_PressOilDif','bar']
#     #,1001101: 'RMD_ListBuffMAvgOilConsume_OilConsumption'
# }

dat = mp.load_dataitems_csv("DataItems_Request.csv")

df = mp.history_batchdata(
    ee.id,
    dat,
    p_from=arrow.get('2020-08-15 07:00').to('Europe/Vienna'),
    p_to=arrow.get('2020-08-20 21:00').to('Europe/Vienna'),
    timeCycle=30,
    cui_log=True
)
df.to_hdf("test.hdf", "data")
print()
print(f"Size of Dataframe {sys.getsizeof(df) / 1e6} MB")

# pp(ee.properties)
#df = ee.batch_hist_dataItem(161, ee.valstart_ts, ee.now_ts, timeCycle=86400)

# plt.plot(df['timestamp'], df['161'])
# plt.show()

# print('----')
# for i, e in enumerate(vl.engines):
#    print(f"{i:02d} {e} {e.historical_dataItem(161, e.now_ts):6.0f} oph")
