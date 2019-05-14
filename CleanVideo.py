import VideoUtils as vu
import TetrodeUtils as tu
import sys
import struct
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from bisect import bisect_left
from matplotlib.widgets import Cursor
import pandas as pd
import matplotlib

import numpy as np

print(matplotlib.get_backend())

def nan_helper(y):   
  return np.isnan(y), lambda z: z.nonzero()[0]


def takeClosest(myList, myNumber):
  pos = bisect_left(myList, myNumber)
  if pos == 0:
     return myList[0]
  if pos == len(myList):
     return myList[-1]

  before = myList[pos - 1]
  after = myList[pos]
  rpos = pos

  if after - myNumber < myNumber - before:
     return after
  else:
     return before

def removeItems(event):
#   print("x {}: y {}".format(event.xdata, event.ydata))
   global xfilt, yfilt, x, y
   yy = event.ydata
   xx = event.xdata
   if xx != None and yy != None:
   #badindex=np.where((y < y+50))
     badindex=np.where((yfilt < yy+5000) & (yfilt > yy-5000) & (xfilt < xx+5000) & (xfilt > xx-5000))
     if np.size(badindex) > 0:
#     print badindex[0]
       x[badindex[0]] = np.nan
       y[badindex[0]] = np.nan
       xfilt[badindex[0]] = np.nan
       yfilt[badindex[0]] = np.nan
    #   print(np.isnan(x))
     
       l1.set_xdata(xfilt[0:len(xfilt)])
       l1.set_ydata(yfilt[0:len(yfilt)])
  

       plt.show()

sys.setrecursionlimit(100000)

vidfile = './RawData/VT1.Nvt'

with open(vidfile, 'rb') as f:
    videodata = f.read()[16384:]
    f.close()
 
npzfile=np.load("./RawData/EPOCHS.npz")
start_idx = int(npzfile['arr_0'])
stop_idx  = int(npzfile['arr_1'])
print(start_idx)
print(stop_idx)

x, y, ts = vu.getVideodata(videodata)
x = x[start_idx:stop_idx]
y = y[start_idx:stop_idx]
ts = ts[start_idx:stop_idx]

xfilt = vu.smooth(x, window_len=200)
yfilt = vu.smooth(y, window_len=200)

xmin = np.amin(xfilt)
xmax = np.amax(xfilt)
ymin = np.amin(yfilt)
ymax = np.amax(yfilt)

ylim=0

fig, ax = plt.subplots()
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
#cid_release  = fig.canvas.mpl_connect('button_release_event', removeItems)
#cid_press = fig.canvas.mpl_connect('button_press_event', tagItems)
cid_motion = fig.canvas.mpl_connect('motion_notify_event', removeItems)


l1, = plt.plot(xfilt[1:len(xfilt)],yfilt[1:len(yfilt)],'.', markersize=3, color='r')

plt.xlim([np.amin(xfilt)-1000,np.amax(xfilt)+1000])
plt.ylim([np.amin(xfilt)-1000,np.amax(xfilt)+1000])

#plt.show()



class Interp_and_Save(object):
 
     def save(self, event):
        print("save")
        #find the nearest good ts point  
        nansIndx = np.where(np.isnan(x))[0]
        isnumIndx = np.where(~np.isnan(x))[0]
        for nan in nansIndx:
            replacementCandidates = np.where(isnumIndx>nan)[0]
            if replacementCandidates.size != 0:
                rx = x[isnumIndx[replacementCandidates[0]]]
                ry = y[isnumIndx[replacementCandidates[0]]]
                rxfilt = xfilt[isnumIndx[replacementCandidates[0]]]
                ryfilt = yfilt[isnumIndx[replacementCandidates[0]]]
 
            else:
                rx = x[isnumIndx[np.where(isnumIndx<nan)[0][-1]]]
                ry = y[isnumIndx[np.where(isnumIndx<nan)[0][-1]]]
                rxfilt = xfilt[isnumIndx[np.where(isnumIndx<nan)[0][-1]]]
                ryfilt = yfilt[isnumIndx[np.where(isnumIndx<nan)[0][-1]]]

            x[nan] = rx
            xfilt[nan] = rxfilt
            y[nan] = ry
            yfilt[nan] = ryfilt

  
        moving,notmoving,speed = vu.returnMoving(xfilt, yfilt, 30)

        np.savez("./RawData/POSITION", xfilt, yfilt, ts, x, y, moving, notmoving, speed)
       


callback = Interp_and_Save()

axsave = plt.axes([0.81, 0.05, 0.1, 0.075])
bsave = Button(axsave, 'Save')
bsave.on_clicked(callback.save)

plt.show()
