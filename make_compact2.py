import sys
import os

dir = sys.argv[1]
o_dir = sys.argv[2]

f = open(dir + '/orig_path.txt', 'r')
orig_vertices = set()

orig_paths=dict()
egress_routers=set()

o_edges = set()

for l in f:
    l=l.strip().split(' ')

    egress_routers.add(l[1])
    egress_routers.add(l[-2])

    for r in l[1:-1]:
        orig_vertices.add(r)
        
    for i in range(1, len(l) - 2):
        edge = [l[i], l[i+1]]
        edge.sort()
    
    o_edges.add(((edge[0], edge[1])))
    
    s = l[0]
    d = l[-1]
    orig_paths[((s,d))] = l
    
    
f = open(o_dir + '/new_paths.txt', 'r')
new_vertices = set()
new_paths = dict()

for l in f:
    l=l.strip().split(' ')

    for r in l[1:-1]:
        new_vertices.add(r)

    s=l[0]
    d=l[-1]
    new_paths[((s,d))] = l

extra_vertices = len(orig_vertices) - len(new_vertices)
print(extra_vertices)
j = 0

while extra_vertices > 0:
    extra_vertices =-1

    for e in o_edges:
        
        v1 = e[0]
        v2 = e[1]
        if v1 in egress_routers and v2 in egress_routers:
            continue

        if v2 in egress_routers:
            tmp = v2
            v2 = v1
            v1 = tmp

        print(v1, v2)
        orig_path2 = dict()
        j += 1
        for p in orig_paths:
            new_p = []
            path = orig_paths[p]
            s = path[0]
            d = path[-1]

            for i in range(len(path)):
                if path[i] == v2 and path[i-1] == v1:
                    continue
                elif path[i] == v2 and path[i+1] != v1:
                    new_p.append(v1)
                elif path[i] == v2 and path[i+1] == v1:
                    continue
                else:
                    new_p.append(path[i])
            orig_path2[(s,d)] = new_p

        nd = str(dir) + "/" + str(j)
        os.system("mkdir " + nd)
        f = open(nd + "/orig_path.txt", "w")
        for p in orig_path2:
            f.write(" ".join([r for r in orig_path2[p]]))
            f.write("\n")
        f.close()
            
                       
                
