import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import matplotlib

networks = ['6et1', 'tata', 'sinet', 'columbus', 'geant5', 'bandcon', 'bics', 'integra', 'rnp', 'sanet', 'dfn' ,'surfnet', 'evolink']

#networks = ['6et1']
network_accu = defaultdict(lambda : defaultdict(float))
for n in networks:
    l_map = dict()

    f1 = open('mapping.' + n, 'r')
    for l in f1:
        l = l.strip().split(' ')
        l_map[int(l[0])] = int(l[1])
    f1.close()
#    print(l_map)

    f2 = open('result.' + n, 'r')
    i = 1
    j = 0
    for l in f2:
        l = l.strip()
        if i%2 == 1:
            accu = l.split(':')[1]
            accu = accu.replace("%", "")
            accu = float(accu)
            j = j + 1

            if l_map[j] not in network_accu[n]:
                network_accu[n][l_map[j]] = 0

 #           print(accu)
            network_accu[n][l_map[j]] = max(network_accu[n][l_map[j]], accu)
            i += 1
        else:
            i += 1
    f2.close()

for n in network_accu:
    for i in [0, 1, 2]:
        if i not in network_accu[n]:
            network_accu[n][i] = network_accu[n][i-1]
        elif network_accu[n][i] == 0:
            network_accu[n][i] = network_accu[n][i-1]

for n in network_accu:
    for p in network_accu[n]:
        print(n, network_accu[n][p])
    

for i in [0,1,2]:
    network_ = []
    accu = []
    for n in network_accu:
        network_.append(n)
        accu.append(network_accu[n][i])

    #network_ = [x for _,x in sorted(zip(accu,network_))]
    #accu.sort()

    N = len(network_)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.30       # the width of the bars
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    rects1 = ax.bar(ind, accu, width, color='b')

    ax.set_ylabel('Accuracy')

    ax.set_ylim([0,100])

    plt.gcf().subplots_adjust(bottom=0.27)

    ax.set_xticks(ind+width)
    ax.set_xticklabels(network_, rotation=90)
    plt.grid()

    plt.savefig('results_' + str(i) + '.pdf')

