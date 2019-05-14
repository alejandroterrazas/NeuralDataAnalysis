import numpy as np
from matplotlib import pyplot as plt
import sys
import TetrodeUtils as tu

def group_consecutives(vals, step=1):
    """Return list of consecutive lists of numbers from vals (number list)."""
    run = []
    result = [run]
    expect = None
    for v in vals:
        if (v == expect) or (expect is None):
            run.append(v)
        else:
            run = [v]
            result.append(run)
        expect = v + step
    return result

plotit = sys.argv[2]
pvdfile = sys.argv[1]

with open(pvdfile, 'rb') as f:
    n_lines = sum(1 for line in f)
    f.close()
    print(n_lines)
    ts = np.zeros(n_lines, dtype=np.uint64)
    x = np.zeros(n_lines)
    y = np.zeros(n_lines)

with open(pvdfile, 'rb') as f:
    for i,line in enumerate(f):
      lineparts=(line.split())
      ts[i]=lineparts[0]
      x[i]=lineparts[1]
      y[i]=lineparts[2]
f.close()
    
#xdiff = np.abs(np.diff(x))
#print(xdiff)
print(np.shape(x))
print(np.shape(y))
hist, bin_edges = np.histogram(x,100,density=True)
print(hist)
print(bin_edges)
plt.plot(bin_edges[1:], hist)
plt.show()
#print(x[0:100])
#print(y[0:100])

#plt.plot(x,y, 'r.')
#plt.show()

 
#plt.hist(np.diff(ts))
#plt.show()

#xdiff = np.abs(np.diff(np.convolve(x,  np.ones(3000, dtype=np.int), 'valid')))
#ydiff = np.abs(np.diff(np.convolve(y, np.ones(3000, dtype=np.int), 'valid')))

xdiff = np.abs(np.convolve(np.diff(x), np.ones(100, dtype=np.int), 'valid'))
ydiff = np.abs(np.convolve(np.diff(y), np.ones(100, dtype=np.int), 'valid'))
totdist = xdiff+ydiff


'''
inotmoving = np.where(totdist<20)[0]
grouped = group_consecutives(inotmoving)
starts = []
stops = []

for group in grouped:
    if group[-1] - group[0]  > 1000:
      starts.append(ts[group[0]])
      stops.append(ts[group[-1]])
      print(starts)
      if plotit == 'plot':
        plt.plot(x[group[0]:group[-1]], y[group[0]:group[-1]],'b.')
        print(x[group[0]:group[-1]])

        plt.ylim([0,480])
        plt.xlim([0,640])
        plt.show()


outfile = pvdfile.replace('.ascii', '_NOTMOVING')
np.savez(outfile, starts, stops)
'''
imoving = np.where(totdist>200)[0]

hist, bin_edges = np.histogram(x[imoving],100,density=True)
print(hist)
print(bin_edges)
plt.plot(bin_edges[1:], hist)
plt.show()
'''
grouped = group_consecutives(imoving)

starts = []
stops = []

for group in grouped:
    if group[-1] - group[0]  > 1000:
      starts.append(ts[group[0]])
      stops.append(ts[group[-1]])
     # minix = x[group[0]:group[-1]]
      if plotit == 'plot':
        plt.plot(x[group[0]:group[-1]], y[group[0]:group[-1]],'b.')
        plt.ylim([0,480])
        plt.xlim([0,640])
        plt.show()


outfile = pvdfile.replace('.ascii', '_MOVING')
np.savez(outfile, starts, stops)



#outfile = './RawData/NOTMOVING.txt'
#f = open(outfile, "w")

#for start, stop in zip(starts,stops):
#  f.write(str(start))
#  f.write(',')
#  f.write(str(stop))
#  f.write('\n')

#f.close()

#print(inotmoving)
#print(totdist[inotmoving])
#notmoving = np.zeros(np.size(totdist))
#notmoving[inotmoving] = 1
#print(notmoving)

#hist, bin_edges = np.histogram(totdist,100)
#print(bin_edges)

#print(xdiff[40000:60000])


#print(x)
#print(y)
'''
