from datetime import datetime
from functools import reduce
import pandas as pd
import numpy as np
import logging
from dmyplant.dEngine import Engine
from pprint import pprint as pp
from scipy.stats.distributions import chi2


class Validation:

    # define the dashboard columns in expected order
    _dashcols = [
        'Name',
        'Engine ID',
        'Design Number',
        'Engine Type',
        'Engine Version',
        'P',
        'serialNumber',
        'id',
        'Count_OpHour',
        'val start',
        'oph@start',
        'oph parts',
    ]
    _dash = None
    _val = None
    _engines = []

    def __init__(self, mp, dval):
        """ Myplant Validation object
            dval ... Pandas DataFrame with the Validation Definition,
                     defined in Excel sheet 'validation'
        """
        self._mp = mp
        self._val = dval
        self._now_ts = datetime.now().timestamp()
        self._valstart_ts = dval['val start'].min()

        engines = self._val.to_dict('records')
        # create and initialise all Engine Instances
        for eng in engines:
            self._engines.append(Engine(mp, eng))
            logging.info(
                f"{eng['n']} {eng['serialNumber']} {eng['Validation Engine']}")

        # iterate over engines and columns
        ldash = [[e.d[c] for c in self._dashcols] for e in self._engines]
        # dashboard as pandas Dataframe
        self._dash = pd.DataFrame(ldash, columns=self._dashcols)

    # def demonstrated_reliability(self, extrapolate_by_h=0.0, beta=1.21, CL=0.9, T=30000, f=0, size=10):
    #     t_arr = np.linspace(self.valstart_ts, self.now_ts +
    #                         3600.0 * extrapolate_by_h, size)
    #     nl_arr = []
    #     pl_arr = []
    #     dr_arr = []
    #     for t in t_arr:
    #         m = []
    #         tt = []
    #         pl = []
    #         for e in self._engines:
    #             m.append(e.P)
    #             tt.append(e.oph(t))
    #         tt_max = max(tt)
    #         if tt_max > 0.0:
    #             n_lip = 0.0
    #             for i in range(len(m)):
    #                 h = tt[i]/tt_max
    #                 h1 = h ** beta
    #                 ln_lip = m[i] * h1
    #                 pl.append(ln_lip / m[i] * 100)
    #                 n_lip += ln_lip

    #             n_lip_T = n_lip * ((tt_max/T) ** beta)
    #             # test = chi2.ppf(0.9, 2*(f+1))
    #             chif = chi2.ppf(CL, 2*(f+1))
    #             dr = np.exp(-chif/(2*n_lip_T))

    #             dr_arr.append(dr*100.0)
    #             nl_arr.append(n_lip)
    #             pl_arr.append(pl)
    #         else:
    #             dr_arr.append(0.0)
    #             pl_arr.append([])
    #             nl_arr.append(0.0)
    #     return (t_arr, np.array(dr_arr), nl_arr, pl_arr)

    # def demonstrated_reliability2(self, start, end, beta=1.21, CL=0.9, T=30000, ft=pd.DataFrame, size=10):
    #     f_arr = np.zeros(size)
    #     t_arr = np.linspace(start, end, size)

    #     if not(ft.empty):
    #         for row in ft.values:
    #             fl = np.where(t_arr > row[0].timestamp(), row[1], 0)
    #             f_arr += fl

    #     dr_arr = []
    #     for i, t in enumerate(t_arr):
    #         m = np.array([e.P for e in self._engines])
    #         tt = np.array([e.oph(t) for e in self._engines])
    #         tt_max = max(tt)
    #         if tt_max > 0.0:  # avoid division by zero
    #             # sum all part's per lipson equality to max hours at time t
    #             n_lip = sum(m*(tt/tt_max) ** beta)
    #             # use Lipson equality again to calc n@T hours
    #             n_lip_T = n_lip * ((tt_max/T) ** beta)
    #             # calc demonstrated Reliability per Chi.square dist (see A.Kleyner Paper)
    #             dr = np.exp(-chi2.ppf(CL, 2*(f_arr[i]+1))/(2*n_lip_T)) * 100.0
    #             # store in list for numpy vector
    #             dr_arr.append(dr)
    #         else:
    #             dr_arr.append(0.0)
    #     return (t_arr, np.array(dr_arr), f_arr)

    @ property
    def now_ts(self):
        return self._now_ts

    @ property
    def valstart_ts(self):
        return self._valstart_ts.timestamp()

    @ property
    def valstart(self):
        return self._valstart_ts

    @ property
    def dashboard(self):
        """ Validation Dasboard as Pandas Dataframe """
        return self._dash

    @ property
    def properties_dict(self):
        # Collect all Keys in a big list and remove double counts
        keys = []
        for e in self._engines:
            keys += e.properties.keys()     # add keys of each engine
            keys = list(set(keys))          # remove all double entries
        keys = sorted(keys, key=str.lower)
        dd = []
        for k in keys:                      # for all keys in all Val Engines
            for e in self._engines:         # iterate through al engines
                if k in e.properties.keys():
                    d = e.properties.get(k, None)  # get property dict
                    if d['value']:                 # if value exists
                        dd.append([d['name'], d['id']])  # store name, id pair
                        break
        return pd.DataFrame(dd, columns=['name', 'id'])

    @ property
    def dataItems_dict(self):
        # Collect all Keys in a big list and remove double counts
        keys = []
        for e in self._engines:
            keys += e.dataItems.keys()     # add keys of each engine
            keys = list(set(keys))          # remove all double entries
        keys = sorted(keys, key=str.lower)
        dd = []
        for k in keys:                      # for all keys in all Val Engines
            for e in self._engines:         # iterate through al engines
                if k in e.dataItems.keys():
                    d = e.dataItems.get(k, None)  # get dataItem dict
                    if d.get('name', None):                 # if value exists
                        dd.append([
                            d.get('name', None),
                            d.get('unit', None),
                            d.get('id', None)
                        ])
                        break
        return pd.DataFrame(dd, columns=['name', 'unit', 'id'])

    @ property
    def properties(self):
        """ Asset Data properties DataFrame """
        # Collect all Keys in a big list and remove double counts
        keys = []
        for e in self._engines:
            keys += e.properties.keys()  # add keys of each engine
            keys = list(set(keys))  # remove all double entries
        keys = sorted(keys, key=str.lower)
        try:
            keys.remove('IB ItemNumber Engine')
            keys.insert(0, 'IB ItemNumber Engine')
        except ValueError:
            raise
        # Collect all values in a Pandas DateFrame
        loc = [[e.get_property(k)
                for k in keys] + [e.Name] for e in self._engines]
        return pd.DataFrame(loc, columns=keys + ['Name'])

    @ property
    def dataItems(self):
        """ Asset Data dataItems list """
        # Collect all Keys in a big list and remove double counts
        keys = []
        for e in self._engines:
            keys += e.dataItems.keys()
            keys = list(set(keys))
        keys = sorted(keys, key=str.lower)
        loc = [[e.get_dataItem(k)
                for k in keys] + [e.Name] for e in self._engines]
        return pd.DataFrame(loc, columns=keys + ['Name'])

    @ property
    def validation_definition(self):
        """ Validation Definition as pandas DataFrame
            defined in Excel sheet 'validation' """
        return self._val

    @ property
    def engines(self):
        return self._engines

    def eng(self, n):
        """ Return the n's Engine Validation Definition """
        return self._val.iloc[n]
