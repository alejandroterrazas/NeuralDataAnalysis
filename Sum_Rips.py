import numpy as np
from matplotlib import pyplot as plt

def returnRips(npzfile):
  filtered = npzfile['arr_0']
  rips = npzfile['arr_1']
  upper = npzfile['arr_2']
  lower = npzfile['arr_3']
  return rips, filtered, upper, lower

npzfile = np.load("./RawData/CSC9_RIPS.npz")
f1,r1,_,_ = returnRips(npzfile)

npzfile = np.load("./RawData/CSC10_RIPS.npz")
f2,r2,_,_ = returnRips(npzfile)

for rip1,rip2 in zip(r1,r2):
   rips = r1+r2
   plt.plot(rips)
   plt.show()

for rip,filt, u,l in zip(rips,filtered, upper, lower):
  plt.plot(filt)
  plt.plot(rip*u)
  plt.show()
