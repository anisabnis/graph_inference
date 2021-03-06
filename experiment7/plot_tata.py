import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

i = 1
f = open('columbus.txt', 'r')
no_trees = dict()

for l in f:
    l = l.strip().split(':')
    no_trees[i] = len(l)
    i += 1
f.close()

print(no_trees)

font = {'size'   : 22}

matplotlib.rc('font', **font)

dir = "."
accuracy=[0] * 6
ped = [0] * 6

N = 6
f = open(dir + '/results_tata', 'r')

for l in f:
    l = l.strip().split(':')
    siz = no_trees[int(l[0])] - 1
    accu = l[1].replace("%", "")
    accu = int(float(accu))
    #accuracy.append(int(float(accu)))
    accuracy[siz] = max(accuracy[siz], accu) 
    p = float(l[2])
    ped[siz] = min(p, ped[siz])

for i in range(1, 6):
    if accuracy[i] < accuracy[i-1]:
        accuracy[i] = accuracy[i-1]

#networks = [x for _,x in sorted(zip(accuracy,networks))]
#ped = [x for _,x in sorted(zip(accuracy,ped))]
#accuracy.sort()

ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
#ax1 = ax.twinx()

rects1 = ax.bar(ind, accuracy, width, color='b')
#rects2 = ax1.bar(ind+width, accuracy, width, color='g')

ax.set_ylabel('Accuracy')
ax.set_xlabel('Number of Best Trees')
#ax1.set_ylabel('Path Edit Distance')

ax.set_ylim([0,100])
#ax1.set_ylim([0,120])
plt.gcf().subplots_adjust(bottom=0.1)
#plt.gcf().subplots_adjust(right=0.85)

ax.set_xticks(ind+width)
ax.set_xticklabels([1,2,3,4,5,6])
#ax.legend( (rects1[0]), ('Accuracy'), prop={'size':18} )
plt.grid()

plt.savefig(dir + '/results_tata_accuracy.pdf')

