import sys
from datetime import datetime as dt
from datetime import timedelta
import matplotlib.dates as mdates
from myplot import graph_plot

dirstr = '/home/mat/Documents'
s_format = '%Y-%m-%d'
today = dt.now()
if len(sys.argv) > 1:
    today = dt.strptime(sys.argv[1], s_format)
startstr = (today - timedelta(days=6)).strftime(s_format)

datelist, list0 = [], []
for i in range(7):
    day = today - timedelta(days=(6-i))
    datelist.append(day.strftime(s_format))

if sys.argv==2:
    for fname in datelist:
        try:
            with open(dirstr + "/data/" + fname + ".txt") as f:
                for line in f:
                    datestr = line[:20].strip()
                    datev = mdates.datestr2num(datestr)
                    value = float(line[25:].strip())
                    list0.append([datev, value])
        except FileNotFoundError:
            continue
else:
    while True:
        try:
            line = input()
            for i, l in enumerate(line.split('\t')):
                temp = l.strip()
                if len(temp)>0:
                    if i==0:
                        startstr = temp[:10]
                        datev = mdates.datestr2num(temp)
                    else:
                        value = float(temp)
            list0.append([datev, value])
        except EOFError:
            break
title = 'Smell Level : ' + startstr + ' (Weekly)'
fig = graph_plot(list0, title)
#fig.savefig(dirstr + '/figs/' + startstr + '.png')
