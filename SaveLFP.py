import numpy as np
import EEGUtils as eeg
from matplotlib import pyplot as plt
import sys
eegfile = sys.argv[1]
print eegfile
outfile=eegfile[:-4]
print outfile
eegdata,eegtimestamps = eeg.readEEG(eegfile)
np.savez(outfile, eegdata)

#eegtime = .257552*np.asarray([ts for ts in range(len(eegdata))])/512.
#print (len(eegtime))
#print (eegtime[:100])

#plt.plot(eegtime,eegdata)
#plt.show()

