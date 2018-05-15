import sys
import os
from operator import itemgetter
from collections import defaultdict
from bs4 import BeautifulSoup as Soup
import networkx as nx
import json
from gen_dot import *

dir = str(sys.argv[1])
enc = str(sys.argv[2])
enclave = str(sys.argv[3])

mapping = defaultdict(str)

os.system("cat dict.txt | grep i | grep _ | sed -n '/ /s/  */ /gp' > var.txt")
os.system("sed 's/^[ \t]*//' var.txt > sol.txt")

f = open("sol.txt", "r")
for l in f:
    l = l.strip().split(' ')
    mapping[l[0]] = l[1]
f.close()

handle = open(dir + '/res' + enc + '.xml').read()
soup = Soup(handle, 'xml')

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

variables = defaultdict(int)

for var in soup.findAll('variable'):
    var_name = var["name"]
    var_value = round(float(var["value"]))
    variables[var_name] = var_value

os.system("cat tree.lst | grep 'VAR ' | grep -v objvar | cut -d ' ' -f 3- | sed -n '/ /s/  */ /gp' | cut -d ' ' -f 1,3 > solution.txt")

trees_s = dict()
trees_d = dict()

all_edges = defaultdict(lambda : defaultdict(float))

all_paths = list()

dst_enclaves = set()
f = open(dir + '/orig_path.txt')
fi = open(dir + '/o_edges.txt', 'w')
for l in f:
    l = l.strip().split(' ')
    all_paths.append(l)

    for i in range(len(l) - 1):
        s = l[i]
        d = l[i + 1]

        fi.write(str(s) + " " + str(d) + "\n")

    dst_enclaves.add(l[-1])

fi.close()
f.close()

gen_dot(all_paths, dir, 'orig')

#enclaves = ['a', 'b', 'c', 'd', 'e', 'f']
enclaves = [enclave]
for var_name in variables:
    var_map = mapping[var_name]
    if var_map == '':
        continue

    if var_map[0] == 's':
        if variables[var_name] > 0:
            dat = float(variables[var_name])
            var = var_map.split('_')
            src = var[3]
            if src not in enclaves:
                continue

            if src not in trees_s:
                trees_s[src] = list()

            trees_s[src].append(tuple((var[1], var[2])))                                      

json.dump(all_edges, open(dir + 'edges.json', 'w'), indent=1)

f = open(dir + '/graph.txt', 'r')
enclaves = [enclave]
for src in trees_s:
    s = sorted(trees_s[src], key=itemgetter(0))
    print("trees_source :", src, s)

all_paths = list()
fi = open(dir + '/new_edges.txt' , 'w')
for src in enclaves:
    edges = trees_s[src]
    G = nx.Graph()
    for edge in edges:
        print(edge)
        fi.write(str(edge[0]) + " " + str(edge[1]) + "\n")
        G.add_edge(edge[0], edge[1])

    for dst in dst_enclaves:
        if dst != src:
            s_path = nx.dijkstra_path(G, src, dst)
            all_paths.append(s_path)
            print("aa", s_path)
fi.close()

f = open(dir + '/new_paths.txt', 'w')
all_paths = sorted(all_paths, key=itemgetter(0))

gen_dot(all_paths, dir, 'inf')
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


