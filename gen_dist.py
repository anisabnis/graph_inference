import sys
from collections import defaultdict
paths = dict()

dir = sys.argv[1]
f = open(dir + '/orig_path.txt', 'r')
for l in f:
    l = l.strip().split(' ')
    s = l[0]
    if s not in paths:
        paths[s] = list()

    paths[s].append(l)

i = 1
f = open(dir + '/distances.txt', 'w')
for s in paths:
    for p in paths[s]:
        d = p[-1]
        f.write(s + ' ' + d + ' ' + str(len(p)) + ' ' + str(i) + "\n")
        i += 1
f.close()

