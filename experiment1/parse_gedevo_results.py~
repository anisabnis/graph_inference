import sys
from collections import defaultdict
import numpy as np
from edit_distance import *

dir=sys.argv[1]
f = open('gedevo/distance' + str(dir) + '.matching' , 'r')
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

            mapped_v -= 1
            orig_v = l[0]
            if orig_v == '-':
                orig_v = inf
                inf += 1
            else :
                orig_v = int(l[0])
            if orig_v >= 20 and orig_v < 50:
                orig_v -= 10

            orig_v -= 1
            if orig_v >= 49 or mapped_v >= 49:
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
o_paths = dict()
enclaves = set()

for l in f:
    l = l.strip().split(' ')
    nl = []
    s = l[0]
    enclaves.add(s)
    d = l[-1]
    for r in l:
        nl.append(orig_map[0][r])
    orig_paths.append(nl)
    o_paths[((s,d))] = nl
f.close()
no_paths = (len(enclaves)) * (len(enclaves) - 1)

#print("orig_paths")
#for o in orig_paths:
#    print(o)

new_paths = []
f = open(dir + '/new_paths.txt' , 'r')
n_paths = dict()
for l in f:
    l = l.strip().split(' ')
    nl = []
    s = l[0]
    d = l[-1]
    for r in l:
        nl.append(orig_map[1][r])        
    new_paths.append(nl)
    n_paths[((s,d))] = nl
f.close()


x = 100
n1_paths = dict()
for k in n_paths:
    np1 = []
    nl = n_paths[k]
    for r in nl:
        if r in mapping1:
            np1.append(mapping1[r])
        else :
            np1.append(x)
    
    n1_paths[k] = np1

n_paths = n1_paths
#print("new", n_paths)

#print("Inferred")
#for n in new_paths:
#    print(n)

ted = 0
for eps in o_paths:
    ed = edit_distance(o_paths[eps], n_paths[eps])
    ted+= ed

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
print(dir + ":" + str(correctness) + ":" + str(ted/no_paths))
