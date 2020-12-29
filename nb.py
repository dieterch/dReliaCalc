from dmyplant2 import cred
import dmyplant2
import pandas as pd
from pprint import pprint as pp
import sys
import matplotlib.pyplot as plt

dval = pd.read_csv("input4.csv", sep=';', encoding='utf-8')
# pp(dval['val start'])
dval['val start'] = pd.to_datetime(dval['val start'], dayfirst=True)
# pp(dval['val start'])

# sys.exit(0)

mp = dmyplant2.MyPlant(0)
vl = dmyplant2.Validation(mp, dval, cui_log=True)


failures = pd.DataFrame([])
dmyplant2.demonstrated_Reliabillity_Plot(vl,
                                         beta=1.21, T=30000, s=1000, ft=failures, cl=[10, 50, 90], factor=2.0)


d = vl.dashboard
d.head()

ee = vl.engines[0]
df = ee.batch_hist_dataItem(161, ee.valstart_ts, ee.now_ts, timeCycle=86400)

plt.plot(df['timestamp'], df['161'])
plt.show()

# print('----')
# for i, e in enumerate(vl.engines):
#    print(f"{i:02d} {e} {e.historical_dataItem(161, e.now_ts):6.0f} oph")
