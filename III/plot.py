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
    "font.size": 16,
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

font = {'size'   : 22}

matplotlib.rc('font', **font)

accuracy = dict()
ped = dict()
f = open("results.txt" ,"r")
for l in f:
    l = l.strip().split(" ")
    n = l[0]
    if n not in accuracy:
        accuracy[n] = list()
        ped[n] = list()
        
    accuracy[n].append(float(l[1]) * 100)
    ped[n].append(l[2])
    
accuracy_by_error = dict()
for i in range(6):
    accuracy_by_error[i] = list()
    for n in ['bandcon', 'att', 'sanet']:
        accuracy_by_error[i].append(accuracy[n][i])
        
print(accuracy_by_error)

first = accuracy_by_error[0]
second = accuracy_by_error[1]
third = accuracy_by_error[2]
fourth = accuracy_by_error[3]
fifth = accuracy_by_error[4]
sixth = accuracy_by_error[5]

N = 3
networks = ['bandcon', 'att', 'sanet']

ind = np.arange(N)
width = 0.15

fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_ylabel('Network Similarity')

p1 = ax.bar(ind, first, width, color='g')
p2 = ax.bar(ind +width, second, width,color='b')
p3 = ax.bar(ind + 2*width, third, width,color='r')
p4 = ax.bar(ind +3*width, fourth, width,color='m')
p5 = ax.bar(ind +4*width, fifth, width,color='c')
p6 = ax.bar(ind +5*width, sixth, width,color='y')


ax.set_xticklabels(networks)

ax.set_ylim([0,100])
plt.gcf().subplots_adjust(bottom=0.35)
plt.gcf().subplots_adjust(right=0.80)

ax.set_xticks(ind + 2*width)
ax.grid()
#plt.grid()
ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]),  ('0 \% error', '10 \% error', '20 \% error', '30 \% error', '40 \% error', '50 \% error') , prop={'size':11}, bbox_to_anchor=(1., 1.), loc=2, borderaxespad=0. ,fontsize=30)
plt.savefig('experiment' + str('II') + '.pdf')
