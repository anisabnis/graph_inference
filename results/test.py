import sys
from collections import defaultdict
import copy

p_file = sys.argv[1]

f = open(p_file + '/orig_path.txt', 'r')
paths = defaultdict(lambda : defaultdict(str))

for l in f:
    l = l.strip().split(' ')
    src = l[0]
    dst = l[-1]
    paths[src][dst] = l

f.close()

## check bidirectionaly
for s in paths:
    for d in paths:
        if s == d:
            continue

        p1 = paths[s][d]
        p2 = copy.deepcopy(paths[d][s])
        p2.reverse()

        if p1 != p2:
            print(p1, p2, "unequal")
            break

for s in paths:
    indegree = defaultdict(set)
    for d in paths:
        p = paths[s][d]
        for i in range(1, len(p)-1):
            indegree[p[i]].add(p[i-1])
#         for i, r in enumerate(p[1:len(p)-1]):
#             indegree[r].add(p[i-1])

    for r in indegree:
        if len(indegree[r]) > 1:
            print("Source Tree Violation at ", s, r, indegree[r])


for d in paths:
    outdegree = defaultdict(set)
    for s in paths:
        p = paths[s][d]
        for i in range(0, len(p)-1):
            outdegree[p[i]].add(p[i+1])

    for r in outdegree:
        if len(outdegree[r]) > 1:
            print("Destination tree Violation at ", d, r)


indegree = defaultdict(lambda:defaultdict(lambda:int))
outdegree = defaultdict(lambda:defaultdict(lambda:int))

for p in paths:
    for i, r in enumerate(p[1:len(p)-1]):
        indegree[r][p[i]] = indegree[r][p[i]] + 1
        outdegree[r][p[i+2]] = outdegree[r][p[i+2]] + 1

two_degree_routers = [r for r in indegree if len(indegree[r]) <= 2 and len(outdegree[r]) <= 2]
print("2d routers", two_degree_routers)
    
    
