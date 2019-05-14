import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob

pause = False
eegfiles = glob.glob("./*.npz")
npzfile=np.load("./CSC1.npz")
eegdata=npzfile['arr_0']
eegtime = .257552*np.asarray([ts for ts in range(len(eegdata))])/512.
nplotpoints=400
nplots = 10
fig, axs = plt.subplots(nplots,1, sharey=False, sharex=True)

bigeeg = np.zeros([len(eegdata),nplots])

for ii in range(nplots):
    npzfile=np.load(eegfiles[ii])
    bigeeg[:,ii]=npzfile['arr_0']

x = eegtime[0:nplotpoints]
lines = []
ii = 0
for ax in axs:
    y = bigeeg[0:nplotpoints,ii]
    #ax.set_autoscaley_on(True)
    #ax.set_ylim([np.min(bigeeg[:,ii]),np.max(bigeeg[:,ii])])
    l, = ax.plot(x, y)
    lines.append(l)
    ii = ii +1

npoints=len(eegdata)

def onClick(event):
   global pause 
   pause ^= True

def animate(i):
    if not pause:
      for  ii  in range(nplots):
           ts = bigeeg[i:nplotpoints+i,ii]
           lines[ii].set_ydata(ts)
           axs[ii].set_ylim([np.min(ts)-30, np.max(ts)+30])
      return lines

def init():
    for ii in range(nplots):
       lines[ii].set_ydata(x)
    return lines

fig.canvas.mpl_connect('button_press_event',  onClick)
ani = animation.FuncAnimation(fig, animate, np.arange(1,npoints), init_func=init, interval=0, blit=True)

plt.show()
