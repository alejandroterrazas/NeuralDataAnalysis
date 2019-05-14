#compare theta band for walking/not walking

import EEGUtils as eeg
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import sys

eegfile = sys.argv[1]
eegdata, eegtimestamps = eeg.readEEG(eegfile)

npzfile = np.load("./RawData/TRAJECTORIES.npz")
tstart=npzfile['arr_0'].astype(int)
tstop=npzfile['arr_1'].astype(int)
tspeed=npzfile['arr_2'].astype(float)

npzfile = np.load("./RawData/NONTRAJECTORIES.npz")
dstart=npzfile['arr_0'].astype(int)
dstop=npzfile['arr_1'].astype(int)
dspeed=npzfile['arr_2'].astype(float)

npzfile = np.load("./RawData/POSITION.npz")
ts=npzfile['arr_2'].astype(float)

print("mean tspeed {}".format(np.mean(tspeed)))


fastindx = [i for i,x in enumerate(tspeed) if x>np.percentile(tspeed,75)]
slowindx = [i for i,x in enumerate(tspeed) if x<np.percentile(tspeed,25)]

#find closest eegtimestamps to tstart, tstop
EEGstart = [eeg.takeClosest(eegtimestamps, ts[start]) for start in tstart]
EEGstop = [eeg.takeClosest(eegtimestamps, ts[stop]) for stop in tstop] 
startidx = [eegtimestamps.index(start)*512 for start in EEGstart]
stopidx =  [eegtimestamps.index(stop)*512 for stop in EEGstop]
m_theta_indices, m_gamma_indices, m_ps, m_freqs = eeg.returnThetaIndex(eegdata, startidx, stopidx)
print('size: m{}'.format(np.size(m_ps)))
m_mean_ps = np.mean(m_ps,1)
#mean_ps[0:2] = 0
fname=sys.argv[1].replace('.Ncs', '') + "_MOVING_EEG"

np.savez(fname, m_ps, m_freqs, m_theta_indices, m_gamma_indices)

EEGstart = [eeg.takeClosest(eegtimestamps, ts[start]) for start in dstart]
EEGstop = [eeg.takeClosest(eegtimestamps, ts[stop]) for stop in dstop] 
startidx = [eegtimestamps.index(start)*512 for start in EEGstart]
stopidx =  [eegtimestamps.index(stop)*512 for stop in EEGstop]
n_theta_indices, n_gamma_indices, n_ps, n_freqs = eeg.returnThetaIndex(eegdata, startidx, stopidx)
#print(n_theta_indices)

n_mean_ps = np.mean(n_ps,1)

fname=sys.argv[1].replace('.Ncs','') + "_NOTMOVING_EEG"
np.savez(fname, n_ps, n_freqs, n_theta_indices, n_gamma_indices)

