import pandas
import sys
import os
import EEGUtils as eu
import numpy as np
import pandas as pd

print(sys.argv[1])
print(sys.argv[2])

dsname = sys.argv[1]
xlname = sys.argv[2]

if os.path.exists(xlname):
   xl = pd.read_excel(xlname)
else:
   xl = pd.DataFrame(columns = ['ds_name', 'start', 'stop', 'duration'])

_, ts = eu.readEEG('./RawData/CSC1.Ncs')

start = ts[0]/60000000
stop = ts[-1]/60000000
duration = stop-start

print("start: {}, stop: {}, duration {}".format(start, stop, duration))

#append to dataframe

df = pd.DataFrame([[dsname,start, stop, duration]], columns = ['ds_name', 'start', 'stop', 'duration'])
xl = xl.append({'ds_name': dsname, 'start': start, 'stop': stop, 'duration': duration}, ignore_index=True)

#print(xl)
xl.to_excel(xlname)

