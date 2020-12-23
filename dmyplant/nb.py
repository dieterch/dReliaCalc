from dmyplant import cred
import dmyplant
import pandas as pd
from pprint import pprint as pp
import sys

dval = pd.read_csv("input2.csv", sep=';', encoding='utf-8')
# pp(dval['val start'])
dval['val start'] = pd.to_datetime(dval['val start'], dayfirst=True)
# pp(dval['val start'])

# sys.exit(0)

mp = dmyplant.MyPlant(7200)
vl = dmyplant.Validation(mp, dval, show_progress=True)

d = vl.dashboard
d.head(2)

# dp = d[['Name', 'oph parts']]
# dp['test'] = 2 * dp['oph parts']
# dp.head(5)

# failures = pd.DataFrame([])
# dmyplant.demonstrated_Reliabillity_Plot(vl,
#                                        beta = 1.21, T = 10000, s = 1000, ft = failures, cl = [10, 50, 90])

for e in vl.engines:
    print(e)
