import VideoUtils as vu
import TetrodeUtils as tu
import sys
import struct
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from bisect import bisect_left
import EEGUtils as eeg


import numpy as np

def readTFile(filename):

  with open(filename, 'rb') as f:  
    #hdr = f.read()[:16384]
    #print(hdr)
    tsdata  = f.read()
    recsize = 8
    nevents = int(len(tsdata)/recsize)
    print("nevents: {}".format(nevents))

    ts = np.zeros(nevents)
 
    for i in range(nevents):
      recoffset=recsize*i
      dnParams = np.zeros(8)
      #print recoffset
      ts[i] = struct.unpack('d', tsdata[recoffset:recoffset+8])[0]
  return ts

eegfile="./05-04POS/BestTheta.Ncs"
eegdata, eegts = eeg.readEEG(eegfile)

#spikets = readTFile("../RawData/Sc10_5.t")
spikets = readTFile(sys.argv[1])

npzfile = np.load("./05-04POS/thetapeaks.npz")
peaks=npzfile['theta_peaks']
troughs=npzfile['theta_troughs']
#print peaks[:10]

event_flags = np.zeros(10)
print eegts[:10]
print spikets[:10]

for i in range(10):
    event_flags[i]  = eeg.takeClosest(eegts, spikets[i])
    closest= eeg.takeClosest(eegts,spikets[i])
    print closest 


phases = eeg.returnPhases(peaks, troughs, event_flags)
print phases

