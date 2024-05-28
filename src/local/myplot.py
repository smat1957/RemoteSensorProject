import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib.dates as mdates

def chop(daystr):
    x, y = [], []
    for dstr in daystr.split('\n'):
        if len(dstr)>0:
            datev = mdates.datestr2num(dstr[:20])
            x.append(datev)
            value = float(dstr[25:].strip())
            y.append(value)
    return x, y

def graph_plot(datalist, titlestr):
    x, y = [], []
    for daystr in datalist:
        x0, y0 = chop(daystr)
        x.extend(x0)
        y.extend(y0)
    ymax, ymin, yave = max(y), min(y), np.mean(y)
    title = titlestr + f'Min={ymin:0.3f}, Max={ymax:0.3f}, Mean={yave:0.3f}'
    matplotlib.style.use('ggplot')
    fig, ax = plt.subplots()
    step = (ymax - ymin) / 10.0
    ymax = ((ymax//step)+1)*step+step/2.0
    ymin = (ymin//step)*step-step/2.0
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.set_ylim([ymin, ymax])
    ax.set_xlabel('Date-Time')
    ax.set_ylabel('Volt')
    ax.set_title(title)
    ax.plot(x, y)
    plt.show()
    return fig

def graph_plots(datalist, titlestr, rows, cols):
    ymax, ymin, yave = -20.0, 20.0, 0.0
    x, y = [], []
    for daystr in datalist:
        x0, y0 = chop(daystr)
        x.append(x0)
        y.append(y0)
        maxi, mini = max(y0), min(y0)
        ymax = maxi if (maxi>ymax) else ymax
        ymin = mini if (mini<ymin) else ymin
        yave += np.mean(y0)
    yave = yave / len(datalist)
    title = titlestr + f'Min={ymin:0.3f}, Max={ymax:0.3f}, Mean={yave:0.3f}'
    matplotlib.style.use('ggplot')
    fig, ax = plt.subplots(nrows=rows, ncols=cols,\
                           squeeze=False, tight_layout=True,\
                           sharex=None, sharey='row', figsize=(15,9))
    step = (ymax - ymin) / 10.0
    ymax = ((ymax//step)+1)*step+step/2.0
    ymin = (ymin//step)*step-step/2.0
    k = 0
    for i in range(rows):
        for j in range(cols):
            locator = mdates.AutoDateLocator()
            formatter = mdates.ConciseDateFormatter(locator)
            ax[i,j].xaxis.set_major_locator(locator)
            ax[i,j].xaxis.set_major_formatter(formatter)
            ax[i,j].set_ylim([ymin, ymax])
            if k<len(x):
                ax[i,j].plot(x[k], y[k])
                k+=1
            else:
                break
        else:
            continue
        break    
    fig.supxlabel('Date-Time')
    fig.supylabel('Volt')
    fig.suptitle(title)
    plt.show()
    return fig