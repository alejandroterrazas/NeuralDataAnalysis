
import sys
import struct

import operator
import numpy as np
#9_3 3447
#4389
#tenths of ms as unsigned integer
def readTFile(filename, hsize):
  with open(filename, 'rb') as f:

    tsdata  = f.read()[int(hsize):]
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

spikets = readTFile(sys.argv[1],sys.argv[2])


