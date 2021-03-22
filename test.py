import arrow
import dmyplant2
import pandas as pd
from pprint import pprint as pp
import numpy as np
from tabulate import tabulate
import logging
import sys
import traceback

logging.basicConfig(
    filename='dmyplant.log',
    filemode='w',
    format='%(asctime)s %(levelname)s, %(message)s',
    level=logging.INFO
)
hdlr = logging.StreamHandler(sys.stdout)
logging.getLogger().addHandler(hdlr)


def main():
    try:
        # load input data from files
        dval = pd.read_csv("input_test.csv", sep=';', encoding='utf-8')
        dval['val start'] = pd.to_datetime(
            dval['val start'], format='%d.%m.%Y')

        # create dmyplant 2 instances
        from dmyplant2 import cred
        mp = dmyplant2.MyPlant(7200)
        vl = dmyplant2.Validation(mp, dval, cui_log=False)

        print("Detailed Investigateion ")
        e = vl.eng_serialNumber(1225799)

        pp(e.dash)

        #dtrips = e.batch_hist_alarms(p_severities=[800], p_offset=0, p_limit=5)
        # dtrips = e.batch_hist_alarms(
        #     p_severities=[500],
        #     p_from=arrow.get(e.val_start).to('Europe/Vienna'),
        #     p_to=arrow.now('Europe/Vienna'),
        # )
        # dtrips['datetime'] = pd.to_datetime(
        #     dtrips['timestamp'] * 1000000.0).dt.strftime("%m-%d-%Y %H:%m")
        # print(tabulate(dtrips[['datetime', 'message', 'name', 'severity']]))

        # define and downlad data for plot
        dat = {
            # 161: 'CountOph',
            102: 'PowerAct',
            # 217: 'Hyd_PressCrankCase',
            # 16546: 'Hyd_PressOilDif'
        }

        df = e.batch_hist_dataItems(
            itemIds=dat,
            # p_from=arrow.get(e.val_start).to('Europe/Vienna'),
            # p_from=arrow.get(
            #    '2021-01-03 07:00').to('Europe/Vienna'),
            # p_to=arrow.now('Europe/Vienna'),
            p_to=arrow.get('2021-03-06 00:00').to('Europe/Vienna'),
            p_limit=40000,
            timeCycle=3600  # sec. adjust the intevall if you get errors
        )

        pp(df)
        # Set Type of time column to DateTime
        # df['datetime'] = pd.to_datetime(df['time'] * 1000000)
        # df['CountOph'] = df.CountOph - e._d['oph@start']

        # and plot the overview
        dmyplant2.chart(df, [
            {'col': ['PowerAct'], 'ylim':(0, 5000)},
            #{'col': ['CountOph'], 'ylim':(0, 500)},
            #{'col': ['Hyd_PressCrankCase'], 'ylim': [-50, 20]},
            #{'col': ['Hyd_PressOilDif'], 'ylim':(0, 1)}
        ],
            title=e,
            figsize=(12, 8),
        )
    except Exception as e:
        print(e)
        traceback.print_tb(e.__traceback__)
    finally:
        hdlr.close()
        logging.getLogger().removeHandler(hdlr)


if __name__ == '__main__':
    main()
