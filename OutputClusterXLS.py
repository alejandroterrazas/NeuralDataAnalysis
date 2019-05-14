import pandas as pd
import json
import sys

filename = sys.argv[1]

with open(filename) as json_data:
  d = json.load(json_data)

targets = ['num_events', 'isolation', 'noise_overlap', 'peak_snr', 'cell_type']

df = pd.DataFrame(columns = targets, index  = [d['clusters'][i]['label'] for i in range(len(d['clusters']))])
  
for i in range(len(d['clusters'])):
  l = d['clusters'][i]['label']
  m = d['clusters'][i]['metrics']
  df.loc[l] = [m['num_events'],m['isolation'], m['noise_overlap'], m['peak_snr'], '']
   
outfile = filename.replace('.json', '.xlsx')

df.to_excel(outfile)


