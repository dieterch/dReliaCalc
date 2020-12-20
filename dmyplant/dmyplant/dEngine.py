from datetime import datetime, timedelta
from pprint import pprint as pp
import pandas as pd
import xlwings as xw
# if __name__ != '__main__':
#     import dmyplant
from dmyplant.dMyplant import cts
import sys
import os
import pickle
import logging
import json


class Engine(object):
    """ dmyplant Engine Class
        mp  .. MyPlant Object
        eng .. Pandas Validation Input DataFrame
    """
    sn = 0
    picklefile = ''
    _properties = {}
    _dataItems = {}
    _k = None
    _P = 0.0

    def __init__(self, mp, eng):
        """ Engine Constructor
            load Instance from Pickle File or
            load Instance Data from Myplant
            if Myplant Cache Time is passed"""

        # read engine Myplant Serial Number from Validation Definition
        self._mp = mp
        self.sn = str(eng['serialNumber'])
        fname = os.getcwd() + '/data/' + self.sn
        self.picklefile = fname + '.pkl'    # load persitant data
        self.lastcontact = fname + '_lastcontact.pkl'
        try:
            with open(self.lastcontact, 'rb') as handle:
                self._last_fetch_date = pickle.load(handle)
        except:
            pass
        try:
            # fetch data from Myplant only on conditions below
            if self._cache_expired()['bool'] or (not os.path.exists(self.picklefile)):
                local_asset = self._mp.asset_data(self.sn)
                logging.debug(
                    f"{eng['Validation Engine']}, Engine Data fetched from Myplant")
                self.asset = self._restructure(local_asset)
                self.d = self._engine_data(eng)
                self.Name = eng['Validation Engine']
                self.set_oph_parameter()
                self._last_fetch_date = cts(datetime.now().timestamp())
                self._save()
            else:
                with open(self.picklefile, 'rb') as handle:
                    self.__dict__ = pickle.load(handle)
        except FileNotFoundError:
            logging.debug(
                f"{self.picklefile} not found, fetch Data from MyPlant Server")
        else:
            logging.debug(
                f"{__name__}: in cache mode, load data from {self.sn}.pkl")
        finally:
            logging.debug(f"Initialize Engine Object, SerialNumber: {self.sn}")

    @property
    def time_since_last_server_contact(self):
        """
        get time since last Server contact
        """
        now = datetime.now().timestamp()
        delta = now - self.__dict__.get('_last_fetch_date', 0.0)
        return delta

    def _cache_expired(self):
        """
        time has since last Server contact
        returns (delta -> float, passed -> boolean)
        """
        delta = self.time_since_last_server_contact
        return {'delta': delta, 'bool': delta > self._mp.caching}

    def _restructure(self, local_asset):
        """
        Restructure Asset Data, add Variable
        Item names as dict key in dataItems & Properties
        """
        local_asset['properties'] = {
            p['name']: p for p in local_asset['properties']}
        local_asset['dataItems'] = {
            d['name']: d for d in local_asset['dataItems']}
        return local_asset

    def set_oph_parameter(self):
        """
        Calculate line parameters, oph - line
        """
        self._k = float(self.d['oph parts']) / \
            (self._lastDataFlowDate - self._valstart_ts)

    def oph(self, ts):
        """
        linear inter- and extrapolation of oph(t)
        t -> timestamp
        """
        y = self._k * (ts - self._valstart_ts)
        y = y if y > 0.0 else 0.0
        return y

    def _engine_data(self, eng) -> dict:
        """
        Extract basic Engine Data
        pd.DataFrame eng, Validation Definition
        """
        def calc_values(d) -> dict:
            oph_parts = float(d['Count_OpHour']) - float(d['oph@start'])
            d.update({'oph parts': oph_parts})
            return d

        dd = {}
        from_asset = {
            'nokey': ['serialNumber', 'status', 'id', 'model'],
            'properties': ['Engine Version', 'Engine Type', 'IB Unit Commissioning Date', 'Design Number',
                           'Engine ID', 'IB Control Software', 'IB Item Description Engine', 'IB Project Name'],
            'dataItems': ['Count_OpHour', 'Count_Start']}

        for key in from_asset:
            for ditem in from_asset[key]:
                dd[ditem] = self.get_data(key, ditem)

        dd['Name'] = eng['Validation Engine']
        dd['P'] = int(str(dd['Engine Type'])[-2:])
        self._P = dd['P']
        dd['val start'] = eng['val start']
        dd['oph@start'] = eng['oph@start']
        # add calculated items
        dd = calc_values(dd)
        self._valstart_ts = cts(dd['val start'].timestamp())
        self._lastDataFlowDate = cts(dd['status'].get(
            'lastDataFlowDate', None))
        return dd

    def _save(self):
        """
        Persistant data storage to Pickle File
        """
        try:
            with open(self.lastcontact, 'wb') as handle:
                pickle.dump(self._last_fetch_date, handle, protocol=4)
        except FileNotFoundError:
            errortext = f'File {self.lastcontact} not found.'
            logging.error(errortext)
        try:
            with open(self.picklefile, 'wb') as handle:
                pickle.dump(self.__dict__, handle, protocol=4)
        except FileNotFoundError:
            errortext = f'File {self.picklefile} not found.'
            logging.error(errortext)
            # raise Exception(errortext)

    def get_data(self, key, item):
        """
        Get Item Value by Key, Item Name pair
        valid Keys are
        'nokey' data Item in Asset Date base structure
        'properties' data Item is in 'properties' list
        'dataItems' data Item is in 'dataItems' list
        """
        return self.asset.get(item, None) if key == 'nokey' else self.asset[key].setdefault(item, {'value': None})['value']

    def get_property(self, item):
        """
        Get properties Item Value by Item Name
        """
        return self.get_data('properties', item)

    def get_dataItem(self, item):
        """
        Get  dataItems Item Value by Item Name
        """
        return self.get_data('dataItems', item)

    @ property
    def P(self):
        return self._P

    @ property
    def properties(self):
        return self.asset['properties']

    @ property
    def dataItems(self):
        return self.asset['dataItems']

    @ property
    def valstart_ts(self):
        return self._valstart_ts


class EngineReadOnly(Engine):
    """ Read Only Version Engine"""

    def __init__(self, sn):
        """ Engine Constructor
        load Instance from Pickle File"""
        self
        self.sn = str(sn)
        self.picklefile = os.getcwd() + '../data/' + self.sn + '.pkl'
        try:
            with open(self.picklefile, 'rb') as handle:
                self.__dict__.update(pickle.load(handle))
        except FileNotFoundError:
            logging.debug(f"{self.picklefile} not found.")


if __name__ == '__main__':
    import traceback
    import dmyplant

    try:
        eng = EngineReadOnly('1386177')
        pp(eng.__dict__)

    except Exception as e:
        print(e)
        traceback.print_tb(e.__traceback__)
