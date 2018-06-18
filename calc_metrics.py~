import sys
import numpy as np
import copy
from edit_distance import *
import re

dir=sys.argv[1]
compact=sys.argv[2]

experiment = dir.split("/")[1]
#experiment = re.sub('\d', '', experiment)

def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)

def Union(lst1, lst2):
    return set(lst1).union(lst2)

def make_compact(paths, nodes):

    egress_routers = set()
    all_routers = set()

    enclaves = set()

    for p in paths:
        path = paths[p]
        egress_routers.add(path[1])
        enclaves.add(path[0])
        for r in path:
            all_routers.add(r)

    internal_nodes = all_routers - egress_routers - enclaves

    if len(internal_nodes) == 0:
        return

    v1 = nodes[0]
    v2 = nodes[1]

    orig_path2 = dict()

    for p in paths:
        new_p = []
        path = paths[p]
        s = path[0]
        d = path[-1]

        for i in range(len(path) - 1):
            if path[i] == v2 and path[i-1] == v1:
                continue
            elif path[i] == v2 and path[i+1] != v1:
                new_p.append(v1)
            elif path[i] == v2 and path[i+1] == v1:
                continue
            else:
                new_p.append(path[i])

        new_p.append(d)
        orig_path2[(s,d)] = new_p

    return orig_path2

def get_orig_edges(dir, compact):
    orig_paths = {}
    f = open(dir + "/" + "tata_paths.txt", "r")

    enclaves = set()
    egress = set()

    egress_map = dict()

    for l in f:
        l = l.strip().split()
        s = l[0]
        d = l[-1]
        orig_paths[((s,d))] = l
        enclaves.add(s)
    f.close()

    if compact == "t":
        f = open(dir + '/edit.txt' ,'r')

        for l in f:
            l = l.strip()
            if l == "x":
                continue
            l = l.split(' ')
            orig_paths = make_compact(orig_paths, l)

        f.close()

    ## egress map should be created here
    for p in orig_paths:
        p = orig_paths[p]
        egress.add(p[1])
        egress_map[p[1]] = p[0]
        egress.add(p[-2])
        egress_map[p[-2]] = p[-1]
        
    edges = set()
    int_nodes = set()

    #print(egress_map)

    for p in orig_paths:
        p = orig_paths[p]
        for i in range(len(p) - 1):
            s = p[i]
            d = p[i+1]

            if s in egress_map:
                s = egress_map[s] + '1'
            if d in egress_map:
                d = egress_map[d] + '1'

            e = [s, d]
            e.sort()
            e = ((e[0], e[1]))
            edges.add(e)


    new_orig_paths = {}
    for p in orig_paths:
        newp = []
        p = orig_paths[p]

        src = p[0]
        dst = p[-1]

        for s in p:
            if s in egress_map:
                newp.append(egress_map[s] + '1')
            else:
                newp.append(s)

        new_orig_paths[((src,dst))] = newp

        
    for p in orig_paths:
        p = orig_paths[p]
        for i in p:
            if i not in egress and i not in enclaves:
                int_nodes.add(i)
            

    return edges, int_nodes, new_orig_paths

def get_inf_edges(dir):
    orig_paths = {}
    f = open(dir + "/" + "new_paths.txt", "r")

    enclaves = set()
    egress = set()
    all_nodes = set()

    for l in f:
        l = l.strip().split()
        s = l[0]
        d = l[-1]
        orig_paths[((s,d))] = l
        enclaves.add(s)
        egress.add(l[1])
        egress.add(l[-2])
        for n in l:
            all_nodes.add(n)
    f.close()

    edges = set()


    for p in orig_paths:
        p = orig_paths[p]
        for i in range(len(p) - 1):
            e = [p[i], p[i+1]]
            e.sort()
            e = ((e[0], e[1]))
            edges.add(e)
    
    int_nodes = all_nodes - enclaves - egress
            
    return edges, int_nodes, orig_paths                


orig_edges, orig_int_nodes, orig_paths = get_orig_edges(dir, compact)
inf_edges, inf_int_nodes, inf_paths = get_inf_edges(dir)

def score_match(o_edges, inf_edges, o_paths, inf_paths, m, inf_nodes):
    new_o_edges = set()
    
    #print("Original edges", o_edges)

    for o in o_edges:
        new_o = list(o)
        for i in range(2):
            if new_o[i] in m:
                index = m.index(new_o[i])
                if index < len(inf_nodes):
                    matched = inf_nodes[index]
                    new_o[i] = matched

        new_o.sort()
        new_o_edges.add(((new_o[0],new_o[1])))

    new_paths = dict()

    for o in o_paths:
        new_p = copy.deepcopy(o_paths[o])
        s = new_p[0]
        d = new_p[-1]

        for i in range(len(new_p)):
            if new_p[i] in m:
                index = m.index(new_p[i])
                if index < len(inf_nodes):
                    matched = inf_nodes[index]
                    new_p[i] = matched 
        

        new_paths[((s,d))] = new_p

    ## Find intersection and union and divide 
    uni = Union(new_o_edges, inf_edges)
    inter = Intersection(new_o_edges, inf_edges)

    score = len(inter)/len(uni)

    ted = 0
    for eps in o_paths:
        #print(new_paths[eps], " ", inf_paths[eps])
        ed = edit_distance(new_paths[eps], inf_paths[eps])
        ted+= ed

    ted = ted/len(o_paths)

    return score, ted


import itertools
matchings = list(itertools.permutations(orig_int_nodes))

orig_int_nodes = list(orig_int_nodes)
inf_int_nodes = list(inf_int_nodes)


max_score = 0
min_ped = 100
for m in matchings:
    s,p = score_match(orig_edges, inf_edges, orig_paths, inf_paths, m, inf_int_nodes) 
    if s > max_score:
        max_score = s
        min_ped = p

print(experiment +  " " + str(max_score) + " " + str(min_ped))
