import sys
import os
from operator import itemgetter
from collections import defaultdict

import networkx as nx
import json

dir = str(sys.argv[1])


#graph_merge = str(sys.argv[2])

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

os.system("cat tree.lst | grep 'VAR ' | grep -v objvar | cut -d ' ' -f 3- | sed -n '/ /s/  */ /gp' | cut -d ' ' -f 1,3 > solution.txt")

trees_s = dict()
trees_d = dict()

all_edges = defaultdict(lambda : defaultdict(float))


f = open(dir + '/orig_path.txt')
fi = open(dir + '/o_edges.txt', 'w')
for l in f:
    l = l.strip().split(' ')
    for i in range(len(l) - 1):
        s = l[i]
        d = l[i + 1]
        fi.write(str(s) + " " + str(d) + "\n")

fi.close()
f.close()

f = open('solution.txt', 'r')
for l in f:
    l = l.strip().split(' ')
    
    if l[0][0] == 's':
        if l[1] == '.':
            continue
        dat = float(l[1])
        
        if dat >= 0:
            var = l[0].split('_')
            src = var[3]
            if src not in trees_s:
                trees_s[src] = list()

            trees_s[src].append(tuple((tuple((var[1], var[2])),dat)))
            all_edges[src][var[1] + "->" + var[2]] = dat


#     elif l[0][0] == 'd':
#         if l[1] == '1.0000':
#             var = l[0].split('_')
#             dst = var[3]
#             if dst not in trees_d:
#                 trees_d[dst] = list()

#             trees_d[dst].append(tuple((var[1], var[2])))

f.close()

json.dump(all_edges, open(dir + 'edges.json', 'w'), indent=1)

f = open(dir + '/graph.txt', 'r')
enclaves = list()
for l in f:
    l = l.split(' ')
    enclaves.extend([e for e in l if hasNumbers(e) == False])

f.close()

# f.close()
for src in trees_s:
    s = sorted(trees_s[src], key=itemgetter(0))
    print("trees_source :", src, s)


all_paths = list()

#f = open(dir + '/new_paths.txt' ,'r')
fi = open(dir + '/new_edges.txt' , 'w')
for src in trees_s:
    edges = trees_s[src]
    G = nx.Graph()
    #if src not in ["a", "b", "e", "g"]:
    #    continue
    for edge in edges:
        edge = edge[0]
        print(edge)
        fi.write(str(edge[0]) + " " + str(edge[1]) + "\n")
        G.add_edge(edge[0], edge[1])

    for dst in trees_s:
        if dst != src:
            s_path = nx.dijkstra_path(G, src, dst)
            all_paths.append(s_path)
            print(s_path)
#f.close()
fi.close()

f = open(dir + '/new_paths.txt', 'w')
all_paths = sorted(all_paths, key=itemgetter(0))
for path in all_paths:
    f.write(' '.join(path))
    f.write('\n')

f.close()

f = open(dir + '/new_paths_dst.txt', 'w')
all_paths = sorted(all_paths, key=itemgetter(-1))

for path in all_paths:
    f.write(' '.join(path))
    f.write('\n')

f.close()

## detect rhombuses


adjacencies = defaultdict(set)
for l in all_paths:
    for i in range(len(l) - 1):
        fv = l[i]
        sv = l[i+1]
        
        adjacencies[fv].add(sv)
        adjacencies[sv].add(fv)

f = open(dir + '/adjacencies.txt', 'w')
for fv in adjacencies:
    f.write(fv + ' ' + ' '.join(adjacencies[fv]))
    f.write('\n')
f.close()
    


# for p in paths:
#     edges = paths[p]
#     src = p[0]
#     dst = p[1]
    
#     path = [src]
#     curr_node = src

#     while curr_node != dst:
#         for e in edges:
#             if e[0] == curr_node:
#                 path.append(e[1])
#                 curr_node = e[1]

#     all_paths.append(path)

# all_paths = sorted(all_paths, key=itemgetter(0))

# f = open(dir + '/path.txt' , 'w')
# for path in all_paths:
#     f.write(' '.join(path))
#     f.write('\n')
# f.close()


