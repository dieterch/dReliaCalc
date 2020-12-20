
# Standard Library imports
from datetime import datetime
import logging
from pprint import pprint as pp
import sys
import traceback

# Third party imports
import numpy as np
import pandas as pd

# Load application imports
import dmyplant
from dmyplant import cred, Validation, MyPlant, EngineReadOnly, dPlot as pl


logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(asctime)s %(levelname)s, %(message)s',
    level=logging.INFO
)
hdlr = logging.StreamHandler(sys.stdout)
logging.getLogger().addHandler(hdlr)

# Validation Excel Workbook Name
# needs to be in the current working directory
VAL = 'input.xlsx'


def main():
    try:
        logging.info('CUI Application Started')

        # Read Excel, Definition of Validation
        xl = pd.ExcelFile(VAL)
        dval = xl.parse("validation")
        dfail = xl.parse("failures")
        pp(dfail)

        e0 = EngineReadOnly(dval.iloc[0]['serialNumber'])
        delta = e0.time_since_last_server_contact
        cacheing = 7200
        if cacheing - delta < 0:
            logging.info(
                f"MyPlant Data Cache interval {cacheing} s passed, contacting Server.")
        else:
            logging.info(
                f"MyPlant Data Cache Interval {cacheing}s, cache expiring in {(cacheing - delta):.0f}s.")

        cred()
        mp = MyPlant(cacheing)  # no parameter = 7200s caching time
        vl = Validation(mp, dval)

        # demonstrated_Reliabillity_Plot(beta=1.21, T=20000, s=1000, cl=[0.1, 0.5, 0.9])
        nofail = pd.DataFrame([])
        pl.demonstrated_Reliabillity_Plot(
            vl, beta=1.4, T=10000, s=1000, ft=nofail, cl=[10, 50, 90])

        logging.info('CUI dmyplantlication Run successfully completed.')

    except Exception as e:
        print(e)
        traceback.print_tb(e.__traceback__)
    finally:
        hdlr.close()
        logging.getLogger().removeHandler(hdlr)


if __name__ == '__main__':
    main()
