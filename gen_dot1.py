#node_pos = {'a': "40,10!", 'b':"50,20!", 'c':"20,10!", 'd':"20,30!", 'e':"30,50!", 'f':"10,50", 'a1':"40,15!", 'b1':"45,20!", 'c1':"30,15!", 'd1':"25,30!", 'e1':"25,45!", 'f':"15,45!"}

node_pos = {'a': "8,2!", 'b':"10,4!", 'c':"4.5,2!", 'd':"2,5!", 'e':"7,9!", 'f':"3,9!", 'a1':"8,3!", 'b1':"9,4!", 'c1':"4.5,3!", 'd1':"3,5!", 'e1':"7,7!", 'f1':"3,8!"}

import sys
from graphviz import Digraph
from graphviz import Graph

def gen_dot(paths, dir, type):
    ## Generate a dot file
    nodes = set()
    edges = set()
    
    dot = Graph(format='png')
    dot.attr('node', labelfontsize='50')

    node_map = dict()
    for p in paths:
        s = p[0]
        d = p[-1]
        for i in range(len(p) -1):
            if i == 1:
                node_map[p[i]] = s + '1'
            elif i == len(p) - 2:
                node_map[p[i]] = d + '1'
    
    for p in paths:
        s = p[0]
        d = p[-1]
        for i in range(len(p) - 1):
            n1 = p[i]
            n2 = p[i + 1]
            if n1 in node_map:
                n1 = node_map[n1]
            if n2 in node_map:
                n2 = node_map[n2]

            nodes.add(n1)
            edge = [n1, n2]
            edge.sort()
            edges.add((edge[0], edge[1]))


    for n in nodes:
        if n in node_pos:
            dot.node(n, pos=node_pos[n], labelfontsize='50')
        else:
            dot.node(n, labelfontsize='50')

    for e in edges:
        dot.edge(e[0], e[1])


    dot.render(dir + '/' + type + '.dot')


if __name__ == "__main__":
    dir = sys.argv[1]
    
    op = list()
    f = open(dir + "/orig_path.txt", 'r')
    for l in f:
        l = l.strip().split(' ')
        op.append(l)

    gen_dot(op, dir, "orig")


    np = list()
    f = open(dir + "/new_paths.txt", 'r')
    for l in f:
        l = l.strip().split(' ')
        np.append(l)

    gen_dot(np, dir, "inf")
    
    
    
