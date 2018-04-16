import sys
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from collections import defaultdict


topology = sys.argv[1]

def prune(src, paths):
    indegree = defaultdict(lambda:defaultdict(lambda:0))
    outdegree = defaultdict(lambda:defaultdict(lambda:0))

    for p in paths:
        for i, r in enumerate(p):
            if i == len(p) - 1:
                continue
            if i == 0:
                continue
            outdegree[r][p[i+1]] = outdegree[r][p[i+1]] + 1

    two_degree_routers = [r for r in outdegree if len(outdegree[r]) == 1]

    new_paths = []
    for p in paths:
        np = [i for i in p if i not in two_degree_routers]
        new_paths.append(np)

    return new_paths

inp_file = open(topology + '/orig_path.txt', 'r')
paths = defaultdict(list)

for l in inp_file:
    l = l.strip().split(' ')
    s = l[0]
    paths[s].append(l)

for s in paths:
    G = nx.DiGraph()
    for p in paths[s]:
        for i in range(len(p) - 1):
            G.add_edge(p[i], p[i+1])
    
    nx.draw(G, with_labels = True, pos=graphviz_layout(G, prog='dot'), node_color='w')
    plt.savefig(topology + '/' + s + '-orig_with2d.pdf')
    plt.gcf().clear()


new_path = defaultdict(list)

for s in paths:
    new_paths = prune(s, paths[s])
    new_path[s] = new_paths


for s in new_path:
    G = nx.DiGraph()
    for p in new_path[s]:
        for i in range(len(p) - 1):
            G.add_edge(p[i], p[i+1])
    
    nx.draw(G, with_labels = True, pos=graphviz_layout(G, prog='dot'), node_color='w')
    plt.savefig(topology + '/' + s + '-orig.pdf')
    plt.gcf().clear()

inp_file = open(topology + '/new_paths.txt', 'r')
paths = defaultdict(list)

for l in inp_file:
    l = l.strip().split(' ')
    s = l[0]
    paths[s].append(l)

new_path = defaultdict(list)

for s in paths:
    G = nx.DiGraph()
    for p in paths[s]:
        for i in range(len(p) - 1):
            G.add_edge(p[i], p[i+1])

    nx.draw(G, with_labels = True, pos=graphviz_layout(G, prog='dot'), node_color='w')
    plt.savefig(topology + '/' + s + '-inf_with2d.pdf')
    plt.gcf().clear()


for s in paths:
    new_paths = prune(s, paths[s])
    new_path[s] = new_paths

paths = new_path

for s in paths:
    G = nx.DiGraph()
    for p in paths[s]:
        for i in range(len(p) - 1):
            G.add_edge(p[i], p[i+1])

    nx.draw(G, with_labels = True, pos=graphviz_layout(G, prog='dot'), node_color='w')
    plt.savefig(topology + '/' + s + '-inf.pdf')
    plt.gcf().clear()


# G = nx.DiGraph()
# G.add_node(prev_enclave)

# i = 0
# g = nx.Graph()

# for l in inp_file:
#     l = l.strip().split(' ')
#     if l[0] != prev_enclave:
#         nx.draw(G, with_labels = True, pos=graphviz_layout(G, prog='dot'), node_color='w')
#         i += 1
#         plt.title(prev_enclave)
#         plt.savefig(topology + '/' + prev_enclave + '-orig.pdf')
#         plt.gcf().clear()
#         G = nx.DiGraph()
#         prev_enclave = l[0]
#         G.add_node(prev_enclave)

#     for i in range(len(l)-1):
#         G.add_edge(l[i], l[i+1])
#         g.add_edge(l[i], l[i+1])

# nx.draw(G, with_labels = True, pos=graphviz_layout(G, prog='dot'), node_color='w')
# plt.title(prev_enclave)
# plt.savefig(topology + '/' + prev_enclave + '-orig.pdf')
# plt.gcf().clear()

# nx.draw_spring(g, with_labels = True)
# plt.savefig(topology + '/orig-graph.pdf')
# inp_file.close()

# prev_enclave = 'a'

# topology = sys.argv[1]

# inp_file = open(topology + '/new_paths.txt', 'r')
# G = nx.DiGraph()
# G.add_node(prev_enclave)

# g = nx.Graph()

# for l in inp_file:
#     l = l.strip().split(' ')
#     if l[0] != prev_enclave:
#         nx.draw(G, with_labels = True, pos=graphviz_layout(G, prog='dot'),node_color='w')
#         plt.title(prev_enclave)
#         plt.savefig(topology + '/' + prev_enclave + '-final.pdf')
#         plt.gcf().clear()
#         G = nx.DiGraph()
#         prev_enclave = l[0]
#         G.add_node(prev_enclave)
#     for i in range(len(l)-1):
#         G.add_edge(l[i], l[i+1])
#         g.add_edge(l[i], l[i+1])


# nx.draw(G, with_labels = True, pos=graphviz_layout(G, prog='dot'), node_color='w')
# plt.title(prev_enclave)
# plt.savefig(topology + '/' + prev_enclave + '-final.pdf')
# plt.gcf().clear()

# nx.draw_random(g,with_labels=True)
# plt.savefig(topology + '/final_new.pdf')
# inp_file.close()
