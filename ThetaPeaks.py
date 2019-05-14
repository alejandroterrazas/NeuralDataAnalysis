
import numpy as np
import peakutils
import sys
from bisect import bisect_left, bisect_right
import EEGUtils as eeg


def returnPeakIndices(eegvals, m, t):
     ind_peaks = peakutils.indexes(eegvals, thres=t, min_dist=m)
     ind_troughs = peakutils.indexes(eegvals*-1, thres=t, min_dist=m)
     return ind_peaks, ind_troughs
     
fs = 512/.257552

eegfile=sys.argv[1]

eegdata, eegtimestamps = eeg.readEEG(eegfile)
print(eegtimestamps[0])
theta = eeg.butter_bandpass_filter(eegdata, 6, 10, fs, order=4)
gamma = eeg.butter_bandpass_filter(eegdata, 30, 100, fs, order=4)
#np.savez("./filteredeeg",theta=theta,gamma=gamma,eegtimestamps=eegtimestamps)

theta_peaks, theta_troughs = returnPeakIndices(theta,20, .25)
gamma_peaks, gamma_troughs = returnPeakIndices(gamma,5, .25)

np.savez(eegfile+".thetapeaks",theta_peaks=theta_peaks,theta_troughs=theta_troughs)


