from __future__ import division

import struct
import matplotlib.pyplot as plt
import numpy as np
import os
import array
import sys
import VideoUtils as vu

"""
Program to create a mask for the maze.  This is part of cleaning video
"""
#use the following at the python command prompt AFTER running this program
'''
npzfile = np.load('./RawData/PREMASK.npz')
img = npzfile['arr_0']
from scipy import ndimage
import numpy as np
mask = np.zeros([640,480])
mask[np.where(img>10)] = 1
im = ndimage.binary_erosion(mask, structure=np.ones((30,30)))
im2 = ndimage.binary_dilation(im, structure=np.ones((10,50)))
'''

      
def makeMask(data): 
 
  img = np.zeros([640,480])

  for ii,targets in enumerate(data):
    for t in targets:
      line = format(t,'032b')
      pure = line[0:4]
      y = int(line[4:16], 2)
      raw = line[16:20]
      x = int(line[20:], 2)
  
      if (ylim[0] < y < ylim[1]) and (xlim[0] < x < xlim[1]):
        img[x,y] += 1
  
  return img

xlim = [0,640]
ylim = [0,480]

npzfile = np.load('./RawData/EPOCHS.npz')
start = npzfile['arr_0'].astype(int)
stop = npzfile['arr_1'].astype(int)

timestamps, xpt, ypt, dwP, dnT = vu.getVideoData('./RawData/VT1.Nvt')

print(start)
print(stop)

P = list(dwP[start:stop])


mask = makeMask(P)
np.savez("./RawData/PREMASK", mask)
   
