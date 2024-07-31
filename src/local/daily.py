import sys
from datetime import datetime as dt
import matplotlib.dates as mdates
from myplot import graph_plot

dirstr = '/home/mat/Documents'
today = dt.now().strftime('%Y-%m-%d')
argv = len(sys.argv)
if argv==2:
    today = sys.argv[1]
else:
    pass

list0=[]
if argv==2:
    with open(dirstr + "/data/" + today + ".txt") as f:
        for line in f:
            datestr = line[:20].strip()
            datev = mdates.datestr2num(datestr)
            value = float(line[25:].strip())
            list0.append([datev, value])
else:
    while True:
        try:
            line = input()
            for i, l in enumerate(line.split('\t')):
                temp = l.strip()
                if len(temp)>0:
                    if i==0:
                        today = temp[:10]
                        datev = mdates.datestr2num(temp)
                    else:
                        value = float(temp)
            list0.append([datev, value])
        except EOFError:
            break
title = 'Smell Level : ' + today
fig = graph_plot(list0, title)
#fig.savefig(dirstr + '/figs/' + today + '.png')
