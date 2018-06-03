import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

import pandas as pd
from pandas import DataFrame

import seaborn as sns
import matplotlib.pyplot as plt

#matplotlib.use('pgf')
params = {
    "pgf.texsystem": "pdflatex",
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": [],
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 16,
    "font.size": 20,
    "legend.fontsize": 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "text.latex.preamble": [
        "\\usepackage{gensymb}",
        "\\usepackage{fix-cm}",
    ]
}
sns.set_palette('colorblind')
sns.set_style("whitegrid", params)
matplotlib.rcParams.update(params)

font = {'size'   : 30}

matplotlib.rc('font', **font)

dir = sys.argv[1]
accuracy=[]
ped = []
networks = [] 

N = 0
#f = open(dir + '/results', 'r')
f = open("experiment" + str(dir) + ".results", "r")

for l in f:
    l = l.strip().split(' ')
    accu = l[1]
    accuracy.append(int(float(accu)* 100))
    p = float(l[2])
    ped.append(p)
    networks.append(l[0])
    N+=1

networks = [x for _,x in sorted(zip(accuracy,networks))]
ped = [x for _,x in sorted(zip(accuracy,ped))]
accuracy.sort()

ind = np.arange(N)  # the x locations for the groups

width = 0.30       # the width of the bars

#d = {'network':networks, 'similarity' : accuracy, 'PED': ped}
#df = pd.DataFrame(data=d)

#df.loc['network','similarity'].plot(kind='bar')
#df.loc['network','PED'].plot(kind='bar',secondary_y=True)

#df.plot(kind='bar',grid=True,subplots=True,sharex=True)

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = ax.twinx()

rects1 = ax.bar(ind, accuracy, width, color='g')
rects2 = ax1.bar(ind+width, ped, width, color='b')

ax.set_ylabel('Network Similarity', fontsize=18)
ax1.set_ylabel('Path Edit Distance', fontsize=18)

ax.set_ylim([0,100])
ax1.set_ylim([0,2])
plt.gcf().subplots_adjust(bottom=0.35)
plt.gcf().subplots_adjust(right=0.80)

ax.set_xticks(ind+width)
ax.set_xticklabels(networks, rotation=90, fontsize=18)
ax.legend( (rects1[0], rects2[1]), ('N.S', 'P.E.D' ), prop={'size':16},  borderaxespad=0. ,fontsize=30)
plt.grid()

plt.savefig('experiment' + str(dir) + '.pdf')
