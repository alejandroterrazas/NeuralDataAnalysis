import numpy as np
from matplotlib import pyplot as plt
import os
import sys
import pandas as pd
import TetrodeUtils as tu
import GeneralUtils as gu
import VideoUtils as vu
import EEGUtils as eeg
import peakutils

def returnPeakIndices(eegvals, m, t):
     ind_peaks = peakutils.indexes(eegvals, thres=t, min_dist=m)
     ind_troughs = peakutils.indexes(eegvals*-1, thres=t, min_dist=m)
     return ind_peaks, ind_troughs


pvdfile = sys.argv[1]

ts, x, y = vu.readPVDfile(pvdfile)
x /= 8.2
xsmooth = np.abs(np.convolve(x, np.ones(50, dtype=np.int), 'valid'))/50

#8.2 pixels per centimer
#use later to detect direction
direction = np.where(np.diff(xsmooth)>0, 1, 0)

cum = np.cumsum(np.abs(np.diff(xsmooth)))

inotmoving = np.where(np.diff(cum)<.05)[0]
imoving = np.where(np.diff(cum)>=.1)[0]

#plt.plot(np.linspace(0,len(x), len(x)), x, 'k.')
#plt.plot(ts, x, 'k.')
#plt.plot(ts[imoving], x[imoving], 'r.')
#plt.show()
#peaks, troughs = returnPeakIndices(xfilt ,600, .25).show()

grouped = gu.group_consecutives(imoving)

eegfile = sys.argv[2]
eegdata, eegtimestamps = eeg.readEEG(eegfile)

fs = 512/.257552
print(eegtimestamps[:10])

speeds = []
thetas = []

for group in grouped:
  distance = np.abs(xsmooth[group[0]]-xsmooth[group[-1]])
  laptime = (ts[group[-1]]-ts[group[0]])/1000
  speed = distance/laptime
  if distance > 20:
#    print(ts[group[0]])
#    print(ts[group[-1]])
  
    EEGstart = eeg.takeClosest(eegtimestamps, ts[group[0]]*100)
    EEGstop = eeg.takeClosest(eegtimestamps, ts[group[-1]]*100)
    startidx = np.where(eegtimestamps==EEGstart)[0][0]*512
    stopidx =  np.where(eegtimestamps==EEGstop)[0][0]*512
    #print(startidx)
    #print(stopidx)
    #plt.plot(eegdata[startidx:stopidx])
    #plt.show()
    speeds.append(speed)

    ps  = eeg.returnPowerSpectrum(eegdata[startidx:stopidx])
    plt.plot(ps[1:20])
    plt.show()
    theta = np.sum(ps[6:11])/ps[0]
    print('***************')
    print(ps[6:10])
    thetas.append(theta)
    print("distance: {}, laptime: {}, speed: {}, theta {}".format(distance, laptime, speed, theta))
    print('***************')
    #print(theta)
#plt.plot(speeds)
#plt.show()
#print(grouped[0])

