import os
import sys
import itertools

network = sys.argv[1]

print("Network : ", network)

sources = set()
paths = dict()

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def findAllPermutations(S, m):
    return set(itertools.combinations(S, m))

f = open("results_tree_algorithm/" +  network + "/orig_path.txt", "r")
for l in f:
    l = l.strip().split(" ")
    s=l[0]
    sources.add(s)
    d=l[-1]
    paths[((s,d))] = l
f.close()

for s in sources:
    os.system("mkdir " + "results_tree_algorithm" + "/" + network + "/" + s)
    
    f = open("results_tree_algorithm" +"/" + network + "/" + s + "/orig_path.txt", "w")
    for s2 in sources:
        if s == s2:
            continue
        f.write(" ".join(paths[((s, s2))]) + "\n")

    f.close()
    
    req_dsts = [d for d in sources if d != s]
    req_dsts_subsets = findAllPermutations(req_dsts, 3)

    f = open("results_tree_algorithm" +"/" + network + "/" + s + "/correlations.txt", "w")

    for sub in req_dsts_subsets:
        ucv1 = sub[0]
        cv = sub[1]
        ucv2 = sub[2]

        p1 = paths[((s, ucv1))]
        p2 = paths[((s, cv))]
        p3 = paths[((s, ucv2))]

        l1 = len(list(set(p1).intersection(p2)))
        l2 = len(list(set(p2).intersection(p3)))
        
        if l1 > l2:
            f.write(s + " " + ucv1 + " " + cv + " " + ucv2 + " g\n")
        elif l2 > l1:
            f.write(s + " " + ucv1 + " " + cv + " " + ucv2 + " l\n")
        else:
            f.write(s + " " + ucv1 + " " + cv + " " + ucv2 + " e\n")

            


         
        
