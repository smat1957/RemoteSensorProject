import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib.dates as mdates
from datetime import datetime as dt
from datetime import timedelta
import sys, time

class RTPlot:
    def dateproc(self):
        #s_format = '%Y-%m-%d, %H:%M:%S'
        s_format0 = '%Y-%m-%d, 00:00:00'
        today = dt.now()
        tomor = today + timedelta(days=1)
        self.todaystr = today.strftime(s_format0)
        self.tomorstr = tomor.strftime(s_format0)

    def readdata(self, fname):
        try:
            with open(fname, 'r') as f:
                for line in f:
                    self.chop(line)
        except FileNotFoundError:
            print(f'File{fname} not found')

    def __init__(self, fname):
        self.fname = fname
        self.x = []
        self.y = []
        self.ims = []
        self.dateproc()
        self.readdata(fname)
        self.fig, self.ax = plt.subplots()
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)
        self.ax.xaxis.set_major_locator(locator)
        self.ax.xaxis.set_major_formatter(formatter)
        xmin = mdates.datestr2num(self.todaystr)
        xmax = mdates.datestr2num(self.tomorstr) 
        self.ax.set_xlim([xmin, xmax])
        ymin, ymax = 0.52, 1.25
        self.ax.set_ylim([ymin, ymax])
        self.ax.set_title("Smel Level : " + self.todaystr[:10] +\
                          " :Real time plot")
        self.ax.set_xlabel('Date-Time')
        self.ax.set_ylabel('Volt')
        matplotlib.style.use('ggplot')
        im, = self.ax.plot(self.x, self.y)
        self.ims.append(im)

    def tail_f(self):
        try:
            with open(self.fname, 'r') as f:
                f.seek(0, 2)
                while True:
                    line = f.readline()
                    if not line:
                        time.sleep(1)
                        continue
                    return line.strip()
        except FileNotFoundError:
            print(f'File{self.fname} not found')
        return ""

    def chop(self, line):
        datestr = line[:20].strip()
        datev = mdates.datestr2num(datestr)
        value = float(line[25:].strip())
        self.x.append(datev)
        self.y.append(value)

    def update(self):
        if len(self.ims) > 0:
            im = self.ims.pop()
            im.remove()
        im, = self.ax.plot(self.x, self.y)
        self.ims.append(im)
    
if __name__=="__main__":
    dirstr = '/home/mat/Documents'
    fname = dirstr + '/w.txt'
    if len(sys.argv) > 1:
        fname = dirstr + '/' + sys.argv[1]
    rtp = RTPlot(fname)
    tomorrow = dt.now() + timedelta(days=1)
    while dt.now() < tomorrow:
        plt.pause(1)
        line = rtp.tail_f()
        print("[info.log]", line)
        rtp.chop(line)
        rtp.update()
    rtp.fig.savefig(dirstr+'/R_'+rtp.todaystr+'.png')

