import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob

eegfiles = glob.glob("./EEGRawData/*.npz")
npzfile=np.load("./EEGRawData/CSC1.npz")
eegdata=npzfile['arr_0']
eegtime = .257552*np.asarray([ts for ts in range(len(eegdata))])/512.

def simData():
   t_max = len(eegtime)
   #x = 0.0
   #t = 0
   i = 0
   while i < t_max:
      # x = np.sin(np.pi*t)
       x = eegdata[i]
       print x
       t = eegtime[i]
       i = i+1
       yield x, i

def simPoints(simData):
    x, t = simData[0], simData[1]
    line.set_data(t, x)
    return line

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot([], [], 'bo')
#ax.set_ylim(-1, 1)
#ax.set_xlim(0, 10)

ani = animation.FuncAnimation(fig, simPoints, simData, blit=False, interval=10, repeat=True)
plt.show()
