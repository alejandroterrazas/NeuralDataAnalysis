"""
TimeStamp : UInt64
ChannelNumber: UInt32
SampleFreq: UInt32
NumValidSample: UInt32
Samples: Int16[]
"""
from __future__ import division

import numpy as np
import sys
from mlpy import writemda16i, writemda32
import gc

from matplotlib import pyplot as plt

recsize = 304   
#args = str(sys.argv)
filename = sys.argv[1]

print("************Processing {} ...".format(filename))

with open(filename, 'rb') as f:  
    spikedata = f.read()[16384:]
    f.close()
    
nevents = int(len(spikedata)/recsize)
print("nevents: {}".format(nevents))
#ts = np.ndarray((nevents,), '<Q', spikedata, 0, (304,))

spikes = np.ndarray((nevents,128), '<h', spikedata, 48, (304,2)).reshape(nevents,32,4)

npad = ((0,0),(48,48),(0,0))
spikes = np.pad(spikes, pad_width=npad, mode='constant', constant_values=0)

spikes = spikes.transpose().reshape(4,nevents*128, order='F')

#uncomment the following line when MS allow event times
#writemda32(firings,'event_times.mda');

filename +=".raw.mda"
writemda16i(spikes,filename);
print("...Done writing raw.mda for {}".format(filename))

gc.collect()
