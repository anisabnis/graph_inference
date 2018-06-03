import sys
network = sys.argv[1]
from collections import defaultdict

f = open('results_distance/' + str(network) + "/orig_path.txt", "r")
path_lengths=defaultdict(list)
path_destinations= defaultdict(list)

for l in f:
    l = l.strip().split()
    s=l[0]
    d=l[-1]
    path_lengths[s].append(len(l))
    path_destinations[s].append(d)
    
f1 = open('results_random_err/' + str(network) + "/rd0.txt", "w")
for s in path_lengths:
    path_ls = path_lengths[s]
    path_dns = path_destinations[s]
    
    wr = [x for _,x in sorted(zip(path_ls,path_dns))]
    
    f1.write(s + ";" + " ".join(wr) + ";" + " ".join(["t"] * (len(wr) - 1)) + "\n")
f1.close()
