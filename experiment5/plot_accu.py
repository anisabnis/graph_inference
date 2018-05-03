import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

network = sys.argv[1]
no_enc = int(sys.argv[2])

i = 1
f = open(network + '.txt', 'r')
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
accuracy=[0] * no_enc
ped = [0] * no_enc

accuracy_avg = list()
for i in range(no_enc):
    accuracy_avg.append([])

print(accuracy_avg)

accuracy_min = [110] * no_enc

N = no_enc
f = open(dir + '/results_' + network, 'r')

for l in f:
    l = l.strip().split(':')
    siz = no_trees[int(l[0])] - 1
    accu = l[1].replace("%", "")
    accu = int(float(accu))
    #accuracy.append(int(float(accu)))
    accuracy[siz] = max(accuracy[siz], accu) 
    accuracy_min[siz] = min(accuracy_min[siz], accu)
    accuracy_avg[siz].append(accu)

    p = float(l[2])
    ped[siz] = min(p, ped[siz])

accu_avg = []

for i in range(no_enc):
    s = sum([x for x in accuracy_avg[i]])
    if len(accuracy_avg[i]) == 0:
        accu_avg.append(accu_avg[i-1])
    else :
        accu_avg.append(s/len(accuracy_avg[i]))


# for i in range(1, no_enc):
#     if accuracy[i] < accuracy[i-1]:
#         accuracy[i] = accuracy[i-1]

#    if accu_avg[i] < accu_avg[i-1]:
#        accu_avg[i] = accu_avg[i-1]

#accu_avg = []
#for i in range(6):
#    accu_avg[i] = sum(accuracy_avg)/len(accuracy_avg)

#networks = [x for _,x in sorted(zip(accuracy,networks))]
#ped = [x for _,x in sorted(zip(accuracy,ped))]
#accuracy.sort()



ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
#ax1 = ax.twinx()

rects1 = ax.bar(ind - width, accuracy, width, color='b')
rects2 = ax.bar(ind , accu_avg, width, color='g')
rects3 = ax.bar(ind + width, accuracy_min, width, color='r')

ax.set_ylabel('Accuracy')
ax.set_xlabel('Number of Trees')
#ax1.set_ylabel('Path Edit Distance')

ax.set_ylim([0,100])
#ax1.set_ylim([0,120])
plt.gcf().subplots_adjust(bottom=0.1)
#plt.gcf().subplots_adjust(right=0.85)

ax.set_xticks(ind)
xvals = list(range(1,no_enc + 1))
ax.set_xticklabels(xvals)
#ax.legend( (rects1[0]), ('Accuracy'), prop={'size':18} )
plt.grid()

plt.savefig(dir + '/results_' +  network + '_accuracy.pdf')

