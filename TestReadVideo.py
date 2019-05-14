import numpy as np
import struct

def OldReadVideodata(data):

  nrecords = len(data)//1828
  print("Number of Records: {}".format(nrecords))
  #nrecs=3000
  xloc=np.zeros(nrecords, dtype=np.uint8)
  yloc=np.zeros(nrecords, dtype=np.uint8)
  hdir=np.zeros(nrecords, dtype=np.uint8)
  ts= np.zeros(nrecords, dtype=np.uint64)
 # dwPoints = np.zeros([nrecords,400])
  dwPoints = []
  dnTargets = []
  recsize=1828

  for record in range(1):
    # print(record)
     recoffset = recsize*record
     swstx = int(struct.unpack('H',data[recoffset:recoffset+2])[0])
#     print("swstx: {}".format(swstx))
     swid = int(struct.unpack('H',data[recoffset+2:recoffset+4])[0])
#     print("swid: {}".format(swid))
     swdata_size = int(struct.unpack('H',data[recoffset+4:recoffset+6])[0])
#     print("swdata_size: {}".format(swdata_size)) 
     ts[record] = int(struct.unpack('Q',data[recoffset+6:recoffset+14])[0])
     dwP = struct.unpack('400I',data[recoffset+14:recoffset+1614])
     print(dwP)
    
     dwPoints.append(tuple(p for p in dwP if int(p) != 0))
     sncrc = int(struct.unpack('H', data[recoffset+1614:recoffset+1616])[0])
     xloc[record] = int(struct.unpack('i', data[recoffset+1616:recoffset+1620])[0])
     yloc[record] = int(struct.unpack('i', data[recoffset+1620:recoffset+1624])[0])
     hdir[record] = int(struct.unpack('i', data[recoffset+1624:recoffset+1628])[0])

     dnT = struct.unpack('50i',data[recoffset+1628:recoffset+1828])
     dnTargets.append(tuple(t for t in dnT if int(t) != 0))

#  return ts, xloc, yloc, dwPoints, dnTargets
  print(dnTargets)

def getVideodata(data):

  nrecords = len(data)//1828
  print("Number of Records: {}".format(nrecords))
  recsize=1828
  #dwPoints = []

  ts = np.ndarray((nrecords,), '<Q', data, 6, (recsize,))
  #print(ts[:10])
  #print(np.shape(ts))
  dwP = np.ndarray((nrecords,400), '<I', data, 14, (recsize,4))
  #print(np.shape(dwP))
  
  xloc = np.ndarray((nrecords,), '<i', data, 1616, (recsize,))
  yloc = np.ndarray((nrecords,), '<i', data, 1620, (recsize,))
  hdir = np.ndarray((nrecords,), '<i', data, 1624, (recsize,))
  
  dnT = np.ndarray((nrecords,50), '<I', data, 1628, (recsize,4))
  for i in range(200):
    print(dnT[1,:])
  print(dwP)
  print(dnT)

  #return ts, xloc, yloc, dwP, dnT

vidfile = './videofiles/VT1.Nvt'

with open(vidfile, 'rb') as f:
    videodata = f.read()[16384:]
f.close()

#OldReadVideodata(videodata)
getVideodata(videodata)

