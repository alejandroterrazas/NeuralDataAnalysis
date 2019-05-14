import numpy as np

def spike_info_measures(firing_rates, occupancy):
  #overall = np.sum(firing_rates*occupancy)
  for i in range(len(firing_rates)):
    print("****** {} *****".format(i))
    info_rate = occupancy[i] * np.log2(firing_rates[i]/occupancy[i])
    print(info_rate)
    print(info_rate)/np.sum(firing_rates)

    
#   print(p * rate*np.log2(rate/overall)
# for p,rate in zip(occupancy, firing_rates)]
#  info_rate = np.sum([i for i in info if np.isneginf(i) != True and np.isnan(i) != True])
#  info_per_spike = info_rate/overall
#  return info_rate, info_per_spike

fr = [4.0, 0.1, 0.1, 0.1]
occup=[.5, 0, .25, .25]


spike_info_measures(fr, occup)

