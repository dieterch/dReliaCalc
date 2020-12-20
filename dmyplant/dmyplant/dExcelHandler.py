from datetime import datetime
import logging
import os
import pandas as pd
import xlwings as xw

#from pprint import pprint as pp

PATCH = False


class ExcelHandler:
    _wb = None
    _val = None
    _dat = None

    def __init__(self, VAL):
        f = os.getcwd() + '/' + VAL

        if PATCH:
            # Check if Excel Workbook is open
            # 2020_12_06 Patch to mitigate a BUG ?
            # in xlwings. When XLwings opens the Workbook on its
            # own, the Workbook gets currupted. (Observed on MAC)
            xl_ok = False
            if xw.apps.count >= 1:
                if xw.books.count >= 1:
                    xl_ok = VAL in xw.books
                    logging.info(f"Excel Workbook {VAL} is open and ready.")

            if xl_ok:
                try:
                    self._wb = xw.Book(f)
                except FileNotFoundError:
                    logging.error(f"{f} not found.")
                    raise
            else:
                raise Exception(
                    f"\n**** CAUTION: Please open {VAL} before you execute this script. ****\n")
        else:
            try:
                self._wb = xw.Book(f)
            except FileNotFoundError:
                logging.error(f"{f} not found.")
                raise

    def openfile(self):
        # xl.names()
        self.write('ndashboard', 'B2', 'Update in progress')
        dval = self.val
        cacheing = self.cacheing
        return (dval, cacheing)

    @property
    def val(self):
        self._val = self._wb.sheets['validation'].range('A1') \
            .options(pd.DataFrame, header=1, index=False, numbers=int, expand='table').value
        return self._val

    @property
    def cacheing(self):
        return int(self.read('ndashboard', 'F2'))
        # return int(self._wb.sheets['dashboard'].range('E2').value)

    def read(self,  Sheet, Cell,):
        return self._wb.sheets(Sheet).range(Cell).value

    def write(self, Sheet, Cell, Value):
        self._wb.sheets(Sheet).range(Cell).value = Value

    def names(self):
        names = [name.name for name in self._wb.names]
        for name in names:
            print(f"{name} {self._wb.names[name].refers_to}")

    def UpdateNames(self, rows):
        data_rv = str(rows + 4)
        prop_rv = str(rows + 4)
        val_rv = str(rows + 1)
        self._wb.names.add('data_i', "=dataItems!$A$5:$A$" + data_rv)
        self._wb.names.add('data_val', "=dataItems!$A$5:$JNC$" + data_rv)
        self._wb.names.add('prop_i', "=properties!$A$5:$A$" + prop_rv)
        self._wb.names.add('prop_val', "=properties!$A$5:$CB$" + prop_rv)
        self._wb.names.add('val_i', "=validation!$A$2:$A$" + val_rv)
        self._wb.names.add('val_val', "=validation!$A$2:$F$" + val_rv)

    def UpdateVAL(self, vl):
        logging.info(f"Copying properties ...")
        prop = vl.properties
        logging.info(f"Copying properties dictionary ...")
        properties_dict = vl.properties_dict
        # pp(properties_dict)  # print properties_dict to Terminal

        logging.info(f"Copying dataItems ...")
        dataItems = vl.dataItems
        logging.info(f"Copying dataItems dictionary ...")
        dataItems_dict = vl.dataItems_dict
        # pp(dataItems_dict)  # print dataitems_dict to Terminal
        # logging.info(f"Populate Excel dashboard ...")

        # xl.write('dashboard', 'A4', dash)
        logging.info(f"Populate Excel properties ...")
        self.write('properties', 'A4', prop)
        logging.info(f"Populate Excel dataitems ...")
        self.write('dataItems', 'A4', dataItems)
        logging.info(f"Populate Excel dictionaries ...")
        self.write('dictionary', 'H3', properties_dict)
        self.write('dictionary', 'P3', dataItems_dict)

        # xl.UpdateNames(100)

        today = datetime.now()
        self.write('ndashboard', 'B2', today)
