import sys, os
import random
import copy

dir=sys.argv[1]
hdeep = int(sys.argv[2])


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

new_vertices = set()
f = open(dir + '/new_paths.txt', 'r')

for l in f:
    l = l.strip().split()
    for r in l:
        new_vertices.add(r)
f.close()

gc = 0
gcc=0

f1 = open(dir + '/mapping.txt', 'w')

def write_output(orig_path2, new_edges, new_nodes, dir, gc):
    os.system("mkdir " + dir + "/" + str(gc))
    new_ = open(dir + '/' + str(gc) + '/orig_edges.txt' , 'w')
    for e in new_edges:
        new_.write(str(e[0]) + " " + str(e[1]) + "\n")
    new_.close()

egress_routers = set()
all_routers = set()
enclaves = set()

def make_compact(paths, depth, type, edges, nodes):

    global hdeep

    global gcc

    if gcc > 2000:
        return

    if depth >= hdeep:
        return


    global egress_routers
    global enclaves

    for e in edges:
        all_routers.add(e[0])
        all_routers.add(e[1])

    internal_nodes = all_routers - egress_routers - enclaves

    if len(internal_nodes) == 0:
        return

    consider = internal_nodes.union(egress_routers)

    if type == "merge":
        if len(all_routers) <= len(new_vertices):
            return

        for v1 in consider:
            for v2 in internal_nodes:
                if v1 == v2:
                    continue

                orig_path2 = dict()
                global gc
                gc += 1
                
#                if depth == 1 and gc%2 == 0:
#                    continue
                if depth == 2 and gc%10 != 0:
                    continue
                
                elif depth > 2 and gc % 15 != 0:
                    continue

                global gcc
                gcc += 1

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

                e = ((v1, v2))
                e1 = ((v2, v1))

                new_edges = copy.deepcopy(edges)

                if e in edges:
                    new_edges.discard(e)

                if e1 in edges:
                    new_edges.discard(e1)

                discard_edges = []
                insert_edges = []

                for e in new_edges:
                    ne = [e[0], e[1]]

                    if ne[0] == v2:
                        ne[0] = v1
                    if ne[1] == v2:
                        ne[1] = v1
                    
                    discard_edges.append(e)
                    insert_edges.append((ne[0], ne[1]))

                for d in discard_edges:
                    new_edges.discard(d)


                for d in insert_edges:
                    new_edges.add(d)


                new_nodes = copy.deepcopy(nodes)
                new_nodes.discard(v2)

                write_output(orig_path2, new_edges, new_nodes, dir, gcc)

                f1.write(str(gcc) + " " + str(depth) + " " + str(v1) + " " + str(v2) + " merge" + "\n")

                #return 

                make_compact(orig_path2, depth + 1, "merge", new_edges, new_nodes)

    
    if type == "add":        
        for v1 in consider:
            for v2 in consider:
                if v1 == v2 :
                    continue
                elif ((v1,v2)) in edges:
                    continue
                elif ((v2, v1)) in edges:
                    continue
                else:
                    new_edges = copy.deepcopy(edges)
                    new_edges.add(((v1,v2)))
                    gc += 1

                    if depth == 1 and gc%2 == 0:
                        continue
                    if depth == 2 and gc%10 != 0:
                        continue
                    elif depth > 2 and gc % 15 != 0:
                        continue

                    global gcc
                    gcc += 1

                    write_output(paths, new_edges, nodes, dir, gcc)

                    f1.write(str(gcc) + " " + str(depth) + " " + str(v1) + " " + str(v2) + " add" + "\n")
                    make_compact(paths, depth + 1, "merge", new_edges, nodes)
                    make_compact(paths, depth + 1, "del", new_edges, nodes)
                    
                    
    if type == "del":
        for e in edges:
            if hasNumbers(e[0]) == False or hasNumbers(e[1]) == False:
                continue

            new_edges = copy.deepcopy(edges)
            new_edges.discard(e)
            gc += 1

            if depth == 1 and gc%2 == 0:
                continue
            if depth == 2 and gc%10 != 0:
                continue
            elif depth > 2 and gc %15 != 0:
                continue

            global gcc
            gcc += 1
            write_output(paths, new_edges, nodes, dir, gcc)

            f1.write(str(gcc) + " " + str(depth) + " " + str(e[0]) + " " + str(e[1]) + " del" +  "\n")
            make_compact(paths, depth + 1, "merge", new_edges, nodes)
            make_compact(paths, depth + 1, "add", new_edges, nodes)

#f1.close()

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

    edges = set()
    nodes = set()

    global egress_routers
    global enclaves

    for p in orig_paths:
        l = orig_paths[p]
        enclaves.add(l[0])
        for i in range(len(l) - 1):
            if i == 1:
                egress_routers.add(l[i])
            edge = [l[i], l[i+1]]
            edge.sort()
            edge = (edge[0], edge[1])
            edges.add(edge)
            nodes.add(l[i])
    
    make_compact(orig_paths, 0, "merge", edges, nodes)
#    make_compact(orig_paths, 0, "add", edges, nodes)
#    make_compact(orig_paths, 0, "del", edges, nodes)

    global gcc
    f = open(dir + "/no_edits", "w")
    f.write(str(gcc))
    f.close()
    