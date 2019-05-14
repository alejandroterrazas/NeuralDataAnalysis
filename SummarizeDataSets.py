import sys
import pandas as pd

#xl = pd.DataFrame(columns = ['ds_name'])
dsname = []
with open(sys.argv[1], 'rb') as f:
  for i,line in enumerate(f):
    dsname.append(line.lstrip().replace("\n", "").replace("PRE ", ""))

#f.close()
print(dsname)

xl = pd.DataFrame(dsname)  

xl.to_excel(sys.argv[2])



