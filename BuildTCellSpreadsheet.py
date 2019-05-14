import pandas
import sys
import os
import EEGUtils as eu
import numpy as np
import pandas as pd


#print(sys.argv[1])
#print(sys.argv[2])

if os.path.exists(sys.argv[3]):
   xl = pd.read_excel(sys.argv[3])
else:
   xl = pd.DataFrame(columns = ['cell_name', 'firing_rate'])

_, ts = eu.readEEG('./RawData/CSC1.Ncs')

EEGstart = ts[0]/1000000
EEGstop = ts[-1]/1000000
totaltime = EEGstop-EEGstart

#print("EEGstart: {}, EEGstop: {}".format(EEGstart, EEGstop))

with open(sys.argv[2], 'rb') as f:  
    tsdata  = f.read()
    f.close()

recsize = 8
nevents = len(tsdata)//recsize
#print("nevents: {}".format(nevents))
firing_rate = nevents/totaltime
cellname = sys.argv[2].replace('./RawData', sys.argv[1])

print("Cell name: {} FR: {}".format(cellname, firing_rate))

#append to dataframe

#df = pd.DataFrame([[sys.argv[1],firing_rate]], columns = ['cell_name', 'firing_rate'])
xl = xl.append({'cell_name': cellname, 'firing_rate': firing_rate}, ignore_index=True)
#print(xl)
xl.to_excel(sys.argv[3])

