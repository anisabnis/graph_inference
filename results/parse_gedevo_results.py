import sys
from collections import defaultdict
import numpy as np

dir=sys.argv[1]
f = open('gedevo/result' + str(dir) + '.matching' , 'r')
mapping = defaultdict(str)
mapping1 = defaultdict(str)
orig = 50
inf = 50

start_ = False
start__ = False

for l in f:
    l=l.strip()
    l.replace('\n', '')

    if "Edge correctness" in l:
        l = l.split(":")
        correctness=l[1]

    elif "#" in l:
        continue
    elif l == "\n":
        continue
    else:
        l=l.split("\t")
        if l[0] == '':
            continue
        else:
            mapped_v = l[1]
            if mapped_v == '-':
                mapped_v = inf
                inf += 1
            else :
                mapped_v = int(l[1])
            if mapped_v >= 20 and mapped_v < 50:
                mapped_v -= 10

            orig_v = l[0]
            if orig_v == '-':
                orig_v = inf
                inf += 1
            else :
                orig_v = int(l[0])
            if orig_v >= 20 and orig_v < 50:
                orig_v -= 10

            if orig_v >= 50 or mapped_v >= 50:
                continue
            mapping[orig_v] = mapped_v
            mapping1[mapped_v] = orig_v


f = open(dir + '/output/map.txt')
orig_map = [defaultdict(), defaultdict()]
i = 0
for l in f:
    l=l.strip()
    l=l[1:-1]
    l = l.split(',')
    for m in l:
        m = m.split(':')
        m[1] = m[1].replace(" ", "")
        m[0] = m[0].replace(" ", "")
        m[0] = m[0][1:-1]
        m[1] = m[1][1:-1]
        orig_map[i][m[0]] = int(m[1])
    i += 1

f.close()      

orig_paths = []
f = open(dir + '/orig_path.txt' ,'r')
for l in f:
    l = l.strip().split(' ')
    nl = []
    for r in l:
        nl.append(orig_map[0][r])
    orig_paths.append(nl)
f.close()

new_paths = []
f = open(dir + '/new_paths.txt' , 'r')
for l in f:
    l = l.strip().split(' ')
    nl = []
    for r in l:
        nl.append(orig_map[1][r])        
    new_paths.append(nl)
f.close()

indices = [defaultdict(), defaultdict()]
i = 0
for v in mapping:
    indices[0][v] = i
    indices[1][mapping[v]] = i
    i += 1

siz = i

adj_A = np.zeros((i, i), dtype='int32')
adj_B = np.zeros((i, i), dtype='int32')
uncounted = 0

for p in orig_paths:
    for i in range(len(p) - 1):
        s = p[i]
        d = p[i+1]
        
        if s in mapping and d in mapping:
            adj_A[indices[0][s], indices[0][d]] = 1
        else :
            uncounted += 1

for p in new_paths:
    for i in range(len(p) - 1):
        s = p[i]
        d = p[i+1]
        
        if s in mapping1 and d in mapping1:
            adj_B[indices[1][s], indices[1][d]] = 1
        else:
            uncounted += 1

diff = np.linalg.norm(adj_A - adj_B, 2)
print(dir, correctness, 1 - diff/siz)
