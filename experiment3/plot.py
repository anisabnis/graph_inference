import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

font = {'size'   : 22}

matplotlib.rc('font', **font)

dir = sys.argv[1]
accuracy=[]
ped = []
networks = [] 

N = 0
f = open(dir + '/results', 'r')
for l in f:
    l = l.strip().split(':')
    accu = l[1].replace("%", "")
    accuracy.append(int(float(accu)))
    p = float(l[2])
    ped.append(p)
    networks.append(l[0])
    N+=1

networks = [x for _,x in sorted(zip(accuracy,networks))]
ped = [x for _,x in sorted(zip(accuracy,ped))]
accuracy.sort()

ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
#ax1 = ax.twinx()

rects1 = ax.bar(ind, ped, width, color='b')
#rects2 = ax1.bar(ind+width, accuracy, width, color='g')

ax.set_ylabel('Path Edit Distance')
#ax1.set_ylabel('Path Edit Distance')

ax.set_ylim([0,3])
#ax1.set_ylim([0,120])
plt.gcf().subplots_adjust(bottom=0.35)
#plt.gcf().subplots_adjust(right=0.85)

ax.set_xticks(ind+width)
ax.set_xticklabels(networks, rotation=90)
#ax.legend( (rects1[0]), ('Accuracy'), prop={'size':18} )
plt.grid()

plt.savefig(dir + '/results_ped.pdf')

