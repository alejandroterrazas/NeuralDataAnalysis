import numpy as np
from matplotlib import pyplot as plt
import os
import sys
from matplotlib import pyplot as plt
import EEGUtils as eeg
from scipy import signal
import VideoUtils as vu
import GeneralUtils as gu

pvdfile = './RawData/maze_dwPout.pvd'
ts, x, y = vu.readPVDfile(pvdfile)
x /= 8.2
xsmooth = np.abs(np.convolve(x, np.ones(100, dtype=np.int), 'valid'))/100
print(ts[0])/10000
print(ts[-1])/10000

eegfile = sys.argv[1]
eegdata, eegtimestamps = eeg.readEEG(eegfile)
#print(eegtimestamps[0])
#print(eegtimestamps[-1])

fs = 512/.257552
print(len(eegdata))
f, spec_t, Sxx = signal.spectrogram(eegdata, fs, nperseg=1024, noverlap=512)
#print(t[0])
#print(t[-1])

closest_start = gu.take_Closest(spec_t, ts[0]/10000)
spec_start_idx = np.where(spec_t==closest_start)[0][0]

closest_stop = gu.take_Closest(spec_t, ts[-1]/10000)
spec_stop_idx = np.where(spec_t==closest_stop)[0][0]

#new_spec_t is spec_t made to fit the length of xsmooth
new_spec_t = np.linspace(spec_t[spec_start_idx], spec_t[spec_stop_idx], len(xsmooth))

print(len(new_spec_t))
print(len(xsmooth))

#fband=4
#theta = Sxx[4,:]+Sxx[5,:]/2
theta = Sxx[:,spec_start_idx:spec_stop_idx]
thetat = spec_t[spec_start_idx:spec_stop_idx]
print(len(theta))
#print(len(thetat))
print("HIPIH")
speed = np.abs(np.diff(xsmooth))
newt = np.linspace(spec_t[spec_start_idx], spec_t[spec_stop_idx], len(speed))

fband = 3
plt.subplot(2,1,1)
plt.plot(thetat,theta[fband,]/np.max(theta[fband,:]),'k')
plt.plot(new_spec_t,xsmooth/np.max(xsmooth),'r')
plt.title(f[fband])
#plt.subplot(2,1,2)
#plt.plot(thetat,theta[fband,:]/np.max(theta[fband,:]))
plt.plot(newt, speed/np.max(speed),'g')
#plt.show()


fband = 4
plt.subplot(2,1,2)
plt.plot(thetat,theta[fband,]/np.max(theta[fband,:]),'k')
plt.plot(new_spec_t,xsmooth/np.max(xsmooth),'r')
plt.title(f[fband])
#plt.subplot(2,1,2)
#plt.plot(thetat,theta[fband,:]/np.max(theta[fband,:]))
plt.plot(newt, speed/np.max(speed),'g')
plt.show()


plt.pcolormesh(t, f, Sxx)
