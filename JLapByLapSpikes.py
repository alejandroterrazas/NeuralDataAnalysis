
import sys
import struct
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from bisect import bisect_left
import operator
import numpy as np
#9_3 3447
#4389
#tenths of ms as unsigned integer
def readTFile(filename):
  with open(filename, 'rb') as f:  
  
    tsdata  = f.read()[259:]
    print len(tsdata)
    f.close()
    recsize = 4
    nevents = int(len(tsdata)/recsize)
    print("nevents: {}".format(nevents))

    ts = np.zeros(nevents)
 
    for i in range(nevents):
      recoffset=recsize*i
      dnParams = np.zeros(8)
      #print recoffset
      ts[i] = struct.unpack('>I', tsdata[recoffset:recoffset+recsize])[0]
      print ts[i]
  return ts

#def convertts_to_minutes(ts):
#    return (ts)/(1*3600) #was 3600


def  takeClosest(myList, myNumber):
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

#def convertvts_to_minutes(vts):
#     return (vts)*(.01)  #/60

spikets = readTFile(sys.argv[1])
#print(convertts_to_minutes(spikets[0]))
#print(convertts_to_minutes(spikets[-1]))
##spikes to to minues ts/(10000*3600
## to sec is ts/10000*60


print("spikets[0] {}".format(spikets[0]))
print("spikets[-1] {}".format(spikets[-1]))

npzfile=np.load("./RawData/POSITION.npz")
xfilt = npzfile['arr_0']
yfilt = npzfile['arr_1']
ts = npzfile['arr_2']
x = npzfile['arr_3']
y = npzfile['arr_4']
mov = npzfile['arr_5']


ts /= 100
print ("vts[0] {}".format(ts[0]))
print ("vts[-1] {}".format(ts[-1]))

#above was .000001 * 60
##videodata in microsecond


npzfile=np.load('./RawData/TRAJECTORIES.npz')
tstart = npzfile['arr_0']
tstop = npzfile['arr_1']
tspeed = npzfile['arr_2']

#ts *= .0001
print(len(spikets))
print("len spikes before: {}".format(len(spikets)))
#reliminate spikes that are during rest1 and rest2
print ts[0]
print ts[-1]

#spikes = spikets[np.where(spikets>=ts[0])]
#spikes = spikets[np.where(spikets<=ts[-1])]

spikes = spikets[np.where((spikets>=ts[0]) & (spikets<=ts[-1]))]
print("len spikes after: {}".format(len(spikes)))
print("spikes[0] after {}".format(spikes[0]))
print("spikes[-1] after {}".format(spikes[-1]))
#spikes = spikets
#print spikes
#mindex=[]
#for i  in len(spikes):
    #find nearest ts
       
#for start, stop in zip(tstart,tstop):
  #  print ts[start]
    #print spikes[np.where((spikes>=ts[start]) & (spikes<=ts[stop]))]
#    mindex.append(spikes[np.where((spikes>=ts[start]) & (spikes<=ts[stop]))])

#print spikes

#print mindex 
#outspikes = np.concatenate(mindex).ravel()
outspikes = spikes
#print len(spikets)
#print len(np.where(mov = 1.0))
#outspikes = spikets[np.where(mov =1.0)]  #spiekts was spikes
print np.shape(outspikes)

#posx = np.zeros(len(outspikes))
#posy = np.zeros(len(outspikes))

posx=np.zeros(len(outspikes))
posy=np.zeros(len(outspikes))


posx=[]
posy=[]


for i in range(len(outspikes)):
    #find the index of closest position ts to the spike
    closest_t = takeClosest(ts, outspikes[i])
    print("{}; {}".format(closest_t, outspikes[i]))
    print(np.where(ts == closest_t))
    if (mov[np.where(closest_t == ts)] == 1.0):           
       posx.append(x[np.where(closest_t == ts)])
       posy.append(y[np.where(closest_t == ts)]) 

    #posx[i] = x[np.where(closest_t == ts)]
    #posy[i] = y[np.where(closest_t == ts)]
#goodx = np.nonzero(posx)
#goody = np.nonzero(posy)
#print goodx[:20]
#print goody[:20]
#posx = posx[goodx]
#posy = posy[goody]

print(np.shape(posx))
print(np.shape(posy))
#print(np.shape(newposx))
#print(np.shape(newposy))

#cleanposx = posx[np.where((posx>30000) & (posx<100000))]

# & posx<10000)]
   
#    print("posx {}: posy {}".format(posx[i], posy[i]))

#plt.hist(posx, 40)
#plt.show()


fig, ax = plt.subplots()

bgpoints = int(len(xfilt)/(len(xfilt)/10))
#l1, = plt.plot(xfilt[1:len(xfilt):bgpoints],yfilt[1:len(yfilt):bgpoints],'.', markersize=3, color='#FFE4C4')
l1, = plt.plot(x[1:len(x):bgpoints],y[1:len(y):bgpoints],'.', markersize=5, color='r')  #FFE4C4

l5, = plt.plot(posx, posy, 'b.', markersize=8)
#plt.xlim([0,140000])
#plt.ylim([60000,80000])
plt.xlim([np.amin(xfilt)-1000,np.amax(xfilt)+1000])
plt.ylim([np.amin(yfilt)-1000,np.amax(yfilt)+1000])

plt.show()


#dsname=sys.argv[2]
#cellname=sys.argv[1].replace('./RawData', '')
#dsname += cellname

#plt.title(dsname)
#plt.xlim([0,140000])
#plt.ylim([60000,80000])

#plt.xlim([np.amin(xfilt)-1000,np.amax(xfilt)+1000])
#plt.ylim([np.amin(yfilt)-1000,np.amax(ycfilt)+1000])

'''

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
'''
outfile = sys.argv[1]
outfile = outfile+".png"
fig.set_size_inches((14,14), forward=False)

fig.savefig(outfile)
plt.show()

