import os
import sys
import itertools
import random

network = sys.argv[1]
i = int(sys.argv[2])

print("Network : ", network)

sources = set()
paths = dict()

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def findAllPermutations(S, m):
    return set(itertools.combinations(S, m))



#for i in [1,2,3,4,5]:
constraints = {}
for j in range(1,i+1):
    if i != 0:
        f = open("results_random_err" +"/" + network + "/" + str(j) + "/orig_path.txt", "r")
    else : 
        f = open("results_random_err" +"/" + network +  "/orig_path.txt", "r")

    for l in f:
        l = l.strip().split(" ")
        s=l[0]
        sources.add(s)
        d=l[-1]
        paths[((s,d))] = l
    f.close()

    if i != 0:
        f = open("results_random_err" +"/" + network + "/" + str(j) + "/correlations.txt", "w")
    else :
        f = open("results_random_err" +"/" + network + "/correlations.txt", "w")

    for s in sources:
        req_dsts = [d for d in sources if d != s]
        req_dsts_subsets = findAllPermutations(req_dsts, 3)

        for sub in req_dsts_subsets:
            ucv1 = sub[0]
            cv = sub[1]
            ucv2 = sub[2]

            key = s + ":" + ucv1 + ":" + cv + ":" + ucv2

            p1 = paths[((s, ucv1))]
            p2 = paths[((s, cv))]
            p3 = paths[((s, ucv2))]
        
            l1 = len(list(set(p1).intersection(p2)))
            l2 = len(list(set(p2).intersection(p3)))        
        
            if random.randint(1,10 - j) <= j:
                make_err_psm = True
            else :
                make_err_psm = False

            if l1 > l2:
                if make_err_psm == False:
                    if key not in constraints:
                        constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " g " + "t" 
                    else:
                        continue
                        
                else:
                    if key not in constraints:
                        constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " l " + "f" 
                    newk = constraints[key]
                    if newk.split(" ")[-1] == "t":
                        constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " l " + "f" 
 
            elif l2 > l1:
                if make_err_psm == False:
                    if key not in constraints:
                        constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " l " + "t" 
                    else:
                        continue
                else :
                    if key not in constraints:
                        constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " g " + "f" 
                    newk = constraints[key]
                    if newk.split(" ")[-1] == "t":
                        constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " g " + "f" 
            else:
                if make_err_psm == False:
                    if key not in constraints:
                        constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " e " + "t"
                    else:
                        continue
                else :
                    decide = random.randint(1,2)
                    if key not in constraints:
                        if decide == 1:
                            constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " l " + "f"                        
                        else:
                            constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " g " + "f"
                        
                    else :
                        newk = constraints[key]
                        if newk.split(" ")[-1] == "t":                        
                            if decide == 1:
                                constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " l " + "f"                        
                            else:
                                constraints[key] = s + " " + ucv1 + " " + cv + " " + ucv2 + " g " + "f"

                        
                
    for k in constraints:
        f.write(constraints[k] + "\n")

    f.close()
         
        
