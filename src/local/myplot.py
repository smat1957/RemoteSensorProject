# https://matplotlib.org/stable/api/dates_api.html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib.dates as mdates

def graph_plot(list0, titlestr):
    df = pd.DataFrame(list0, columns=["DateVal", "Value"])
    matplotlib.style.use('ggplot')
    fig, ax = plt.subplots()
    x = df.loc[:,"DateVal"].values
    y = df.loc[:,"Value"].values
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ymin, ymax = y.min(), y.max()
    step = (ymax - ymin) / 10.0
    ymax = ((ymax//step)+1)*step+step/2.0
    ymin = (ymin//step)*step-step/2.0
    ax.set_ylim([ymin, ymax])
    ax.set_xlabel('Date-Time')
    ax.set_ylabel('Volt')
    ax.set_title(titlestr)
    ax.plot(x,y)
    plt.show()
    return fig