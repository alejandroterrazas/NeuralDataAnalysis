import numpy as np
from matplotlib import pyplot as plt
import EEGUtils as eu

eegdata, ts = eu.readEEG('./RawData/CSC2.Ncs')
timestamps = np.linspace(ts[0], ts[-1], len(eegdata))
s1_end = timestamps[9876000]
s2_start = timestamps[9876000+1250000]

#end session 1 for 1-24: 9876000
#start session 2 for 1-24  9876000+1250000
#bigjump works on the type where record was turned off but no exit
#if errortype == 1:
#  bigjump = np.argsort(np.diff(ts))
#  plt.subplot(2,1,1)
#  plt.plot(eegdata[0:bigjump[-1]*512])
#  plt.subplot(2,1,2)
#  plt.plot(eegdata[bigjump[-1]*512:])

#plt.plot(eegdata[:9876000])

import TetrodeUtils as tu
spikets, waveforms = tu.readTetrode('./RawData/Sc10.ntt')

ds1 = [spike for spike in spikets if spike<s1_end]
ds2 = [spike  for spike in spikets if spike>s2_start]

waveforms1 = waveforms[:,:,:len(ds1)]
waveforms2 = waveforms[:,:,len(spikets)-len(ds2):]

print(len(ds1))
print(len(ds2))

print(np.shape(waveforms1))
print(np.shape(waveforms2))

plt.plot(waveforms2[:,:,5])
plt.show()

