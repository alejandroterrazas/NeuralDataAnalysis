from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button

import os
import sys
#img = mpimg.imread(fname)
#plt.subplot(2,1,1)
#plt.imshow(img)
#plt.show()

#fig, ax = plt.subplots()
pfmaps = os.listdir('./PFData/PFMAPS/')
tsheets  = os.listdir('./PFData/TFILES/')
print pfmaps
print tsheets

pfimg = mpimg.imread('./PFData/PFMAPS/'+pfmaps[0])
timg = mpimg.imread('./PFData/TFILES/'+tsheets[0])
fig, ax = plt.subplots()

plt.subplot(1,2,1)
curr_pf = plt.imshow(pfimg)
plt.subplot(1,2,2)
curr_t = plt.imshow(timg)

class Index(object):
    ind = 0

    def next(self, event):
        self.ind += 1
        ii=self.ind
 
        if ii < len(pfmaps):
           pfimg = mpimg.imread('./PFData/PFMAPS/'+pfmaps[ii])
           timg = mpimg.imread('./PFData/TFILES/'+tsheets[ii]) 
           curr_pf.set_data(pfimg)
           curr_t.set_data(timg)
           plt.draw()
    def prev(self, event):
        self.ind -= 1
        ii=self.ind

        if ii > 0:
           pfimg = mpimg.imread('./PFData/PFMAPS/'+pfmaps[ii])
           timg = mpimg.imread('./PFData/TFILES/'+tsheets[ii])
           curr_pf.set_data(pfimg)
           curr_t.set_data(timg)
           plt.draw()

callback = Index()

axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()

