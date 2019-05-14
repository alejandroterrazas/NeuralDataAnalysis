import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys
import EEGUtils as eeg
import os


outfile = 'ThetaIndex.xlsx'
files = os.listdir('./RawData')

eegfiles = [file for file in files if file[-3:] == 'Ncs']

if len(eegfiles) ==0:
  sys.exit()

all_ps =  np.zeros([200, len(eegfiles)])
theta = np.zeros(len(eegfiles))
gamma = np.zeros(len(eegfiles))

for indx, file in enumerate(eegfiles):
  eegdata,ts = eeg.readEEG('./RawData/'+file)
  midpt = len(eegdata)//2
  ps  = eeg.returnPowerSpectrum(eegdata[midpt-midpt//2: midpt+midpt//2])
  all_ps[:, indx] = ps[:200]/np.max(ps)

  theta[indx] = np.sum(ps[6:10])/np.sum(ps[1:3])
  gamma[indx] = np.sum(ps[25:100])/np.sum(ps[1:3])
     

sort_index = list(np.argsort(theta))[::-1]

index = [eegfiles[index] for index in sort_index]
fig, ax = plt.subplots()
ax.plot(all_ps[:,sort_index[:5]])
#ax.set_ylim(-.1, np.max(all_ps[6:10,:]))
ax.set_ylim(-.001, .1)
ax.set_xlim(-.001, 80)
fig.savefig("./RawData/PowerSepctrum.png")

#plt.show()


df = pd.DataFrame(theta[sort_index], columns = ['Theta'], index = index)
df.to_excel('./RawData/ThetaIndices.xlsx')

sort_index = list(np.argsort(gamma))[::-1]
index = [eegfiles[index] for index in sort_index]

df = pd.DataFrame(gamma[sort_index], columns = ['Gamma'], index = index)
df.to_excel('./RawData/GammaIndices.xlsx')

