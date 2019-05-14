import VideoUtils as vu
import TetrodeUtils as tu
import sys
import struct
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from bisect import bisect_left
import operator
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

spikets = readTFile(sys.argv[1])

npzfile=np.load("./RawData/POSITION.npz")
xfilt = npzfile['arr_0']
yfilt = npzfile['arr_1']
ts = npzfile['arr_2']

npzfile=np.load('./RawData/TRAJECTORIES.npz')
tstart = npzfile['arr_0']
tstop = npzfile['arr_1']
tspeed = npzfile['arr_2']
print(len(spikets))

#reliminate spikes that are during rest1 and rest2
spikes = spikets[np.where((spikets>=ts[0]) & (spikets<=ts[-1]))]
spikes = spikets
#print spikes
mindex=[]

for start, stop in zip(tstart,tstop):
  #  print ts[start]
    #print spikes[np.where((spikes>=ts[start]) & (spikes<=ts[stop]))]
    mindex.append(spikes[np.where((spikes>=ts[start]) & (spikes<=ts[stop]))])

#print spikes

#print mindex 
outspikes = np.concatenate(mindex).ravel()
outspikes = spikes

print np.shape(outspikes)

posx = np.zeros(len(outspikes))
posy = np.zeros(len(outspikes))


for i in range(len(posx)):
    #find the closest position ts to the spike
    closest_t = takeClosest(ts, outspikes[i])
#    print closest_t
    posx[i] = xfilt[np.where(closest_t == ts)]
    posy[i] = yfilt[np.where(closest_t == ts)]
#    print("posx {}: posy {}".format(posx[i], posy[i]))


  
fig, ax = plt.subplots()

bgpoints = int(len(xfilt)/(len(xfilt)/10))
l1, = plt.plot(xfilt[1:len(xfilt):bgpoints],yfilt[1:len(yfilt):bgpoints],'.', markersize=3, color='#FFE4C4')
l5, = plt.plot(posx, posy, 'b.', markersize=3)
#dsname=sys.argv[2]
#cellname=sys.argv[1].replace('./RawData', '')
#dsname += cellname

#plt.title(dsname)
plt.xlim([40000,np.amax(xfilt)+1000])
plt.xlim([np.amin(xfilt)-1000,np.amax(xfilt)+1000])
plt.ylim([np.amin(xfilt)-1000,np.amax(xfilt)+1000])


class Index(object):
    ind = 0

    def next(self, event):
        self.ind += 1
        ii=self.ind
        
        if ii < len(tstop):
			l3.set_xdata(xfilt[tstop[ii]])
			l3.set_ydata(yfilt[tstop[ii]])
			l2.set_xdata(xfilt[tstart[ii]])
			l2.set_ydata(yfilt[tstart[ii]])
			l4.set_xdata(xfilt[tstart[ii]:tstop[ii]])
			l4.set_ydata(yfilt[tstart[ii]:tstop[ii]])
			plt.draw()
		#else:
		 #   self.ind -= 1
	    
	   # plt.draw()

    def prev(self, event):
        self.ind -= 1
        ii=self.ind
        if ii > 0:
			l3.set_xdata(xfilt[tstop[ii]])
			l3.set_ydata(yfilt[tstop[ii]])
			l2.set_xdata(xfilt[tstart[ii]])
			l2.set_ydata(yfilt[tstart[ii]])
			l4.set_xdata(xfilt[tstart[ii]:tstop[ii]])
			l4.set_ydata(yfilt[tstart[ii]:tstop[ii]])
			plt.draw()
		#else:
		#    self.ind += 1
		#plt.draw()
        
  
callback = Index()      
outfile = sys.argv[1]
outfile = outfile+".png"
fig.savefig(outfile)
plt.show()

