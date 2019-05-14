import EEGUtils as eeg
import sys
from matplotlib import pyplot as plt

eegfile = sys.argv[1]
eegdata,eegtimestamps = eeg.readEEG(eegfile)
print len(eegtimestamps)
print eegtimestamps[:10]
print len(eegdata)

startidx = int(sys.argv[2])
stopidx = int(sys.argv[3])
starttime = startidx/20003
stoptime = stopidx/2003
print("START: {}; STOP: {}".format(starttime, stoptime))

plt.plot(eegdata[startidx:stopidx])

plt.show()

