import sys, os
import random
import copy

dir=sys.argv[1]

new_vertices = set()
f = open(dir + '/new_paths.txt', 'r')
for l in f:
    l = l.strip().split()
    for r in l:
        new_vertices.add(r)
f.close()


f1 = open(dir + '/mapping.txt', 'w')
def write_output(orig_path2, dir):

    os.system("mkdir " + dir + "/output/")
    new_ = open(dir + '/output' + '/orig_path.txt' , 'w')

    for p in orig_path2:
        path = orig_path2[p]
        new_.write(' '.join([x for x in path]))
        new_.write("\n")

    new_.close()

enclaves = set()

def make_compact(paths, nodes):

    print("make_compact")

    egress_routers = set()
    all_routers = set()

    for p in paths:
        path = paths[p]
        egress_routers.add(path[1])
        for r in path:
            all_routers.add(r)

    print(egress_routers)
    print(all_routers)
    print(enclaves)

    internal_nodes = all_routers - egress_routers - enclaves

    if len(internal_nodes) == 0:
        print("here ")
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

    print(orig_path2)
    return orig_path2

if __name__ == "__main__":

    orig_paths=dict()
    f = open(dir + '/orig_path.txt' , 'r')
    enclaves = set()

    for l in f:
        l = l.strip().split(' ')
        s = l[0]
        d = l[-1]
        orig_paths[((s,d))] = l
        enclaves.add(s)
    f.close()
    
    print("orig_paths", orig_paths)

    f = open(dir + '/edit.txt' ,'r')
    for l in f:
        l = l.strip().split(' ')
        orig_paths = make_compact(orig_paths, l)    

    write_output(orig_paths, dir)
        