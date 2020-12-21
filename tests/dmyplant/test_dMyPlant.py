from unittest import TestCase
from pprint import pprint as pp
import pandas as pd

import dmyplant
from dmyplant.dMyplant import MyPlant, cts


class Test_dMyplant(TestCase):

    assert cts(1608471671) == 1608471671.0
    assert cts(1608471671000) == 1608471671.0

    def test_Constructor(self):
        mp = MyPlant(7200)
        assert mp._name != ""
        assert mp._password != ""

    def test_login(self):
        mp = MyPlant(7200)
        mp.login()
        assert mp._session != None
        mp.logout()
        assert mp._session == None

    def test_logout(self):
        mp = MyPlant(7200)
        mp.logout()
        assert mp._session == None

    def test_assetdata(self):
        mp = MyPlant(7200)
        mp.login()
        sn = '1386177'
        res = mp.asset_data(sn)

        # res['dataItems'] = {}
        # pp(res)

        erg2 = mp.gdi(res, 'properties', 'IB ItemNumber Engine')
        assert erg2 == sn

        erg2 = mp.gdi(res, 'nokey', 'id')
        assert erg2 == 130891

        assert res['serialNumber'] == sn
        # ts = mp.to_myplant_ts(1608471671)
        # assert ts == 1608471671000
        erg = mp.historical_dataItem(
            130891, 161, 1608471671000)
        assert erg['value'] == 8065.0
        assert erg['name'] == 'Count_OpHour'

        # ts2 = mp.d(1608471671)
        # assert ts2 == pd.Timestamp('2020-12-20 13:41:11')
        # assert mp.from_myplant_ts(ts) == 1608471671
        # assert mp.future_timestamp(1608471671, 1) == 1608471671 + 3600
        assert mp.caching == 7200
        mp.logout()

    def test_login_fail(self):
        mp = MyPlant(7200)
        mp._name = "Y2VsNDZ0ZWN1"
        with self.assertRaises(dmyplant.dMyplant.MyPlantException):
            mp.login()
        mp.logout()
