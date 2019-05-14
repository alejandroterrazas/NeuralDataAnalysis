import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

def returnCell_dfs(fname):

  xl = pd.read_excel(fname)
  pyram = xl.loc[xl['cell_type'] == 'P']
  inter = xl.loc[xl['cell_type'] == 'I']
  print("*"*15)
  print("Pyramidal cells for {}: n={}".format(fname,len(pyram['s1_fr']))) 
  print("s1_fr mean: {} , s1_fr std: {}".format(
         np.mean(pyram['s1_fr']),
         np.std(pyram['s1_fr'])))
  print("m_fr mean: {} , m_fr std: {}".format(
         np.mean(pyram['m_fr']),
         np.std(pyram['m_fr'])))
  print("s2_fr mean: {} , s2_fr std: {}".format(
         np.mean(pyram['s2_fr']),
         np.std(pyram['s2_fr'])))
  print("#"*15)
  print("Interneurons for {}: n={}".format(fname,len(inter['s1_fr'])))
  print("s1_fr mean: {} , s1_fr std: {}".format(
         np.mean(inter['s1_fr']),
         np.std(inter['s1_fr'])))
  print("m_fr mean: {} , m_fr std: {}".format(
         np.mean(inter['m_fr']),
         np.std(inter['m_fr'])))
  print("s2_fr mean: {} , s2_fr std: {}".format(
         np.mean(inter['s2_fr']),
         np.std(inter['s2_fr'])))
  print("*"*15)
  return pyram, inter


wt_datasets = ['10603firingrates.xlsx', '10547firingrates.xlsx']

ko_datasets = ['10601firingrates.xlsx', '10551firingrates.xlsx']

wt_p = pd.DataFrame(columns = 
                  ['cell_name', 's1_fr', 'm_fr', 's2_fr', 'cell_type'])

wt_i = pd.DataFrame(columns =
                  ['cell_name', 's1_fr', 'm_fr', 's2_fr', 'cell_type'])

ko_p = pd.DataFrame(columns =
                  ['cell_name', 's1_fr', 'm_fr', 's2_fr', 'cell_type'])

ko_i = pd.DataFrame(columns =
                  ['cell_name', 's1_fr', 'm_fr', 's2_fr', 'cell_type'])

for ds in wt_datasets:
  p, i = returnCell_dfs(ds)
  wt_p = wt_p.append(p)
  wt_i = wt_i.append(i)

for ds in ko_datasets:
  p, i = returnCell_dfs(ds)
  ko_p = ko_p.append(p)
  ko_i = ko_i.append(i)

print(ko_p)

print('PYRAMIDAL CELLS******')
print(stats.ttest_ind(ko_p['s1_fr'], wt_p['s1_fr']))
print(stats.ttest_ind(ko_p['m_fr'], wt_p['m_fr']))
print(stats.ttest_ind(ko_p['s2_fr'], wt_p['s2_fr']))
print('*'*20)
print('INTERNEURONS********')
print(stats.ttest_ind(ko_i['s1_fr'], wt_i['s1_fr']))
print(stats.ttest_ind(ko_i['m_fr'], wt_i['m_fr']))
print(stats.ttest_ind(ko_i['s2_fr'], wt_i['s2_fr']))
print('*'*20)

