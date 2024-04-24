import numpy as np
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
        matplotlib.style.use('ggplot')
        self.fig, self.ax = plt.subplots()
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)
        self.ax.xaxis.set_major_locator(locator)
        self.ax.xaxis.set_major_formatter(formatter)
        xmin = mdates.datestr2num(self.todaystr)
        xmax = mdates.datestr2num(self.tomorstr) 
        self.ax.set_xlim([xmin, xmax])
        self.yrange()
        self.ax.set_xlabel('Date-Time')
        self.ax.set_ylabel('Volt')
        self.update()

    def tail_f(self):
        try:
            with open(self.fname, 'r') as f:
                f.seek(0, 2)
                enter = dt.now()
                while True:
                    line = f.readline()
                    if not line:
                        time.sleep(1)
                        if dt.now()-enter < timedelta(minutes=6):
                            continue
                        return
                    return line.strip()
        except FileNotFoundError:
            print(f'File{self.fname} not found')
        return

    def chop(self, line):
        datestr = line[:20].strip()
        datev = mdates.datestr2num(datestr)
        value = float(line[25:].strip())
        self.x.append(datev)
        self.y.append(value)

    def statvalue(self):
        self.ymax = np.array(self.y).max()
        self.ymin = np.array(self.y).min()
        self.mean = np.array(self.y).mean()
        str1 = f"Max={self.ymax:.2f}, "
        str2 = f"Min={self.ymin:.2f}, "
        str3 = f"Mean={self.mean:.2f}"
        self.ax.set_title("Smel Level : " + str1 + str2 + str3)
        
    def yrange(self):
        self.statvalue()
        step = (self.ymax - self.ymin)/10.0
        v = 0
        while self.ymax > v:
            v += step
        ymax = v
        while self.ymin < v:
            v -= step
        ymin = v
        ymax += step/2.0
        ymin -= step/2.0
        self.ax.set_ylim([ymin, ymax])
        
    def update(self):
        self.yrange()
        if len(self.ims) > 0:
            im = self.ims.pop()
            im.remove()
        im, = self.ax.plot(self.x, self.y, color="red")
        self.ims.append(im)
    
if __name__=="__main__":
    dirstr = '/home/mat/Documents'
    fname = dirstr + '/w.txt'
    if len(sys.argv) > 1:
        fname = dirstr + '/' + sys.argv[1]
    rtp = RTPlot(fname)
    tomorrow = dt.strptime(rtp.tomorstr, '%Y-%m-%d, 00:00:00')
    while dt.now() < tomorrow:
        plt.pause(1)
        line = rtp.tail_f()
        if line is not None:
            print("[info.log]", line)
            rtp.chop(line)
            rtp.update()
    rtp.fig.savefig(dirstr+'/figs/R_'+rtp.todaystr[:10]+'.png')

