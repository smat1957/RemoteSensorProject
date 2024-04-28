# https://matplotlib.org/stable/api/dates_api.html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib.dates as mdates

def graph_plot(list0, dirstr, datestr, weekly=False):
    df = pd.DataFrame(list0, columns=["DateVal", "Value"])
    matplotlib.style.use('ggplot')
    fig, ax = plt.subplots()
    x = df.loc[:,"DateVal"].values
    y = df.loc[:,"Value"].values
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    #ymax = np.array([y.max(), 1.45]).max()
    #ymin = np.array([y.min(), 0.25]).min()
    ymin, ymax = y.min(), y.max()
    step = (ymax - ymin) / 10.0
    v = 0
    while ymax > v:
        v += step
    ymax = v + step / 2.0
    while ymin < v:
        v -= step
    ymin = v - step / 2.0
    ax.set_ylim([ymin, ymax])
    ax.set_xlabel('Date-Time')
    ax.set_ylabel('Volt')
    if weekly:
        titlestr = "Smel Level : " + datestr + "(Weekly)"
        figpath = dirstr + "/figs/" + "Weekly_" + datestr
    else:
        titlestr = "Smel Level : " + datestr
        figpath = dirstr + "/figs/" + datestr
    ax.set_title(titlestr)
    ax.plot(x,y)
    fig.savefig(figpath + '.png')
    plt.show()