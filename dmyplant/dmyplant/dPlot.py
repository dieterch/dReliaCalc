
# Standard Library imports
from datetime import datetime
import pandas as pd
import numpy as np
from pprint import pprint as pp
import statistics
import sys
import time

# Third party imports
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as dates

# Load Application imports
from dmyplant.dReliability import demonstrated_reliability_sr


def idx(n, s, e, x):
    return int(n * (x - s) / (e - s) + 1)


def demonstrated_Reliabillity_Plot(vl, beta=1.21, T=20000, s=1000, ft=pd.DataFrame, cl=[10, 50, 90]):

    # define milestones
    v_ts = vl.valstart_ts  # val start
    n_ts = vl.now_ts  # now
    en = T
    ep = en - (n_ts - v_ts) / 3600  # extrapolation
    l_ts = vl.now_ts + ep * 3600.0  # the end :-)

    s = s  # points
    b = beta
    fcol = 'grey'

    # tr1 = dmyplant.vl.demonstrated_reliability(
    #     extrapolate_by_h=ep, beta=b, size=s)[0]  # timestamp x axis start .. end

    tr = demonstrated_reliability_sr(vl,
                                     v_ts, l_ts, beta=b, size=s, ft=ft)[0]  # timestamp x axis start .. end
    n_i = idx(s, v_ts, l_ts, n_ts)
    n_tr = tr[0:n_i:1]  # x axis start .. now

    # date start .. end
    dtr = [datetime.fromtimestamp(t) for t in tr]  # date start .. end
    rel = {c: demonstrated_reliability_sr(vl, v_ts, l_ts,
                                          CL=c/100.0, beta=b, size=s, ft=ft)[1] for c in cl}
    # rel = {c: dmyplant.vl.demonstrated_reliability2(
    #     CL=c/100.0, extrapolate_by_h=ep, beta=b, size=s)[1] for c in cl}
    n_dtr = [datetime.fromtimestamp(t) for t in n_tr]  # date start .. now
    n_rel = {c: rel[c][0:n_i:1] for c in cl}

    fig, ax1 = plt.subplots(  # pylint: disable=unused-variable
        figsize=(12, 8), constrained_layout=True)
    #fig, (ax1, ax3) = plt.subplots(2, figsize=(6, 6))
    color = 'tab:red'
    ax1.set_xlabel('date')
    ax1.set_ylabel('Demonstrated Reliability [%]', color=color)
    ax1.set_title('Demonstrated Reliability [%]')

    # plot demonstrated reliability
    for CL in cl:
        ax1.plot(dtr, rel[CL], color=fcol, linestyle='-', linewidth=0.5)
        ax1.plot(n_dtr, n_rel[CL], color='red', linestyle='-', linewidth=0.7)
    ax1.tick_params(axis='y', labelcolor=color)

    ax1.axis((datetime.fromtimestamp(v_ts),
              datetime.fromtimestamp(l_ts), 0, 100))
    ax1.yaxis.set_major_locator(ticker.LinearLocator(13))
    locator = dates.AutoDateLocator()
    locator.intervald[dates.MONTHLY] = [1]
    ax1.xaxis.set_major_locator(locator)
    ax1.grid(color='lightgrey')

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    le = vl.engines[:]
    for e in le:
        #print(e.Name, e._d['Engine ID'], e._d['val start'], e._d['oph parts'])
        y = [e.oph(t) for t in tr]
        ax2.plot(dtr, y, linewidth=0.5, color=fcol)
        n_y = [e.oph(t) for t in n_tr]
        ax2.plot(n_dtr, n_y)

    # max possible runtime line
    y = [(t-v_ts) / 3600.0 for t in tr]
    ax2.plot(dtr, y, color='grey', linestyle='--', linewidth=0.7)

    # actual date line
    ax1.axvline(datetime.now(), color='red',
                linestyle='--', linewidth=0.7)

    # 1% horizontal lines
    # for lev in range(0, 100):
    # ax1.axhline(lev, color='grey', linestyle='-', linewidth=0.3)

    # Point max CL Reliability@now
    myrel_y = float(
        rel[max(cl)][int((vl.now_ts-v_ts)/(l_ts - v_ts)*s)])
    myrel_x = datetime.fromtimestamp(vl.now_ts)
    ax1.scatter(myrel_x, myrel_y, marker='o', color='black', label='point')
    txt = f"CL {max(cl)}%@{30000}\nbeta={b}\nR={myrel_y:.1f}%"
    # txt = 'ttt'
    myrel_txt_x = datetime.fromtimestamp(vl.now_ts + 200000)
    ax1.text(myrel_txt_x, myrel_y - 9, txt)
    #x1, x2, y1, y2 = ax1.axis()
    ax1.axis((datetime.fromtimestamp(v_ts),
              datetime.fromtimestamp(l_ts), 0, 120))
    # oph Fleet Leader
    fl = [e.oph(n_ts) for e in vl.engines]
    fl_point_x = datetime.fromtimestamp(vl.now_ts)
    ax2.scatter(fl_point_x, max(fl), marker='o', color='black', label='point')
    fl_txt_x = datetime.fromtimestamp(vl.now_ts + 200000)
    txt = f'{len(fl)} engines\nmax {max(fl):.0f}h\ncum {sum(fl):.0f}h\navg {statistics.mean(fl):.0f}h\n{datetime.now():%d.%m.%Y %H:%M}'
    ax2.text(fl_txt_x, max(fl) - T/7, txt)
    #x1, x2, y1, y2 = ax2.axis()
    ax2.axis((datetime.fromtimestamp(v_ts),
              datetime.fromtimestamp(l_ts), 0, 24000))
    color = 'tab:blue'
    # we already handled the x-label with ax1
    ax2.set_ylabel('hours [h]', color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.yaxis.set_major_locator(ticker.LinearLocator(13))

    # x1, x2, y1, y2 = ax3.axis()
    # ax3.axis((datetime.fromtimestamp(v_ts),
    #           datetime.fromtimestamp(l_ts), 0, 100))

    # ax3.plot(dtr, fail)

    plt.show()


if __name__ == '__main__':
    pass
